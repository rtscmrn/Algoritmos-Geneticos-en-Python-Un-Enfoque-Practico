print("Hellow world!")
print("Second line")
import random
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7])
print(a)

for i in a:
    print("================ item ", i)

def function1():
    print("function1")
    fruits = ["apple", "orange", "banana"]
    for i in fruits:
        print("fruit: ", i)

    greetings = "Greetings for me!"

    for i in greetings:
        print("greetings: ", i)

    print("Finish function1 ")

function1()

print("Finish!")