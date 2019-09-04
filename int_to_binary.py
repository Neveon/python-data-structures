# divide integer by 2 keeping the remainder until int = 0
# the remainders give us the binary

from stack import Stack

def int_to_binary(num):
  num = int(num)
  binary = Stack()

  # edge case for 0
  if num == 0:
    return '0'

  while num > 0:
    if num//2 == num/2:
      binary.push('0')
    else:
      binary.push('1')
    
    num = num//2

  
  return binary.items

integer = 2
print(int_to_binary(integer))
integer = 17
print(int_to_binary(integer))