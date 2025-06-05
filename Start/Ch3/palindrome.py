import string

def is_palindrome(teststr):
    teststr = remove_punctuation_and_spaces(teststr)
    reversestr = teststr[::-1]
    if (teststr == reversestr):
        return True
    return False

def remove_punctuation_and_spaces(inputString):
    inputString = str.lower(inputString)
    translator = str.maketrans('', '', string.punctuation + ' ')
    return inputString.translate(translator)

test_word1 = "Madam, I'm Adam."
# try using some of these other words:
test_word2 = "RACE CAR!"
test_word3 = "Hello, world"
test_word4 = "Radar?"
test_word5 = "A man, a plan, a canal Panama!"

# print(remove_punctuation_and_spaces(test_word2))
print(is_palindrome(test_word1))
print(is_palindrome(test_word2))
print(is_palindrome(test_word3))
print(is_palindrome(test_word4))
print(is_palindrome(test_word5))