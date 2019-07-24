class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value:
      if not self.left:
        self.left = BinarySearchTree(value)
      else:
        #recursive to keep going until we find an empty spot
        self.left.insert(value)
    else:
      if not self.right:
        self.right = BinarySearchTree(value)
      else:
        self.right.insert(value)

  def contains(self, target):
    #base case no value or value is the root
    if self.value is None or self.value == target:
      return True
    
    if self.value < target and self.right:
      return self.right.contains(target)
      
    elif self.value < target and self.left:
      return self.left.contains(target)
    
    else:
      return False

  def get_max(self):
    pass

  def for_each(self, cb):
    pass