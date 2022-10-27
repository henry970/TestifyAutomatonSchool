# Task 10

def invoke(cb):
    cb("Hello world")

hello = lambda : print("Hello world")
hello()

invoke(lambda x: print(x))