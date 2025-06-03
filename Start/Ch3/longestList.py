test_strings = [
    "Hello World!",
    "And how can this be? For he is the Kwisatz Haderach!",
    "Four score and seven years ago",
    "Life moves pretty fast. If you don’t stop and look around once in a while, you could miss it."
]

def find_largest(test_strings):
  largestString = 0
  for i in test_strings:
    if (len(i) > largestString):
        largestString = len(i)
  return largestString

print(find_largest(test_strings))
# print(len(test_strings[3]))