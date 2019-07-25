class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def delete(self):
        max_del = self.storage[0]
        self.storage[0] = self.storage[len(self.storage) - 1]
        self.storage.pop()
        self._sift_down(0)
        return max_del

    def get_max(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        while index > 0:
            # compare to parent
            parent = (index - 1) // 2  # double divide handles the rounding

            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]

                index = parent

            else:
                break

    def _sift_down(self, index):
        end = len(self.storage) - 1
        child = index * 2 + 1
        while child <= end:
            right_child = child + 1
            if right_child <= end and self.storage[child] < self.storage[right_child]:
                child = right_child
            if self.storage[index] < self.storage[child]:
                self.storage[index], self.storage[child] = self.storage[child], self.storage[index]
                index = child
                child = index * 2 + 1
            else:
                break
