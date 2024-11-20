class BinarySearch:
    __indexed_array = []
    
    def __init__(self, array=[], target=None) -> None:
        self.__array = array
        self.__target = target
        
        self.__indexed_array = list(enumerate(self.__array))
        self.__indexed_array.sort(key=lambda x: x[1])

    def get_array(self):
        return self.__array

    def set_array(self, array):
        self.__array = array

    def get_target(self):
        return self.__target

    def set_target(self, target):
        self.__target = target

    def binary_search(self):
        

        low = 0
        upper = len(self.__indexed_array) - 1

        while low <= upper:
            mid = (low + upper) // 2
            mid_value = self.__indexed_array[mid][1]

            if self.__target > mid_value:
                low = mid + 1
            elif self.__target < mid_value:
                upper = mid - 1
            else:
                return self.__indexed_array[mid][0]

        return -1
    def binary_search_recursive(self, low=0, upper=None):
        if upper == None:
            upper = len(self.__indexed_array) - 1

        if low <= upper:
            mid = (low + upper) // 2
            mid_value = self.__indexed_array[mid][1]

            if self.__target > mid_value:
                return self.binary_search_recursive(low + 1, upper)
            elif self.__target < mid_value:
                return self.binary_search_recursive(low, upper - 1)
            else:
                return self.__indexed_array[mid][0]
        return -1
    
        


