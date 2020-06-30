class ListMaiAnhVersion(object):

    def __init__(self):
        self.array = [None for x in range(10)]
        self.length = 0

    def get(self, index):
        """
        Method to get an element of the list at the given index

        :param index: The index to get the element from
        """
        if index < self.length:
            return self.array[index]
        else:
            "NOT ALLOWED"
    
    def set(self, index, ele):
        """
        Method to set an element at the given index
        """
        if index < self.length:
            self.array[index] = ele
            return True # đã set thành công 
        else:
            return "Not Allowed"

    def add(self, ele):
        """
        Add an element to the end of list 

        :para ele: the element to add
        """
        if self.length == len(self.array):
            new_array = self.array + [None for x in range(len(self.array))]
            self.array = new_array

        self.array[self.length] = ele # xem lại chỗ self.length
        self.length += 1 

        return self.length

    def remove(self):
        """ 
        Remove at the end
        """
        self.array[self.length - 1] = None
        self.length -= 1

        return self.length

    def add_at(self, index, ele):
        """
        Add an element to an index
        """
        if index >= self.length:
            return "Not Allowed"
        
        # Move elements to new space
        for i in range(self.length - 1, index - 1, -1):
            self.array[i+1] = self.array[i]

        # Add ele to the index
        self.set(index, ele)
        self.length += 1
        return self.length

    def remove_at(self, index):
        """
        Remove an element at a given index
        """
        if index >= self.length:
            return "Not Allowed"
        
        # Set the current element at index to None
        self.set(index, None)

        # Move everything up
        for i in range(index + 1, self.length):
            self.array[i - 1] = self.array[i]
        
        self.set(self.length - 1, None)
        self.length -= 1
        return self.length

if __name__ == "__main__":
    a_list = ListMaiAnhVersion()

    print(f"Length of the new list: {a_list.length}")

    a_list.add(444)

    print(f"The length should be 1 {a_list.length}")

    ele_at_0 = a_list.get(0)

    print(f"Expected result 444: ")

    ele_at_3 = a_list.get(3)

    print(f"Expected result ERROR: ")

    for i in range(11):
        a_list.add(i)

    print(f"Length of the new list: {a_list.length}")
    print(f"The length should be 1 {a_list.length}")
    ele_at_10 = a_list.get(10)

    print(f"Expected result 10: ")

    # Homework: kiểm tra những case nhỏ có thể xảy ra và phải code để không xảy ra những trường hợp đó
    # VD case 1: add_at khi array đã full 

    