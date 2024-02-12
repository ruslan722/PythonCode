class LinkedList:
    class Item:
        value = None
        next = None

        def init(self, value):
            self.value = value

    head: Item = None

    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            self.head.value = value
            return

        while current.next:
            current = current.next

        item = LinkedList.Item(value)
        current.next = item

    def append_by_index(self, value, index):
        current = self.head
        if index == 0:
            self.append_begin(value)
            return
        count = 0
        while current:
            if count == index - 1:
                new_item = LinkedList.Item(value)
                new_item.next = current.next
                current.next = new_item
                return
            current = current.next
            count += 1
    '''Метод всавляет значение по указанному индексу,
        оставшиеся элементы сдвигаются'''

    def len(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def remove_first(self):
        if self.head is None:
            raise ValueError("Cannot remove from an empty list")

        self.head = self.head.next

    def remove_last(self):
        if self.head is None:
            raise ValueError("Cannot remove from an empty list")

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next:
            current = current.next

        current.next = None

    def remove_at(self, index):
        if self.head is None:
            raise ValueError("Cannot remove from an empty list")

        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise ValueError("Index out of range")
            current = current.next

        if current.next is None:
            raise ValueError("Index out of range")

        current.next = current.next.next

    def remove_first_value(self, value):
        if self.head is None:
            raise ValueError("Cannot remove from an empty list")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

        raise ValueError("Value not found in list")

    def remove_last_value(self, value):
        if self.head is None:
            raise ValueError("Cannot remove from an empty list")

        if self.head.value == value:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.value == value and current.next.next is None:
                current.next = None
                return
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

        raise ValueError("Value not found in list")

my_list = LinkedList()

my_list.append_begin(4)
my_list.append_begin(5)
my_list.append_begin(6)
my_list.append_begin(7)
my_list.append_begin(8)
my_list.append_begin(9)
my_list.append_by_index(5, 5)
my_list.remove_first()
my_list.remove_last()
my_list.remove_at(4)
my_list.remove_first_value(7)
my_list.remove_last_value(5)
print(len(my_list))