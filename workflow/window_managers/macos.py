import invoke
from AppKit import NSScreen
from ScriptingBridge import SBApplication


def screen_size_tuple(width_factor=1, height_factor=1):
    size = NSScreen.mainScreen().frame().size
    return size.width * width_factor, size.height * height_factor


def set_size_of_app(app, size, position):
    app = SBApplication.applicationWithBundleIdentifier_(app)
    finderWin = app.windows()[0]
    finderWin.setBounds_([size, size])
    finderWin.setPosition_(position)


class Wm:
    def __init__(self, debug=False):
        self.debug = debug

    def create_workflow(self):
        raise NotImplementedError

    def create_workspace(self, workspace):
        if workspace.layout.layout == 'splith':
            set_size_of_app(
                'com.apple.Finder',
                screen_size_tuple(width_factor=0.5),
                position=[0, 0]
            )
        print(workspace.__dict__)
        print(workspace.layout.__dict__)
        raise NotImplementedError()

    def create_layout(self, layout):
        print(layout)
        raise NotImplementedError

    def command(self, cmd):
        if self.debug:
            print(cmd)
        else:
            invoke.run(cmd)

    def open(self, cmd):
        self.command("exec " + cmd)

    def get_current_workspace(self):
        raise NotImplementedError()
