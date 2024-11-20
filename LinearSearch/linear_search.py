from typing import Union

class LinearSearch:
    def __init__(self, array=[], target=None) -> None:
        """Initialize the LinearSearch instance.

        Args:
            array (list, optional): List of elements to search through. Defaults to an empty list.
            target (_type_, optional): Element to search for. Defaults to None.
        """
        self.__array = array  # Private attribute
        self.__target = target  # Private attribute

    def linear_search(self) -> Union[int, float]:
        """Performs a linear search on the private array attribute.

        Returns:
            Union[int, float]: Index of target in array if found, else -1.
        """
        for index, value in enumerate(self.__array):
            if value == self.__target:
                return index
        return -1

    def linear_search_recursive(self, index=0) -> Union[int, float]:
        """Performs a recursive linear search on the private array attribute.

        Args:
            index (int, optional): The current index to check. Defaults to 0.

        Returns:
            Union[int, float]: Index of target in array if found, else -1.
        """
        if index == len(self.__array):  # Fixed condition to compare with the length of array
            return -1

        if self.__array[index] == self.__target:
            return index

        return self.linear_search_recursive(index + 1)

    # Public methods to access private attributes, if needed
    def set_target(self, target) -> None:
        """Set the target for the search.

        Args:
            target (_type_): The target value to search for.
        """
        self.__target = target

    def get_target(self):
        """Get the current target value."""
        return self.__target

    def set_array(self, array) -> None:
        """Set the array for the search.

        Args:
            array (list): The array to search in.
        """
        self.__array = array

    def get_array(self):
        """Get the current array."""
        return self.__array
