class Queue:
    def __init__(self):
        self._data = []
        self._data_len = 0

    def __len__(self):
        return self._data_len

    def enqueue(self, value):
        self._data.insert(0, value)
        self._data_len += 1

    def dequeue(self):
        if self._data:
            self._data_len -= 1
            return self._data.pop()

    def search(self, index):
        # if self._data[index]:
        #     raise IndexError
        # else:
        return self._data[len(self._data) - index - 1]

    def __str__(self):
        return "Queue(" + ", ".join(str(x) for x in self._data) + ")"
