class BubbleSort:
    def __init__(self, array):
        self.__array = array
    
    def get_array(self):
        return self.__array
    
    def bubble_sort(self):
        arr = self.__array
        
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    
        return arr
                    
