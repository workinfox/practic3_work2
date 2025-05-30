def Hello():
    print("Hello, it's my repozitory for practic")


def subtr(num3, num4):
    result = num3 - num4
    print(f"Subtraction {num3} and {num4} equal to: {result}")

def sum_number(num1, num2):
    result = num1 + num2
    print(f"Sum: {num1} and {num2} equal to {result}")
    return result

def End():
    print("Bye-bye, I'm finally done with this")

def main():
    Hello()
    subtr(30, 5)
    sum_number(25, 5)
    End()


if __name__ == '__main__':
    main()
