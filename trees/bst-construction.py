class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Avg: O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None: 
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    # Avg: O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space
    def contains(self, value):
        if value < self.value: 
            if self.left is None: 
                return False
            else: 
                return self.left.contains(value)
        elif value > self.value:
            if self.right is None: 
                return False
            else: 
                return self.right.contains(value)
        else: 
            return True
   
    # Avg: O(log(n)) Time | O(log(n)) Space
    # Worst: O(n) Time | O(n) Space         
    def remove(self, value, parent=None):
        if value < self.value:
            if self.left is not None:
                self.left.remove(value, self)
        elif value > self.value: 
            if self.right is not None: 
                self.right.remove(value, self)
        else: 
            if self.left is not None and self.right is not None: 
                self.value = self.right.getMinValue()
                self.right.remove(self.value, self)
            elif parent is None: 
                if self.left is not None: 
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    # This is a single-node tree; do nothing.
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right == self:
                parent.right = self.left if self.left is not None else self.right
        return self
    
    def getMinValue(self):
        if self.left is None:
            return self.value
        else: 
            return self.left.getMinValue()

def main():
    root = BST(10)
    root.left = BST(5)
    root.right = BST(15)
    root.left.left = BST(2)
    root.left.right = BST(5)
    root.right.left = BST(13)
    root.right.right = BST(22)
    root.left.left.left = BST(1)
    root.right.left.right = BST(14)
    print(root.insert(12).right.left.left.value)
    print(root.remove(10).value)
    print(root.contains(15))
    
if __name__ == "__main__":
    main()