class Solution:
    # def sortArray(self, arr: List[int]) -> List[int]:
    #     # Helper merge function
    #     def merge(arr, l, mid, r):
    #         temp = []
    #         i, j = l, mid + 1

    #         # Merge two sorted halves
    #         while i <= mid and j <= r:
    #             if arr[i] <= arr[j]:
    #                 temp.append(arr[i])
    #                 i += 1
    #             else:
    #                 temp.append(arr[j])
    #                 j += 1

    #         # Copy remaining elements
    #         while i <= mid:
    #             temp.append(arr[i])
    #             i += 1
    #         while j <= r:
    #             temp.append(arr[j])
    #             j += 1

    #         # Copy back to original array
    #         for i in range(len(temp)):
    #             arr[l + i] = temp[i]

    #     # Recursive merge sort
    #     def mergeSort(arr, l, r):
    #         # ✅ Base case: single element
    #         if l >= r:
    #             return

    #         mid = (l + r) // 2
    #         mergeSort(arr, l, mid)
    #         mergeSort(arr, mid + 1, r)
    #         merge(arr, l, mid, r)

    #     # Call helper
    #     mergeSort(arr, 0, len(arr) - 1)
    #     return arr      

    #Better to Understand
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

        