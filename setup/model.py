import OpenGL.GL as gl
import ctypes
import numpy as np


class Texture(object):

    def __init__(self, width, height, data):
        self.width = width
        self.height = height
        self.data = data


class Model(object):

    def __init__(self, vao_id, vertices, indices, texture=None):
        self.vao_id = vao_id
        self.vertices = vertices
        self.indices = indices
        self.texture = texture

    @property
    def vertex_count(self):
        return len(self.vertices)

    @property
    def index_count(self):
        return len(self.indices)


class ModelLoader(object):

    def __init__(self, vertex_loc, color_loc, texture_loc):
        self._vaos = []
        self._vbos = []
        self._vertex_loc = vertex_loc
        self._color_loc = color_loc
        self._texture_loc = texture_loc
        self._dtype = np.dtype(np.float32)
        self._type = gl.GL_FLOAT
        self._vertex_dim = 3
        self._color_dim = 3
        self._tex_dim = 2

    @property
    def stride(self):
        return (self._vertex_dim + self._color_dim + self._tex_dim) * self._dtype.itemsize

    def load_to_vao(self, vertices, indices, texture=None):
        assert type(vertices) is np.ndarray, type(vertices)
        assert vertices.dtype is self._dtype, vertices.dtype
        vao_id = self.create_vao()
        self._vaos.append(vao_id)
        self.store_vertices(vertices)
        self.store_colors()
        if texture is not None:
            offset = (self._vertex_dim + self._color_dim) * self._dtype.itemsize
            self.store_texture(texture, offset)
        self.store_indices(indices)
        self.unbind()
        return Model(vao_id, vertices, indices)

    def clean_up(self):
        for vao in self._vaos:
            gl.glDeleteVertexArrays(vao)
        for vbo in self._vbos:
            gl.glDeleteVertexBuffers(vbo)

    def create_vao(self):
        vao_id = gl.glGenVertexArrays(1)
        gl.glBindVertexArray(vao_id)
        return vao_id

    def store_vertices(self, vertices):
        offset = ctypes.c_void_p(0)
        vbo_id = gl.glGenBuffers(1)
        self._vbos.append(vbo_id)
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, vbo_id)
        gl.glBufferData(gl.GL_ARRAY_BUFFER, vertices.nbytes, vertices, gl.GL_STATIC_DRAW)
        gl.glVertexAttribPointer(self._vertex_loc, self._vertex_dim, gl.GL_FLOAT, gl.GL_FALSE, self.stride, offset)
        gl.glEnableVertexAttribArray(self._vertex_loc)

    def store_colors(self):
        color_offset = ctypes.c_void_p(self._vertex_dim * self._dtype.itemsize)
        gl.glVertexAttribPointer(self._color_loc, self._color_dim, gl.GL_FLOAT, gl.GL_FALSE, self.stride, color_offset)
        gl.glEnableVertexAttribArray(self._color_loc)

    def store_indices(self, indices):
        index_vbo_id = gl.glGenBuffers(1)
        self._vbos.append(index_vbo_id)
        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, index_vbo_id)
        gl.glBufferData(gl.GL_ELEMENT_ARRAY_BUFFER, indices.nbytes, indices, gl.GL_STATIC_DRAW)
        gl.glBindBuffer(gl.GL_ELEMENT_ARRAY_BUFFER, 0)

    def store_texture(self, texture, offset):
        offset = ctypes.c_void_p(offset)
        gl.glVertexAttribPointer(self._texture_loc, self._tex_dim, gl.GL_FLOAT, gl.GL_FALSE, self.stride, offset)
        gl.glEnableVertexAttribArray(self._texture_loc)

        tex_vbo_id = gl.glGenTextures(1)
        self._vbos.append(tex_vbo_id)
        gl.glBindTexture(gl.GL_TEXTURE_2D, tex_vbo_id)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_S, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_WRAP_T, gl.GL_REPEAT)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MIN_FILTER, gl.GL_LINEAR)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_LINEAR)
        gl.glTexImage2D(gl.GL_TEXTURE_2D, 0, gl.GL_RGB, texture.width, texture.height, 0, gl.GL_RGB,
                        gl.GL_UNSIGNED_BYTE, texture.data)
        gl.glBindTexture(gl.GL_TEXTURE_2D, 0)

    def unbind(self):
        gl.glBindBuffer(gl.GL_ARRAY_BUFFER, 0)
        gl.glBindVertexArray(0)