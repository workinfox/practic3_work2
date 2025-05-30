def Hello():
    print("Hello, it's my repozitory for practic")

def sum_number(num1, num2):
    result = num1 + num2
    print(f"Sum: {num1} and {num2} equal to {result}")
    return result

def main():
    Hello()
    sum_number(25, 5)

if __name__ == '__main__':
    main()
