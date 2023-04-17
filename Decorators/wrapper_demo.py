def func1():
    print("Start func1")
    def wrapper():
        print("Inside wrapper")
        return 11
    print("End func1")
    return wrapper


print(func1())
print(func1()())