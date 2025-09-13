class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], kings: List[int]) -> List[List[int]]:
        res=[]
        # left->right
        l,r=kings[0],kings[1]+1
        while r<8:
            if [l,r] in queens:
                res.append([l,r])
                break
            r+=1
        # right->left
        l,r=kings[0],kings[1]-1
        while r>=0:
            if [l,r] in queens:
                res.append([l,r])
                break
            r-=1
        # up->down
        l,r=kings[0]+1,kings[1]
        while l<8:
            if [l,r] in queens:
                res.append([l,r])
                break
            l+=1
        # down->up
        l,r=kings[0]-1,kings[1]
        while l>=0:
            if [l,r] in queens:
                res.append([l,r])
                break
            l-=1

        #Diagonal

        # up-right
        l,r=kings[0]-1,kings[1]+1
        while l>=0 and r<8:
            if [l,r] in queens:
                res.append([l,r])
                break
            l-=1
            r+=1
        # Up-left
        l,r=kings[0]-1,kings[1]-1
        while l>=0 and r>=0:
            if [l,r] in queens:
                res.append([l,r])
                break
            l-=1
            r-=1
        # down-right
        l,r=kings[0]+1,kings[1]+1
        while l<8 and r<8:
            if [l,r] in queens:
                res.append([l,r])
                break
            l+=1
            r+=1
        # down-left
        l,r=kings[0]+1,kings[1]-1
        while l<8 and r>=0:
            if [l,r] in queens:
                res.append([l,r])
                break
            l+=1
            r-=1
        return res
        