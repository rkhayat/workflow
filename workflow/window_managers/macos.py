from workflow.utils import json
from .base import AbstractWm


def screen_size_tuple(width_factor=1, height_factor=1):
    from AppKit import NSScreen
    size = NSScreen.mainScreen().frame().size
    return size.width * width_factor, size.height * height_factor


def set_size_of_app(app, size, position, index=0):
    from ScriptingBridge import SBApplication
    app = SBApplication.applicationWithBundleIdentifier_(app)
    finderWin = app.windows()[index]
    finderWin.setBounds_([size, size])
    finderWin.setPosition_(position)


def setup_window(config, index=0):
    size = screen_size_tuple(width_factor=0.5)
    x_position = 0 if index == 0 else size[0]
    y_position = 0
    set_size_of_app(
        'com.apple.Finder',
        size,
        position=[x_position, y_position],
        index=index
    )


class Wm(AbstractWm):
    def setup_workflow(self, workflow):
        print(json.dumps(workflow))
        for index, window in enumerate(workflow):
            setup_window(window, index)

    @property
    def is_supported_in_current_environment(self):
        try:
            from AppKit import NSScreen
            return True
        except ImportError:
            return False
