def my_func1(x: int, y: int) -> float:
    for i in range(2):
        x *= y
    return print(x)
x = 2
y = -3
my_func2 = lambda x, y: x ** y
print(my_func2(x, y))
print(my_func2(x, y))
