class SelectionSort:
    def __init__(self, array):
        self.__array = array
    
    def get_array(self):
        return self.__array
    
    def select_sort(self):
        size = len(self.__array)
        arr = self.__array
        for step in range(size):
            min_idx = step

            for i in range(step + 1, size):
            
                # to sort in descending order, change > to < in this line
                # select the minimum element in each loop
                if arr[i] < arr[min_idx]:
                    min_idx = i
            
            # put min at the correct position
            arr[step], arr[min_idx] = arr[min_idx], arr[step]
        
        return arr



        
        