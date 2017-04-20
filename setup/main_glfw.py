import glfw
import OpenGL.GL as gl


def main():

    # initialize glfw
    if not glfw.init():
        return

    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 2)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, gl.GL_TRUE)

    window = glfw.create_window(800, 600, "My OpenGL window", None, None)

    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.swap_interval(1)

    i = 0
    while not glfw.window_should_close(window):
        glfw.swap_buffers(window)
        i += 1
        if i > 10000: break

        glfw.poll_events()

    glfw.terminate()


if __name__ == "__main__":
    main()