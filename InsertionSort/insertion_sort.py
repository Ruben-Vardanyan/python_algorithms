class InsertionSort:
    def __init__(self, array):
        self.__array = array
        
    def get_array(self):
        return self.__array
    
    def infertion_sort(self):
        arr = self.__array
        
        for step in range(1, len(arr)):
            key = arr[step]
            j = step - 1
            
            while j >= 0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j = j - 1
            
            arr[j + 1] = key
        
        return arr



