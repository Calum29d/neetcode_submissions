class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, l, m ,r):
            leftArr, rightArr = arr[l:m+1], arr[m+1:r+1]
            i, j, k = l, 0, 0 # i -> arr ptr, j -> left arr ptr, k -> right arr ptr

            while j < len(leftArr) and k < len(rightArr):
                if leftArr[j] <= rightArr[k]:
                    arr[i] = leftArr[j]
                    j += 1
                else:
                    arr[i] = rightArr[k]
                    k += 1
                i += 1
            
            while j < len(leftArr):
                arr[i] = leftArr[j]
                j += 1
                i += 1
                
            while j < len(leftArr):
                arr[j] = leftArr[k]
                k += 1
                i += 1

        def mergeSort(arr, l, r):
            if l == r: # if the size of the array is now 1
                return
            
            m = (l + r) // 2
            mergeSort(arr, l, m)
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)

        mergeSort(nums, 0, len(nums) - 1)
        return nums