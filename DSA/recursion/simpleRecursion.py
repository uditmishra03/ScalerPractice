def bar(x, y):
    if y == 0:
        return 0
    return (x+bar(x, y-1))

def foo(x, y):
    if y == 0:
        return 1
    return bar(x, foo(x, y-1))

print(foo(3, 5))