import numpy as np
from scipy import misc


# img_file = r"image001.png"
# img = misc.imread(img_file)
# s = img.shape
# max_len = np.max(s[:2])
# M = s[0]
# N = s[1]
# dx = 1.0 / max_len
# num_triangles = 2
# num_vertices = 3
# vertex_len = 3
# color_len = 3
# tri = [[0.0, 0.0], [1.0, 0.0], [0.0, 1.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]
# data_points = (M - 1) * (N - 1) * num_triangles * num_vertices * vertex_len * color_len
# vertices = np.zeros(data_points, dtype=np.float32)
# k = 0
# for i in range(M - 1):
#     for j in range(N - 1):
#         for t in range(num_triangles):
#             stride = num_triangles * num_vertices * vertex_len * color_len
#             idx = i * j * stride
#             for c in range(vertex_len - 1):
#                 vertices[idx + c] = tri[t * 3][1] + i * dx
#             vertices[idx + 2] = 0.0


dx = 0.2
vertices = np.array([
    0.0, 0.0, 0.0, 1.0, 0.0, 0.0,
    dx, 0.0, 0.0, 0.0, 1.0, 0.0,
    0.0, dx, 0.0, 0.0, 0.0, 1.0,
    0.0, dx, 0.0, 1.0, 1.0, 0.0,
    dx, 0.0, 0.0, 1.0, 0.0, 1.0,
    dx, dx, 0.0, 0.0, 1.0, 1.0,
    0.0, dx, 0.0, 1.0, 0.0, 0.0,
    dx, dx, 0.0, 1.0, 0.0, 0.0,
    0.0, 2 * dx, 0.0, 1.0, 0.0, 0.0,
    0.0, 2 * dx, 0.0, 0.0, 0.0, 1.0,
    dx, dx, 0.0, 0.0, 0.0, 1.0,
    dx, 2 * dx, 0.0, 0.0, 0.0, 1.0,
    dx, 0.0, 0.0, 0.0, 1.0, 0.0,
    2 * dx, 0.0, 0.0, 0.0, 1.0, 0.0,
    dx, dx, 0.0, 0.0, 1.0, 0.0,
    dx, dx, 0.0, 1.0, 0.0, 0.0,
    2 * dx, 0.0, 0.0, 1.0, 0.0, 0.0,
    2 * dx, dx, 0.0, 1.0, 0.0, 0.0,
    dx, dx, 0.0, 0.0, 1.0, 0.0,
    2 * dx, dx, 0.0, 0.0, 1.0, 0.0,
    dx, 2 * dx, 0.0, 0.0, 1.0, 0.0,
    dx, 2 * dx, 0.0, 0.0, 0.0, 1.0,
    2 * dx, dx, 0.0, 0.0, 0.0, 1.0,
    2 * dx, 2 * dx, 0.0, 0.0, 0.0, 1.0
], dtype=np.float32)





indices = np.array([
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
], dtype=np.uint32)



