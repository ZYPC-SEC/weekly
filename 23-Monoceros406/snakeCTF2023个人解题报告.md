---
title: snakeCTF2023个人解题报告
date: 2023-12-09 20:16:36
tags: CTF
mathjax: true
---

# snakeCTF2023个人解题报告

## static warmup

差一点三血...不开心。

发现侧信道攻击点0x401FD3，直接用Pintools插桩去打：

```c++
#include <iostream>
#include <fstream>
#include "pin.H"
using std::cerr;
using std::endl;
using std::string;
static UINT64 icount=0;
VOID docount(VOID* addr) {
    if ((long)addr==0x401FD3)
        icount++;
    return;
};
VOID Instruction(INS ins,VOID* v){
    INS_InsertCall(ins,IPOINT_BEFORE,(AFUNPTR)docount,IARG_INST_PTR,IARG_END);
};
KNOB<string> KnobOutputFile(KNOB_MODE_WRITEONCE,"pintool","o","inscount.out","specify output file name");
VOID Fini(INT32 code,VOID* v){
    std::cout<<"Count "<<icount<<endl;
};
INT32 Usage(){
    cerr<<"This tool counts the number of dynamic instructions executed"<<endl;
    cerr<<endl<<KNOB_BASE::StringKnobSummary()<<endl;
    return -1;
};
int main(int argc,char* argv[]){
    if(PIN_Init(argc,argv))
        return Usage();
    INS_AddInstrumentFunction(Instruction,0);
    PIN_AddFiniFunction(Fini,0);
    PIN_StartProgram();
    return 0;
};
```

用Python脚本施行爆破：

```python
import subprocess,time,copy,os
STR_LEN=30
start_time=time.time()
out_file_path=r"ttext.txt"
exe_path=r"/home/monoceros406/SharedFiles/pintools/crackme"
dll_path=r"./MyPinTool.so"
record_ins_nums={}
except_str="snakeCTF{"
except_inss=0   
find_str=""
s_map="0123456789qwertyuiopasdfghjklzxcvbnm{}-_"
def sub_intreaction(input_msg):
    global start_time
    sh=subprocess.Popen(['./pin','-t',dll_path,'-o',out_file_path,'--',exe_path,input_msg.ljust(36,"0")],
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    get_input=sh.stdout.readlines()
    lenn=int(get_input[1][6:])
    if record_ins_nums and lenn>max(record_ins_nums.values()):
        record_ins_nums[input_msg]=lenn
        sh.kill()
        print(input_msg," : ",get_input)
        return 1
    record_ins_nums[input_msg]=lenn
    sh.kill()
    print(input_msg," : ",get_input)
    if b"success" in get_input[1]:
        print("Oh,my sir, you may got the flag:")
        print(input_msg)
        print(time.time() - start_time)
        exit()
    return 0
def intreaction():
    for i in range(len(s_map)):
        if sub_intreaction(except_str+s_map[i])==1:
            return
def pintools():
    global except_str,v,record_ins_nums,except_inss
    intreaction()
    for k,v in record_ins_nums.items():
        if v>=except_inss:
            except_str=copy.deepcopy(k)
            except_inss=v
    print(except_str," ",except_inss)
    record_ins_nums={}
    pintools()
if __name__=='__main__':
    pintools()
```



