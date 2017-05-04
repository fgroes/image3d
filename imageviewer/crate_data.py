import numpy as np
from scipy import misc
from PIL import Image


# img_file = r"image001.png"
# img = misc.imread(img_file)


img_orig = Image.open("01561.tiff")
img = np.array(img_orig)
max = np.max(np.max(img))
min = np.min(np.min(img))

with open("color_map.csv") as fid:
    lines = fid.readlines()
cm = np.array([[float(x) for x in line.split(",")] for line in lines])

s = img.shape
max_len = np.max(s[:2])
M = s[0]
N = s[1]
dx = 1.0 / max_len
# dx = 0.5
vertex_len = 3
color_len = 3
data_len = vertex_len + color_len
num_vertices = M * N * data_len
vertices = np.zeros(num_vertices, dtype=np.float32)
num_indices = (M - 1) * (N - 1) * 2 * 3
indices = np.zeros(num_indices, dtype=np.uint32)
for m in range(M):
    for n in range(N):
        i = (m * N + n) * data_len
        vertices[i] = m * dx
        vertices[i + 1] = n * dx
        # vertices[i + 2] = np.sum(img[m, n, :3]) / (255 * 3)
        # vertices[i + 3] = 1.0 * img[m, n, 0] / 255
        # vertices[i + 4] = 1.0 * img[m, n, 1] / 255
        # vertices[i + 5] = 1.0 * img[m, n, 2] / 255
        h = (1.0 * img[m, n] - min) / (max - min)
        h_idx = np.min([int(256 * h), 255])
        vertices[i + 2] = h
        vertices[i + 3] = cm[h_idx, 0]
        vertices[i + 4] = cm[h_idx, 1]
        vertices[i + 5] = cm[h_idx, 2]
k = 0
for m in range(M - 1):
    for n in range(N - 1):
        indices[k] = m * N + n
        indices[k + 1] = m * N + n + 1
        indices[k + 2] = (m + 1) * N + n
        indices[k + 3] = (m + 1) * N + n
        indices[k + 4] = m * N + n + 1
        indices[k + 5] = (m + 1) * N + n + 1
        k += 6


# indices = np.array([
#     0, 1, N, N, 1, N + 1, 1, 2, N + 1, N + 1, 2, N + 2
# ], dtype=np.uint32)


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



