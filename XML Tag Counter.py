"""Write a function, `tag_count`, that takes as its argument a list
of strings. It should return a count of how many of those strings
are XML tags. You can tell if a string is an XML tag if it begins
with a left angle bracket "<" and ends with a right angle bracket ">".
"""
#TODO: Define the tag_count function

def tag_count(list1):
  sum = 0
  for count in list1:
    if (count[0] == '<' and count[-1] == '>'):
      sum += 1
  return sum

# Test for the tag_count function:
list1 = ['<greeting>', 'Hello World!', '</greeting>']
count = tag_count(list1)
print("Expected result: 2, Actual result: {}".format(count))
