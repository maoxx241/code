class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        # res=[]
        # for i in range(len(nums)//2):
        #     res.append(nums[i])
        #     res.append(nums[i+n])
        # return res
        getDesireIdx = lambda i: i*2 if i<n else (i-n)*2+1
        for i in range(2*n):
            j=i
            while nums[i]>=0:
                j=getDesireIdx(j)
                nums[i],nums[j]=nums[j],-nums[i]
        for i in range(2*n):
            nums[i]=-nums[i]
        return nums