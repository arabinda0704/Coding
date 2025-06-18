class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        balance=0
        n=len(gas)
        total=res=0
        for i in range(n):
            total+=gas[i]-cost[i]
            if total<0:
                total=0
                res=i+1
        return res


        