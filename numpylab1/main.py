import math
import numpy as np
import matplotlib.pyplot as plt
import scipy as sci
from scipy import optimize
from scipy import ndimage as ndi
from mpl_toolkits.mplot3d import Axes3D

'''
# skapa array från lista
np.array([1, 2, 3])
# start-end-step
np.arange(0, 10, 0.1)
# bara nollor
np.zeros(4)

my_array = np.arange(0, 2, 0.1)
print(my_array)

my_array = np.ones(4) * math.pi
print(my_array)

a1 = np.array([0, 1, 2])
a2 = np.array([4, 5, 6])
a3 = np.array(a1.tolist() + a2.tolist())
print(a3)

# det går att loopa en array som en lista
a4 = np.array([1, 2, 3, 4])
for x in a4:
    print(x)

# debug guide
# form: print(arr2.shape)
# datatyp: print(arr2.dtype)
# storlek: print(arr2.size)
# antal dimensioner: print(arr2.ndim)
# delmatris/sub-matrix: print(arr2[0:3, 0:2])

A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 1], [1, 1]])
c = np.array([1, 2])

print(A * B)
print(A * c)
# matrismultiplikation
print(A @ B)
print(A @ c)


# kryssprodukt: np.cross
def my_f1(x):
    return x * x * np.sin(x)


x = np.arange(-4, 4, 0.1)
y = my_f1(x)

# plotta med matlib
plt.plot(x, y)
# plt.show()
'''

# Uppgift 1
'''
a = np.array([1, 2, 3, 4, 5])
print('a', a)
b = np.arange(0, sci.pi, 0.1)
print('b', b)
c = np.arange(1, 7, 1)
c.reshape(3, 2)
print('c', c)
d = np.array(a.tolist() + [6, 7])
print('d', d)

e_list = a.tolist()
for i in range(-1, -6, -1):
    e_list.append(i)
    print(i)
e = np.array(e_list)
e = e.reshape(2, 5)
print(e)

f = np.sin(b)
print(f)
'''

# Uppgift 2
'''
def function_a(x):
    return x ** 2


def function_b1(x):
    return x ** 2


def function_b2(x):
    return x @ x


def function_c1(x):
    return x ** 2


def function_c2(x):
    return x @ x


'''
# Uppgift 3
'''
def f(x):
    return 1+x+(4/(x-2)**2)


x = np.linspace(-10, 10)
plt.plot(x, f(x), color="red")
plt.show()

'''
# Uppgift 4
'''
def f_prim(x, y, der):
    dx = x[1] - x[0]
    dydx = np.gradient(y, dx)
    plt.plot(x, der)
    plt.plot(x, dydx)
    plt.show()


# x mellan -10 och 10 och det finns 1000 punkter.
x = np.linspace(-10, 10, 1000)
y = 1 + np.sin(x) + 0.5 * np.cos(4 * x)
der = np.cos(x) - 2 * np.sin(4 * x)
plt.plot(x, f_prim(x, y, der), color="blue")
plt.show()
'''

# Uppgift 5
'''
def riemann_func_1(x):
    y = x / ((x ** 2 + 4) ** (1 / 3))
    return y


def riemann_func_2(x):
    y = np.sqrt(x) * np.ln(x)
    return y


def riemann_sum(under_lim, over_lim, step):
    integral = 0.0
    prev_x = 0.0
    for x in np.linspace(under_lim, over_lim, step, endpoint=True):
        integral += riemann_func_1(x) * (x - prev_x)
        prev_x = x
    return integral


print('A', riemann_sum(0, 2, 1000))

integral = 0.0
prev_x = 0.0
for x in np.linspace(1, 4, 30, endpoint=True):
    integral = integral + (riemann_func_1(x) * (x - prev_x))
    prev_x = x

print('B', integral)
'''

# Uppgift 6
'''
def q(t, A, B):
    return np.e ** -t * (A * np.cos(t) + B * np.sin(t)) + np.cos(t) + 2 * np.sin(t)


t = np.linspace(0, 10)
for A in range(-4, 5):
    for B in range(-4, 5):
        plt.plot(t, q(t, A, B))
plt.show()

'''

# Uppgift 7
'''
def taylor_sin(x):
    return ((-1)**i * x**(2*i+1)) / np.math.factorial(2*i+1)


x = np.linspace(-10, 10, 500)
y = np.zeros(len(x))

for i in range(13):
    y = y + taylor_sin(x)
plt.plot(x, y)
plt.plot(x, np.sin(x))
plt.show()

'''
# Uppgift 8 a
'''

x = np.linspace(-5, 5)
y = x - np.cos(x)


# plt.plot(x, y)
# plt.show()


# Uppgift 8 b
def func(x):
    return x - np.cos(x)


def bisection_algorithm(a, b):
    n = 0

    # first c is a constant, the half between delta(ab)
    y_a = func(a)
    y_b = func(b)
    # felhantering
    if y_a > 0 or y_b < 0:
        return "välj värden på a och b som uppfyller villkoren!"

    while abs(a - b) > 10 ** -12:
        # counter
        n += 1

        c = (b + a) / 2.0
        y_c = func(c)

        e = abs(a - b)

        if y_c < 0:
            a = c
        else:
            b = c
    return 'y för x = cos(x) är: ' + str(c) + '. Antal körningar: ' + str(n) + '. Felmarginal : ' + str(e)


print('bisection:', bisection_algorithm(-2.5, 2.5))


# Uppgift 8 c
def func_prim(x):
    return 1 + np.sin(x)


# reset counter
counter = 0


def newton_raphson_algorithm(a):
    # counter
    n = 0

    xn_plus1 = 0
    xn = a
    while abs(xn_plus1 - xn) > 10 ** -12:
        xn = xn_plus1
        xn_plus1 = xn - (func(xn) / func_prim(xn))
        n += 1
        e = abs(xn_plus1 - xn)
    return 'y för x = cos(x) är: ' + str(xn) + '. Antal körningar: ' + str(n) + '. Felmarginal: ' + str(e)


print('Newton Raphson:', newton_raphson_algorithm(-2.5))
'''
# Uppgift 9
'''
Argument	    Description
xs, ys	x, y    coordinates of vertices
zs	z           value(s),either one for all points or one for each point.
zdir	        Which direction to use as z (‘x’, ‘y’ or ‘z’) when plotting a 2D set.

'''

