def reverse(num):

    reversed =0
    remainder = 0

    while num > 0:
        remainder = num%10
        reversed = reversed*10 + remainder
        num //= 10
    return reversed
    

if __name__ == '__main__':
    print(reverse(45632))