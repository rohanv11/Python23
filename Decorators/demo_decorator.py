def f1(a):
    def f2(b):
        return a + b
    return f2


f2_obj = f1(10)
print(f2_obj(14))