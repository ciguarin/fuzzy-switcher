from ApplicationServices import AXUIElementPerformAction

from src.types import Window


def focus_window(window: Window) -> None:
    window.ns_app.activateWithOptions_(2)
    AXUIElementPerformAction(window.ax_element, "AXRaise")