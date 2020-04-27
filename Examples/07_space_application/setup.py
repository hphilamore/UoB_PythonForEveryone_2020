"""
Creates an executable file
"""

import cx_Freeze
import sys

executables = [cx_Freeze.Executable("05_space_game.py")]

cx_Freeze.setup(
    name="Space",
    options={"build_exe": {"packages":["pygame", "sys", "random", "math"],
                           "include_files":["space.jpg",
                                            "saucer.png",
                                            "fire.png",
                                            "monster.png",
                                            "battleThemeB.mp3",
                                            "zap8a.ogg"
                                         ]}},
    executables = executables

    )