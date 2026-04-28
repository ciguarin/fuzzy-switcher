from AppKit import NSWorkspace
from ApplicationServices import AXUIElementCreateApplication, AXUIElementCopyAttributeValue

from src.types import Window


def get_windows() -> list[Window]:
    running_apps = [app for app in NSWorkspace.sharedWorkspace().runningApplications() if app.activationPolicy() == 0]

    windows = []

    for app in running_apps:
        pid = app.processIdentifier()
        app_ax_obj = AXUIElementCreateApplication(pid)

        err, window = AXUIElementCopyAttributeValue(app_ax_obj, "AXWindows", None)

        if err == 0 and window:
            for window_ax_obj in window:
                err, title = AXUIElementCopyAttributeValue(window_ax_obj, "AXTitle", None)

                if err == 0 and title:
                    windows.append(Window(title, app.localizedName(), pid, window_ax_obj, app))

    return windows