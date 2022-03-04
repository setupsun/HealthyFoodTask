from matplotlib import pyplot as plt
import numpy as np

def turn_sign(a, b, c):
    return ((b[0] - a[0]) * (c[1] - a[1])) - ((b[1] - a[1]) * (c[0] - a[0]))

def bubble_sort(points, indecies):
    n = len(points)
    for i in range(0, n - 1):
        for j in range(1, n - i - 1):
            if turn_sign(points[indecies[0]], points[indecies[j]], points[indecies[j + 1]]) < 0:
                indecies[j], indecies[j + 1] = indecies[j + 1], indecies[j]

def compareX(p1, p2):
    return p1[0] > p2[0]

def make_first_idx_min_x(points, indecies):
    for i in range(1, len(indecies)):
        if compareX(points[indecies[0]], points[indecies[i]]) == True:
            indecies[0], indecies[i] = indecies[i], indecies[0]

def remove_interior_points(points, indecies):
    convex_set = [indecies[0], indecies[1]]

    for i in range(len(indecies)):
        while turn_sign(points[convex_set[-2]], points[convex_set[-1]], points[indecies[i]]) < 0:
            convex_set.pop()
        convex_set.append(indecies[i])
    convex_set.append(indecies[0])
    return convex_set

def search_point(points, target_point):
  for i in points:
    if i[0] == target_point[0] and i[1] == target_point[1]:
      return True
  return False

def draw_points(points, convex_set):
    for p in points:
      if search_point(convex_set, p):
        plt.plot([p[0]], [p[1]], color='r', marker='.', markersize=10)
      else:
        plt.plot([p[0]], [p[1]], color='g', marker='.', markersize=10)
    plt.plot(points[0][0], points[0][1], color='purple', marker='*', markersize=15)
def main():
    points = np.array([[1, 1], [2, -3], [5, 1], [3, 4],
                       [3, 2], [3, 3], [2, -1], [2, 0],
                       [2.5, 1], [4, 0], [4.5, 3], [1.5, -2],
                       [3.5, -2], [1.5, 3], [1.5, -3]])

    indecies = [i for i in range(len(points))]
    make_first_idx_min_x(points, indecies)
    bubble_sort(points, indecies)
    convex_set_indecies = remove_interior_points(points, indecies)
    convex_set = list()
    for i in convex_set_indecies:
      convex_set.append(points[i])
    draw_points(points, convex_set)
    for i in range(len(convex_set_indecies) - 1):
        plt.plot([points[convex_set_indecies[i]][0], points[convex_set_indecies[i + 1]][0]],
                 [points[convex_set_indecies[i]][1], points[convex_set_indecies[i + 1]][1]], color='b')
                 
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.show()
if __name__ == "__main__":
    main()


