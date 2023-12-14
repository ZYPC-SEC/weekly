---
title: LeetCode快速入门
date: 2023-12-02 19:33:36
tags: 算法
mathjax: true
---

# LeetCode快速入门

## C++

```c++
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> ans;
        for(int i=0;i<nums.size();i++)
            for(int j=i+1;j<nums.size();j++)
                if(nums.at(i)+nums.at(j)==target){
                    ans.push_back(i);
                    ans.push_back(j);
                    return ans;
                };
        return ans;
    };
};
```

## Java

```Java
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int len=nums.length;
        for(int i=0;i<len;i++)
            for(int j=i+1;j<len;j++)
                if(nums[i]+nums[j]==target)
                    return new int[]{i,j};
        return new int[0];
    };
};
```

## Python

```python
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
```

## Python3

```python
#!python3
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []
```

## C

```c
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    for(int i=0;i<numsSize;i++)
        for(int j=i+1;j<numsSize;j++)
            if(nums[i]+nums[j]==target){
                int* ans=malloc(sizeof(int)*2);
                ans[0]=i,
                ans[1]=j,
                *returnSize=2;
                return ans;
            };
    *returnSize=0;
    return NULL;
};
```

## Javascript

```javascript
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var n=nums.length;
    for(var i=0;i<n;i++)
        for(var j=i+1;j<n;j++)
            if(nums[i]+nums[j]==target){
                var ans=new Array(i,j);
                return ans;
            };
    return new Array(1);
};
```

