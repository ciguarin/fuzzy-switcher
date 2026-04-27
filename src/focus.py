from src.types import Window
from ApplicationServices import AXUIElementPerformAction


def focus_window(window: Window) -> None:
    window.ns_app.activateWithOptions_(0)
    AXUIElementPerformAction(window.ax_element, "AXRaise")