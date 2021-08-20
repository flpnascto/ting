class Queue:
    def __init__(self):
        self.__data = []
        self.__data_len = 0

    def __len__(self):
        return self.__data_len

    def enqueue(self, value):
        self.__data.insert(0, value)
        self.__data_len += 1

    def dequeue(self):
        if self.__data:
            self.__data_len -= 1
            return self.__data.pop()

    def search(self, index):
        # if self._data[index]:
        #     raise IndexError
        # else:
        return self.__data[len(self.__data) - index - 1]

    def __str__(self):
        return "Queue(" + ", ".join(str(x) for x in self.__data) + ")"
