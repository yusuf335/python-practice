def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers

    Although this function is intended to multiply 2 numbers,
    you can also use it to multiply a sequence.  If you pass
    a string, for example, as the first argument, you'll get
    the string repeated `y` times as the returned value.

    :param x: The first number to multiply.
    :param y: The number to multiply `x` by.
    :return: The productt of `x` and `y`.
    """
    result = x * y
    return result


def is_palindrome(string: str) -> bool:
    # backward = string[:: -1]
    # return  backward == string
    return string[:: -1].casefold() == string.casefold()

def plindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    print(string)
    # return string[:: -1].casefold() == string.casefold()
    return is_palindrome(string)

def fibonacci(n: int) -> int :
    """Return the `n` th Fibonacci number, for positive `n`."""
    if 0 <= n <= 1:
        return n
    n_minus1, n_minus2 = 1, 0

    result = None
    for f in range(n-1):
        result = n_minus2 + n_minus1
        n_minus2 = n_minus1
        n_minus1 = result

    return result


for i in range(36):
    print(i, fibonacci(i))

p = multiply()
# word = input("Please enter a word to check: ")
# if plindrome_sentence(word):
#     print("'{}' is a palindrome".format(word))
# else:
#     print("'{}' is not a palindrome".format(word))

# answer = multiply(18, 3)
# print(answer)

# answer = multiply(10.5, 4)
# print(answer)
#
#
# forty_two = multiply(6, 7)
# print(forty_two)
#

# print()
#
# for val in range(1,5):
#     two_times = multiply(2, val)
#     print(two_times)