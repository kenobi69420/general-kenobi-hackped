print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (board.D10, board.D9, board.D8,)
keyboard.row_pins = (board.D0, board.D1, board.D2,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.D,KC.Q,KC.L,]
    [KC.K,KC.H,KC.M,],
    [KC.O,KC.X,KC.0,]
]

if __name__ == '__main__':
    keyboard.go()
