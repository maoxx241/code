class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic={}
        st = []
        ans = []
        
        for x in nums2:
            while len(st) and st[-1] < x:
                dic[st.pop()] = x
            st.append(x)

        for x in nums1:
            ans.append(dic.get(x, -1))
            
        return ans