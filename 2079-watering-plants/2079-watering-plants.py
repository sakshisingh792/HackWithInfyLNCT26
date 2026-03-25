class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        n=len(plants)      
        steps=0
        water=capacity
        for i in range(n):
            if water<plants[i]:
                steps+=2*i
                water=capacity
            steps+=1
            water-=plants[i]
        return steps         

        