def isPalindrome(self, x: int) -> bool:
    number_str = str(x)
    palindrome = number_str[::-1]

    return True if number_str == palindrome else False