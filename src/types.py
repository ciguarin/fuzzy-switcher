from dataclasses import dataclass
from typing import Any


@dataclass
class Window:
    title: str
    app_name: str
    pid: int
    ax_element: Any  # AXUIElement — opaque to fuzzy.py