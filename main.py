

class MultilinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = []

class MultilinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = MultilinkedNode(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            current.next.append(new_node)


multilinked_list = MultilinkedList()
multilinked_list.add_node("Node 1")
multilinked_list.add_node("Node 2")
multilinked_list.add_node("Node 3")
print(multilinked_list.head.data)

for i in multilinked_list.head.next:
    print(i.data)