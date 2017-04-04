import platform

system = platform.system()

if system == 'Linux':
    from .i3 import Wm  # noqa
elif system == 'Darwin':
    from .macos import Wm  # noqa
else:
    raise NotImplementedError('Your window manager is not supported')
