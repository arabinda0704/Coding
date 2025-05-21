class Solution:
    def minDays(self, arr: List[int], m: int, k: int) -> int:
        val = m * k
        n = len(arr)  # size of the array
        if val > n:
            return -1  # impossible case
        
        mini = min(arr)
        maxi = max(arr)

        low = mini
        high = maxi
        res=0
        while low<=high:
            mid=low+(high-low)//2
            cnt=0
            noOfB=0
            for i in range(n):
                if arr[i]<=mid:
                    cnt+=1
                else:
                    noOfB+=cnt//k
                    cnt=0
            noOfB+=cnt//k  
            if noOfB>=m:
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res


        