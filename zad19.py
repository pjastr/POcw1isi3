def foo():
    foo.counter += 1
    print(foo.counter)


foo.counter = 0
foo()
foo()
foo()
