# TODO: Find all one digit to 10 digit numbers for which abcd * 4 = dcba

def pallindrome_numbers():
    for number in range (1000,10000):
        reverse_num= int(str(number)[::-1])
        if number*4 == reverse_num:
            return number

ans= pallindrome_numbers()
print(ans)