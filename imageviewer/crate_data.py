import numpy as np
from scipy import misc


img_file = r"image001.png"
img = misc.imread(img_file)
s = img.shape
max_len = np.max(s[:2])
M = s[0]
N = s[1]
#dx = 1.0 / max_len
dx = 0.5
vertex_len = 3
color_len = 3
data_len = vertex_len + color_len
data_points = M * N * data_len
vertices = np.zeros(data_points, dtype=np.float32)
k = 0
for m in range(M):
    print(m)
    for n in range(N):
        i = (m * N + n) * data_len
        vertices[i] = m * dx
        vertices[i + 1] = n * dx
        vertices[i + 2] = np.sum(img[m, n, :3]) / (255 * 3)
        vertices[i + 3] = 1.0 * img[m, n, 0] / 255
        vertices[i + 4] = 1.0 * img[m, n, 1] / 255
        vertices[i + 5] = 1.0 * img[m, n, 2] / 255

print(vertices[:6])
print(vertices[6:12])
print(vertices[N * 6: (N + 1) * 6])

indices = np.array([
    0, 1, N, N, 1, N + 1, 1, 2, N + 1, N + 1, 2, N + 2
], dtype=np.uint32)


# dx = 0.2
# vertices = np.array([
#     0.0, 0.0, 0.0, 1.0, 0.0, 0.0,
#     dx, 0.0, 0.0, 0.0, 1.0, 0.0,
#     0.0, dx, 0.0, 0.0, 0.0, 1.0,
#     0.0, dx, 0.0, 1.0, 1.0, 0.0,
#     dx, 0.0, 0.0, 1.0, 0.0, 1.0,
#     dx, dx, 0.0, 0.0, 1.0, 1.0,
#     0.0, dx, 0.0, 1.0, 0.0, 0.0,
#     dx, dx, 0.0, 1.0, 0.0, 0.0,
#     0.0, 2 * dx, 0.0, 1.0, 0.0, 0.0,
#     0.0, 2 * dx, 0.0, 0.0, 0.0, 1.0,
#     dx, dx, 0.0, 0.0, 0.0, 1.0,
#     dx, 2 * dx, 0.0, 0.0, 0.0, 1.0,
#     dx, 0.0, 0.0, 0.0, 1.0, 0.0,
#     2 * dx, 0.0, 0.0, 0.0, 1.0, 0.0,
#     dx, dx, 0.0, 0.0, 1.0, 0.0,
#     dx, dx, 0.0, 1.0, 0.0, 0.0,
#     2 * dx, 0.0, 0.0, 1.0, 0.0, 0.0,
#     2 * dx, dx, 0.0, 1.0, 0.0, 0.0,
#     dx, dx, 0.0, 0.0, 1.0, 0.0,
#     2 * dx, dx, 0.0, 0.0, 1.0, 0.0,
#     dx, 2 * dx, 0.0, 0.0, 1.0, 0.0,
#     dx, 2 * dx, 0.0, 0.0, 0.0, 1.0,
#     2 * dx, dx, 0.0, 0.0, 0.0, 1.0,
#     2 * dx, 2 * dx, 0.0, 0.0, 0.0, 1.0
# ], dtype=np.float32)





# indices = np.array([
#     0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
# ], dtype=np.uint32)



