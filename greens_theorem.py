
Green's Theorem Verification Program


This program verifies Green's Theorem for the vector field:
P(x, y) = -y
Q(x, y) = x

Region:
Unit square where x = 0 to 1 and y = 0 to 1

It calculates:
1. Line integral around the boundary
2. Double integral inside the region
and checks if both are equal.


import numpy as np


def P(x, y):
    return -y

def Q(x, y):
    return x



def line_integral(n=2000):
    total = 0

  
    t = np.linspace(0, 1, n)
    dx = 1/(n-1)
    dy = 0
    x = t
    y = 0
    total += np.trapz(P(x, y)*dx + Q(x, y)*dy, t)


    x = 1
    y = t
    dx = 0
    dy = 1/(n-1)
    total += np.trapz(P(x, y)*dx + Q(x, y)*dy, t)

  
    t2 = np.linspace(1, 0, n)
    x = t2
    y = 1
    dx = -1/(n-1)
    dy = 0
    total += np.trapz(P(x, y)*dx + Q(x, y)*dy, t2)

  
    x = 0
    y = t2
    dx = 0
    dy = -1/(n-1)
    total += np.trapz(P(x, y)*dx + Q(x, y)*dy, t2)

    return total



def double_integral():
  
    value = 2

    area = 1 
    return value * area



if __name__ == "__main__":
    L = line_integral()
    D = double_integral()

    print("Line Integral Result:   ", L)
    print("Double Integral Result: ", D)
    print("Difference:             ", abs(L - D))
