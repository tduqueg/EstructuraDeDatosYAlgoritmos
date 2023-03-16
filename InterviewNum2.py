def palindrome(s):
    if s == s[::-1]:
        return True
    return False

if __name__ == '__main__':
    print(palindrome("eene"))