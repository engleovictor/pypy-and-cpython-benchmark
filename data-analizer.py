import matplotlib.pyplot as plt
import numpy as np

data = open("./data.txt", 'r').read().splitlines()

fibonacci_values = [5,10,15,20,25,30,35,40]

python_iterative_fibonacci = [float(data[i]) for i in range(0,16,2)]
python_recursive_fibonacci = [np.log(float(data[i])) for i in range(1,16,2)]

pypy_iterative_fibonacci = [float(data[i]) for i in range(16,32,2)]
pypy_recursive_fibonacci = [np.log(float(data[i])) for i in range(17,32,2)]

plt.plot(fibonacci_values,python_iterative_fibonacci,color="r",label="Python Iterative Fibonacci")
plt.plot(fibonacci_values,pypy_iterative_fibonacci,color="b",label="PyPy Iterative Fibonacci")
plt.legend(['CPython', 'PyPy'], loc=9)
plt.grid()
plt.show()

plt.plot(fibonacci_values,python_recursive_fibonacci,color="r",label="Python Recursive Fibonacci")
plt.plot(fibonacci_values,pypy_recursive_fibonacci,color="b",label="PyPy Recursive Fibonacci")
plt.legend(['CPython', 'PyPy'], loc=9)
plt.grid()
plt.show()