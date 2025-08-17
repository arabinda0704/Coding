class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qr=[]
        qd=[]
        for i in range(len(senate)):
            if senate[i]=="R":
                qr.append(i)
            else:
                qd.append(i)
        n=len(senate)
        while qr and qd:
            r=qr.pop(0)
            d=qd.pop(0)
            if r<d:
                qr.append(r+n)
            else:
                qd.append(d+n)
        if not qr:
            return "Dire"
        if not qd:
            return "Radiant"
            

        