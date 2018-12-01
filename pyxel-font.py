"""
PYXEL FONT

Use the arrow keys ← ↑ → ↓
Or vim keys h j k l
Q: Quit the editor
R: Restart the editor

Created by Eli Heuer in 2018.
licensed under the GPL(v3).
"""

from collections import namedtuple
from random import randint
import pyxel

Point = namedtuple("Point", ["x", "y"]) # for coordinates

#############
# Constants #
#############

COL_BACKGROUND = 1
WIDTH = 240
HEIGHT = 160

##############
# The Editor #
##############


class PyxelFont:
    """The class that sets up and runs the font editor."""

    def __init__(self):
        """Initiate pyxel, set up initial variables, and run."""

        pyxel.init(WIDTH, HEIGHT, caption="PYXEL FONT", scale=4, fps=20)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(55, 41, "PYXEL FONT", pyxel.frame_count % 16)
        pyxel.blt(61, 66, 0, 0, 0, 38, 16)

if __name__ == '__main__':
    PyxelFont()