'''
# Kon
def cone():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    r = np.linspace(0, 1, 50)
    p = np.linspace(0, 2 * np.pi, 50)
    R, P = np.meshgrid(r, p)
    Z = R

    X, Y = R * np.cos(P), R * np.sin(P)

    ax.plot_surface(X, Y, -Z+1)

    ax.set_zlim(0, 1)
    ax.set_xlabel(r'x')
    ax.set_ylabel(r'y')
    ax.set_zlabel(r'z')

    plt.show()


cone()


# Pyramid
def pyramid():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(y, x)
    Z = np.abs(X) + np.abs(Y) - 5
    Z[Z>0] = None

    ax.plot_surface(X, Y, -Z, cmap='Blues_r')

    ax.set_zlim(0, 5)
    ax.set_xlabel(r'x')
    ax.set_ylabel(r'y')
    ax.set_zlabel(r'z')

    # fig.add_subplot(projection=ax)
    plt.show()


pyramid()


# En halvsfär
def half_sphere():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    r = 1
    p = np.linspace(0, 2 * np.pi, 50)
    phi = np.linspace(0, np.pi / 2, 50)
    P, PHI = np.meshgrid(p, phi)
    Z = r*np.cos(PHI)

    X, Y = r*np.cos(P)*np.sin(PHI), r*np.sin(P)*np.sin(PHI)

    ax.plot_surface(X, Y, Z)

    ax.set_zlim(0, 1)
    ax.set_xlabel(r'x')
    ax.set_ylabel(r'y')
    ax.set_zlabel(r'z')

    plt.show()


half_sphere()


# Två halvspiraler som går runt varandra
def spirals():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z = np.linspace(0, 10, 100)
    x = np.sin(z)
    y = np.cos(z)
    ax.plot3D(x, y, z, 'red')
    z = np.linspace(0, 10, 100)
    x = np.sin(z+np.pi)
    y = np.cos(z+np.pi)
    ax.plot3D(x, y, z, 'blue')

    plt.show()

# Plot the surface
# ax.plot_surface(xline, yline, zline, color='b')

spirals()

'''
# Uppgift 10a)

a = np.array([[4, -1, -9, -4, -6],
            [1, 1, -1, 4, -5],
            [0, -3, 4, 7, 0],
            [3, -5, -5, -3, 7],
            [9, -1, 4, -8, -9]])
b = np.array([[-59, -21, 20, 16, -11]])

b = b.reshape(5, 1)
answer = np.linalg.solve(a, b)
print(answer)

# Uppgift 10b)

text = open('Shinkansen.text', 'r')
info = text.readlines()
info.pop(0)
info.pop(0)
for i in range(len(info)):
    info[i] = info[i].strip()
    info[i] = info[i].split(' ')

info_prices = []
info_distance = []
print(info)
for i in info:
    info_prices.append(float(i[1]))
    info_distance.append(float(i[2]))

info_prices = np.array(info_prices)
info_distance = np.array(info_distance)
info_distance = info_distance[:, np.newaxis]**[0, 1]
P, res, rank, s = np.linalg.lstsq(info_distance, info_prices, rcond=None)
print(P)


# Uppgift 10c)

text = open('Naringsbehov.text', 'r')
text2 = open('nutrients.text', 'r')
nutlist = []
pris = []
for line in text2:
    if '#' not in line:
        nutlist.append(line)

for i in range(len(nutlist)):
    nutlist[i] = nutlist[i].strip()
    nutlist[i] = nutlist[i].split(' ')

for i in range(len(nutlist)):
    nutlist[i] = list(filter(('').__ne__, nutlist[i]))

nutlist = list(filter(([]).__ne__, nutlist))
price = []
a_ub = []
b_ub = []
food = []
joule = []
for i in range(len(nutlist)):
    price.append(float(nutlist[i][13]))
    nutlist[i].pop(13)
    joule.append(float(nutlist[i][12]))
    nutlist[i].pop(12)
    food.append(str(nutlist[i][0]))
    nutlist[i].pop(0)
    for j in range(len(nutlist[i])):
        a_ub.append(float(nutlist[i][j]))
a_ub = np.array(a_ub)
a_ub = a_ub.reshape(len(nutlist), len(nutlist[0]))
a_ub = a_ub.T
a_eq = np.matrix([joule])
b_eq = np.matrix(8710)
b_ub = np.array([60000, 275000, 70000, 0.7, 1.1, 1.2, 15, 0.002, 75, 0.01, 0.065])
price = np.array([price])
print(a_ub)

res = optimize.linprog(price, -a_ub, -b_ub, a_eq, b_eq, options={"tol": 1e-10})
print(res)

