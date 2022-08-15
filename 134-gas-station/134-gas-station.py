class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total = 0
        currGas = 0
        startStation = 0
        for i in range(n):
            total += gas[i] - cost[i]
            currGas += gas[i] - cost[i]
            if currGas < 0:
                startStation = i+1
                currGas = 0
        
        if total >= 0:
            return startStation
        else:
            return -1