class Stack():
  def __init__(self):
    self.items = []

  def push(self, item):
    self.items.append(item)

  def pop(self):
    return self.items.pop()

  def is_empty(self):
    if self.items == []:
      return True
    else:
      return False

  def get_stack(self):
    return self.items