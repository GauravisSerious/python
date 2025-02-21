def heapify_up(self):
        current_index = len(self.heap)-1
        while current_index > 0:
            parent_index  = self._get_parent_index(current_index)
            if self.heap[current_index]> self.heap[parent_index]:
                self.swap(current_index,parent_index)
                current_index = parent_index
            else:
                break
