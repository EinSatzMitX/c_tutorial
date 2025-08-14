from manim import ManimColor

# central place for all colors — use ManimColor so colors are first-class
BG    = ManimColor("#282828")
FG    = ManimColor("#ebdbb2")
RED   = ManimColor("#fb4934")
GREEN = ManimColor("#b8bb26")
YELLOW= ManimColor("#fabd2f")
BLUE  = ManimColor("#83a598")
PURPLE= ManimColor("#d3869b")
AQUA  = ManimColor("#8ec07c")
ORANGE= ManimColor("#fe8019")
GRAY  = ManimColor("#928374")

# optional convenience dict
PALETTE = {
    "bg": BG, "fg": FG,
    "red": RED, "green": GREEN, "yellow": YELLOW,
    "blue": BLUE, "purple": PURPLE, "aqua": AQUA, "orange": ORANGE,
    "gray": GRAY
}