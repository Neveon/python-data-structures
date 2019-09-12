from stack import Stack

str_to_reverse = 'Hello World'

def recursive_reverse(string_to_reverse, reversed_string = Stack()):

  # check if string submitted contains no characters
  if len(string_to_reverse) == 0:
    return reversed_string.items

  # pushing last element
  reversed_string.push(string_to_reverse[-1])

  # submitting string without last character
  return recursive_reverse(string_to_reverse[:-1])

print(recursive_reverse(str_to_reverse))