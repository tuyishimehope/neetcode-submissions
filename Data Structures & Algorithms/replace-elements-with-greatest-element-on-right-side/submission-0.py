class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length = len(arr)

        if length < 1:
            return []
        
        ans = [0]  * length

        for i, num in enumerate(arr):
            if i == length - 1:
                ans[i]= -1
                return ans
            
            new_arr = arr[i + 1:]
            for index, el in enumerate(new_arr):
                if index == length - 1:
                    continue

                largest = new_arr[index]
                if largest > ans[i]:
                    ans[i] = largest


                
        