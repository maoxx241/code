class Solution:
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     if len(gas)==1 and gas[0]-cost[0]>=0:
    #         return 0
    #     gap=0
    #     for i in range(len(gas)):
    #         if gas[i]-cost[i]>gap:
    #             if self.helper(gas,cost,i)==True:
    #                 return i
        
    #     return -1
    
    
    # def helper(self, gas: List[int], cost: List[int], index: int):
    #     g=0
    #     for i in range(index,len(gas)):
    #         g+=gas[i]
    #         g-=cost[i]
    #         if g<0:
    #             return False
        
    #     for i in range(0,index+1):
    #         g+=gas[i]
    #         g-=cost[i]
    #         if g<0:
    #             return False
        
    #     return True

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, curr_tank = 0, 0
        starting_station = 0
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            # If one couldn't get here,
            if curr_tank < 0:
                # Pick up the next station as the starting one.
                starting_station = i + 1
                # Start with an empty tank.
                curr_tank = 0
        if total_tank<0:
            return -1
        return starting_station 