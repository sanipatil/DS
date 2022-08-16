class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        i=0
        count=0
        ele=None
        flag=False
        hand.sort()
        while i <= len(hand)-1:
            if hand[i] == -1:
                i += 1
                continue
            elif ele == None:
                flag = False
                ele = hand[i]
                count += 1
                hand[i] = -1
            else:
                if hand[i] == ele + 1:
                    ele = hand[i]
                    count += 1
                    hand[i] = -1
                    
            if count == groupSize:
                flag = True
                count = 0
                i = 0
                ele = None
            else:
                i += 1
        return flag