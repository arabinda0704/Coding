class Solution:
    def merge(self,arr1,arr2):
        merged=[]
        i,j=0,0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                merged.append(arr1[i])
                i+=1
            else:
                merged.append(arr2[j])
                j+=1
        # Add remaining elements (if any)
        # merged.extend(left[i:])
        # merged.extend(right[j:])
        while i<len(arr1):
            merged.append(arr1[i])
            i+=1
        while j<len(arr2):
            merged.append(arr2[j])
            j+=1
        return merged
    
    def sortArray(self, arr: List[int]) -> List[int]:

        # Merge Sort
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = self.sortArray(arr[:mid])
        right = self.sortArray(arr[mid:])

        # return self.merge(left, right)
        # less space
        i,j,k=0,0,0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        # Add remaining elements (if any)
        # merged.extend(left[i:])
        # merged.extend(right[j:])
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1
        return arr
        

        