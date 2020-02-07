class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is greater than current node
        if value < self.value:
            # no node to the left then add a new node / tree
            if not self.left:
                self.left = BinarySearchTree(value)
            else: 
                self.left.insert(value)
          
        else:
            if not self.right:
                self.right = BinarySearchTree(value)
            # else insert value
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target): 
        if target == self.value:
            return True
        elif target > self.value:
            if not self.left:
                return False 
            else:
                self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                self.right.contains(target)
            
               