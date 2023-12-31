# -*- coding: utf-8 -*-
"""Copy of Lab_Assignment_02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1CEeYJ5blQpBJiIVNdTt1NRUQYeOhZTKN

<a href="https://colab.research.google.com/github/mirsazzathossain/CSE317-Lab/blob/main/Lab_Assignment_02.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

#### **Find the following integral using the simpson's 1/3 rule**

Simpson's 1/3 rule uses higher-order polynomials to approximate the integral of a function $f(x)$ over the interval $[a,b]$. For Example, if there is an extra point midway between $f(a)$ and $f(b)$, the three points can be connected with a parabola. The area under the parabola is an approximation of the integral of $f(x)$ over the interval $[a,b]$.

<center>
    <img src="https://github.com/mirsazzathossain/CSE317-Lab/blob/main/images/simpson.PNG?raw=1" width="400" />
</center>

If we are given values of $f(x)$ at 3 points as $(x_0, f(x_0))$, $(x_1, f(x_1))$, and $(x_2, f(x_2))$ then we can estimate $f(x)$ using the Lagrange polynomial of degree 2:

$$
\begin{align*}
f(x) &\approx f(x_0) \frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)} + f(x_1) \frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)} + f(x_2) \frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)}
\end{align*}
$$

Now, as the area under the estimated curve is an approximation of the integral of $f(x)$ over the interval $[a,b]$, we can write the integral as:

$$
\begin{align*}
I &= \int_{a}^{b} f(x) dx \\
&\approx \int_{a}^{b} \left[f(x_0)\frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)} + f(x_1) \frac{(x-x_0)(x-x_2)}{(x_1-x_0)(x_1-x_2)} + f(x_2) \frac{(x-x_0)(x-x_1)}{(x_2-x_0)(x_2-x_1)} \right] dx
\end{align*}
$$

When $a = x_0$, $b = x_2$, $x_1 = \frac{a+b}{2}$, and $h = \frac{b-a}{2}$, we can simplify the integral to:

$$
\begin{align*}
    I &\approx \frac{h}{3} \left[ f(x_0) + 4f(x_1) + f(x_2) \right] \\
    &= (b-a) \frac{f(x_0) + 4f(x_1) + f(x_2)}{6}
\end{align*}
$$

We will use Simpson's 1/3 rule to approximate the integral of $f(x) = 0.2 + 25x - 200x^2 + 675x^3 - 900x^4 + 400x^5$ over the interval $[0, 0.8]$. Follow the steps below to approximate the integral using Simpson's 1/3 rule.

#** Maha Murshed 2030385**

##### **Step 1: Define the function**

Define a function `f` that takes a single parameter `x` and returns the value of $f(x) = 0.2 + 25x - 200x^2 + 675x^3 - 900x^4 + 400x^5$ at `x`. Note that the function should be able to handle both scalar and vector inputs.
"""

# Write appropriate code
import numpy as np
import matplotlib.pyplot as plt
import math
def f(x):
  return 0.2 + 25*x - 200*pow(x,2) + 675*pow(x,3)-900*pow(x,4)+400*pow(x,5)

"""##### **Step 2: Define a function to approximate the function $f(x)$ using Lagrange polynomial**

Define a function `lagrange` that takes four parameters `x0`, `x1`, `x2` and `x` and returns the value of the Lagrange polynomial of degree 2 at `x`. The function should be able to handle both scalar and vector inputs. Use the function `f` defined in Step 1 to evaluate the function at the given points.
"""

# write appropriate code
def lagrange(x0,x1,x2,x):
   return  ((f(x0)*(x-x1)*(x-x2))/((x0-x1)*(x0-x2))) + ((f(x1)*(x-x0)*(x-x2))/((x1-x0)*(x1-x2))) + ((f(x2)*(x-x0)*(x-x1))/((x2-x0)*(x2-x1)))

"""##### **Step 3: Define the interval**
Define the interval as a numpy array of two elements, where the first element is the lower bound and the second element is the upper bound. Name the array `interval`.
"""

# Write appropriate code
interval = np.array([0,0.8])

"""##### **Step 4: Plot the function and the approximated polynomial**

Plot the function $f(x)$ and the approximated polynomial using the function `lagrange` defined in Step 2. Use the interval defined in Step 3 as the x-axis. Also, plot the points $(x_0, f(x_0))$, $(x_1, f(x_1))$, and $(x_2, f(x_2))$ on the same plot. Fill the area under the approximated polynomial using numpy's `fill_between` function.
"""

x = np.linspace(interval[0], interval[1], 100)
lag = np.linspace(interval[0],interval[1], 3)

plt.xlabel('x')
plt.ylabel('f(x)')

plt.plot(x,f(x))
plt.plot(x,lagrange(lag[0],lag[1],lag[2],x))

plt.plot(lag[0],f(lag[0]), marker="x")
plt.plot(lag[1],f(lag[1]), marker="x")
plt.plot(lag[2],f(lag[2]), marker="x")

plt.fill_between(x,lagrange(lag[0],lag[1],lag[2],x), color='blue', alpha=.3, facecolor="none", hatch="//", edgecolor="blue", linewidth=2.0)
plt.grid()
plt.show()

"""##### **Step 5: Define a function to approximate the integral using Simpson's 1/3 rule**

Define a function `simpson` that takes a parameter `interval` and returns the approximate value of the integral of $f(x)$ over the interval `interval` using Simpson's 1/3 rule. You have to employ the following steps:

*   Calculate the midpoint of the interval. Store the value in a variable named `midpoint`.
*   Calculate the value of $f(x_0)$, $f(x_1)$, and $f(x_2)$, where $x_0 = a$, $x_1 = \frac{a+b}{2} = midpoint$, and $x_2 = b$. Store the values in variables named `f0`, `f1`, and `f2` respectively.
*   Calculate the approximate value of the integral using Simpson's 1/3 rule. Store the value in a variable named `I`.
*   Return the value of `I`.
"""

# Write appropriate code
def simpson(interval):
  midpoint = x1 = (interval[0]+interval[1])/2
  x0 = interval[0]
  x2 = interval[1]

  f0 = f(x0)
  f1 = f(x1)
  f2 = f(x2)
  I = ((interval[1]- interval[0])*(f(x0)+(4*f(x1))+f(x2)))/6
  return I

"""##### **Step 6: Approximate the integral using Simpson's 1/3 rule**

Call the function `simpson` with the interval `interval` as the parameter. Store the value returned by the function in a variable named `I`. Print the value of `I`. Then you should compute the integral analytically and find the absolute relative error between the two values. Print the absolute relative error.
"""

# Write appropriate code
I = simpson(interval)
print(round(I,2))
Calc = 1.640533
are = ((Calc - I)/Calc) *100

print("Absolute relative error is : ",round(are,2))