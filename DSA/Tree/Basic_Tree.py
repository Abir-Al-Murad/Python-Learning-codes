class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
    def add_child(self,Child): 
        Child.parent = self
        self.children.append(Child)
root = TreeNode('Taslima')
daughter1 = TreeNode('Tajakka')
root.add_child(daughter1)