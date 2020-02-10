import matplotlib.pyplot as plt
import math

def func(x):
    return math.sin(x)

def plot_func(f, x1, x2, nx):
    dx = (x2-x1)/nx
    x = []
    y = []
    for i in range(nx+1):
        x.append(x1+i*dx)
        y.append(f(x[i]))
    
    plt.style.use('seaborn-notebook')
    fig,ax = plt.subplots()
    ax.plot(x, y, linewidth = 3)
    ax.set_title("График функции", fontsize = 14)
    ax.set_xlabel("x", fontsize = 14)
    ax.set_ylabel("f(x)", fontsize = 14)
    ax.tick_params(axis="both", labelsize = 14)
    plt.show()

to_deg = 180/math.pi
to_rad = math.pi/180
plot_func(lambda x:math.sin(x*to_rad), -math.pi*to_deg, math.pi*to_deg, 100)

# print(plt.style.available)





# a = [1,4,9,16,25]
# fig,ax = plt.subplots()
# ax.plot(a)

# plt.show()