from myData import doctor


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if self.left is None:
                self.left = Node(data)
            elif self.right is None:
                self.right = Node(data)
            else:
                if self.left.left is None or self.right.right is None:
                    self.left.insert(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        print(self.data)
        if self.left:
            self.left.printTree()

        if self.right:
            self.right.printTree()
