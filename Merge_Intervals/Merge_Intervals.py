class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans=[]
        index=-1
        intervals.sort(key=lambda i: i[0])
        for i in range(len(intervals)):
            if ans ==[]:
                ans.append(intervals[i])
                index+=1
                continue


            if intervals[i][0]<=ans[index][1] and intervals[i][1]>ans[index][1]:
                ans[index][1]=intervals[i][1]
            elif intervals[i][0]>ans[index][1] or intervals[i][1]<ans[index][0]:
                ans.append(intervals[i])
                index+=1
        
        return ans