def add_numbers(lst):
    return sum(lst)

def mul_numbers(lst):
    mul = 1
    for i in lst:
        mul *= i

    return mul

def divide(num1, num2):
    return num1/num2

if __name__ == '__main__':

    lst = [i for i in range(101)]
    print(add_numbers(lst))

