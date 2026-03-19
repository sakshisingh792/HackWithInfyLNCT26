class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_ten=0
        change_five=0
        
        for bill in bills:
            if bill==5:
                change_five+=1
            elif bill==10:
                if change_five>0:
                    change_five-=1
                    change_ten+=1
                else:
                    return False    
            else:
                if change_ten>0 and change_five>0:
                    change_ten-=1
                    change_five-=1
                elif change_five>=3:
                    change_five-=3
                else:
                    return False
        return True                                


        