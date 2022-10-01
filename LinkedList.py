class Node(object):

    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

    def set_val(self, val):
        self.val = val

    def get_val(self):
        return self.val

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class LinkedList(object):

    def __init__(self, head=None) -> None:
        self.head = head
        self.count = 0

    def insert(self, data):
        # create a new node to hold the data
        new_node = Node(data)

        # set the next of the new node to the current head
        # set the head of the Linked List to the new head
        new_node.set_next(self.head)
        self.head = new_node

        # add 1 to the count
        self.count += 1

    def find(self, val):
        item = self.head

        while item != None:
            if item.get_val() == val:
                return item
            else:
                item = item.get_next()

        return None

    def remove(self, val):
        # set the current node starting with the head
        current = self.head
        # create a previous node to hold the one before
        # the node we want to remove
        previous = None

        # while current is note None then we can search for it
        while current is not None:
            if current.val == val:
                if current is None:
                    raise ValueError(f"{val} is not in the list")
                # if previous None then the val is at the head
                elif previous is None:
                    self.head = current.next
                    self.count -= 1
                # otherwise then we remove that node from the list
                else:
                    previous.set_next(current.get_next())
                    self.count -= 1

            # otherwise we set previous to current and
            # current to the next val in list
            previous = current
            current = current.get_next()

    def get_count(self):
        return self.count

    def is_empty(self):
        return self.head == None
