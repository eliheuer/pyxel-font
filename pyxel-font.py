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
import math

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
 
        pyxel.image(0).load(0, 0, "assets/pencil_16x16.png")
        pyxel.image(1).load(0, 0, "assets/pencil_16x16.png")
        pyxel.image(2).load(0, 0, "assets/pencil_16x16.png")

        pyxel.run(self.update, self.draw)
        pyxel.mouse(True)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(5)
        pyxel.text(5, 5, "PYXEL FONT", pyxel.frame_count % 16)
        self.test_blt()

    def test_blt(self):
            pyxel.blt(4, 16*1, 0, 0, 0, 16, 16)
            pyxel.blt(4, 16*2, 0, 0, 0, 16, 16)
            pyxel.blt(4, 16*3, 0, 0, 0, 16, 16)
            pyxel.blt(4, 16*4, 0, 0, 0, 16, 16)
            pyxel.blt(4, 16*5, 0, 0, 0, 16, 16)
            pyxel.blt(4, 16*6, 0, 0, 0, 16, 16)
            pyxel.blt(4, 16*7, 0, 0, 0, 16, 16)

if __name__ == '__main__':
    PyxelFont()
