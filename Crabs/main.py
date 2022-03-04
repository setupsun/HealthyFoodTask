import matplotlib.pyplot as plt
import numpy as np

#Reading and parsing
def arrayY():
    r_file = open('data.txt', 'r')
    # r_file = open('TestData.txt', 'r')
    # r_file = open('TestDataBigToLittle.txt', 'r')
    arrY = np.array(str(r_file.read()).split(','), dtype=np.int64)
    return(arrY)

#Fuel Calculation Formula
def f(n):
    f = (n * (n+1))/2
    return (f)

#Visualization of dataset
def arrayX():
    arrX = [i for i in range(len(arrayY()))]
    return(arrX)
y_level = (sum(arrayY()) // len(arrayY()))
level_arr = np.full(shape=len(arrayY()), fill_value=y_level, dtype=np.int64)
sortArr = arrayY()
sortArr.sort()
#Visialisation of solving data with step x = 1
fig, (ax1 ,ax2) = plt.subplots(nrows = 1, ncols = 2, figsize=(10,5))
ax1.scatter(arrayX(), arrayY(), c='deeppink', s=1)
ax1.scatter(arrayX(), level_arr, c='red', s=1)
ax1.set_facecolor('black')
ax1.set_title('Unsorted data-Set')
ax2.scatter(arrayX(), sortArr, c='deeppink', s=1)
ax2.scatter(arrayX(), level_arr, c='red', s=1)
ax2.set_facecolor('black')
ax2.set_title('Sorted data-Set')
plt.show()

#Median method
y_level = (sum(arrayY()) // len(arrayY()))
level_arr = np.full(shape=len(arrayY()), fill_value=y_level, dtype=np.int64)
pure_sum_arr = np.array([])
for k in range (0, len(arrayY())):
    if arrayY()[k] < level_arr[k]:
        new_element_sum = level_arr[k] - arrayY()[k]
        pure_sum_arr = np.append(pure_sum_arr, new_element_sum)
    else:
        new_element_diff = arrayY()[k] - level_arr[k]
        pure_sum_arr = np.append(pure_sum_arr, new_element_diff)
i = 0
new = np.array([])
while i <= (len(pure_sum_arr)-1):
    n = pure_sum_arr.flat[i]
    k = f(n)
    new = np.append(new, k)
    i = i + 1
s_new = sum(new)

#Dichotomy
def dichotomyMethod(a, b, precision, c, y, our_fun):
  while abs(b - a) > precision:
    x = (a + b) / 2
    f1 = our_fun(y, x - precision)
    f2 = our_fun(y, x + precision)
    if c * f1 < c * f2:
      b = x
    else:
      a = x
  x = (b + a) / 2
  return x, our_fun(y, x)

#Golden selection
def golden_sectionMethod(a, b, precision, c, y, our_fun):
  phi = (1 + 5**(0.5)) / 2
  x1 = b - (b - a) / phi
  x2 = a + (b - a) / phi
  while abs(b - a) / 2 >= precision:
    f1 = our_fun(y, x1)
    f2 = our_fun(y, x2)
    if c * f1 > c * f2:
      a = x1
      x1 = x2
      x2 = b - (x1 - a)
    else:
      b = x2
      x2 = x1
      x1 = a + (b - x2)
  x = (a + b) / 2
  return x, our_fun(y, x)

#Calculations
def getting_Way(x1, b):
  c = np.array([0, 1])
  x = np.array([0, 0])
  return abs(c.dot((x - x1)) + b)

def fuel_Needs(our_Way):
  return ((1 + our_Way) / 2) * our_Way

def our_fun(y, i):
  cost = 0
  for p in y:
    our_Way = getting_Way(p, i)
    cost += fuel_Needs(our_Way)
  return cost

def check_min(x, y):
  if x < round(x):
    x1 = round(x) - 1
  else:
    x1 = round(x) + 1
  x2 = round(x)
  cost1 = our_fun(y, x1)
  cost2 = our_fun(y, x2)
  cost = 0
  if cost1 < cost2:
    cost = cost1
  else:
    cost = cost2
  return cost
precision = 0.0001
x, cost = dichotomyMethod(sortArr[0], sortArr[-1], precision, 1, sortArr, our_fun)
x, cost = golden_sectionMethod(sortArr[0], sortArr[-1], precision, 1, sortArr, our_fun)

#Printing
print(f'Дихотомия -> {check_min(x, sortArr)}')
print(f'Золотое сечение -> {check_min(x, sortArr)}')
print('Серединное значение->', s_new)
