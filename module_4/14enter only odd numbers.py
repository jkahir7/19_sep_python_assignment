#Write python program that user to enter only odd numbers, else will raise an exception.
def odd_num():
    while True:
        try:
            num = int(input("enter a number : "))
            if num % 2 == 0:
                raise ValueError("invalid input")
            return num
        except ValueError as e:
            print(e)

obj = odd_num()
print("odd number is : ",obj)