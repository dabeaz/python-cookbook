import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self

if __name__ == '__main__':
    root = Node('parent')
    c1 = Node('c1')
    c2 = Node('c2')
    root.add_child(c1)
    root.add_child(c2)

    print(c1.parent)
    del root
    print(c1.parent)
    
