# -*- coding: utf-8 -*-

"""solarized.py

Import to adust matplotlibs rcParams to use solarized colors (dark as default).
You may want to call solarize("light") if you need the light version.

"""

__author__ = "Stephan Porz"

import matplotlib as mpl

COLOR = {"base03":  "#002B36",
         "base02":  "#073642",
         "base01":  "#586e75",
         "base00":  "#657b83",
         "base0":   "#839496",
         "base1":   "#93a1a1",
         "base2":   "#EEE8D5",
         "base3":   "#FDF6E3",
         "yellow":  "#B58900",
         "orange":  "#CB4B16",
         "red":     "#DC322F",
         "magenta": "#D33682",
         "violet":  "#6C71C4",
         "blue":    "#268BD2",
         "cyan":    "#2AA198",
         "green":   "#859900"
         }

# rebase: original naming for dark, renamed for light
DARK = {"03": COLOR["base03"],
        "02": COLOR["base02"],
        "01": COLOR["base01"],
        "00": COLOR["base00"],
        "0":  COLOR["base0"],
        "1":  COLOR["base1"],
        "2":  COLOR["base2"],
        "3":  COLOR["base3"]
        }
LIGHT = {"03": COLOR["base3"],
         "02": COLOR["base2"],
         "01": COLOR["base1"],
         "00": COLOR["base0"],
         "0":  COLOR["base00"],
         "1":  COLOR["base01"],
         "2":  COLOR["base02"],
         "3":  COLOR["base03"]
         }


def solarize(mode="dark"):
    """solarize(mode="dark")

    Changes default colors of matplotlib to solarized.

    Params
    ------
    mode: str
        Can be "light" or "dark". Defaults to "dark".

    """
    if mode == "dark":
        rebase = DARK
    elif mode == "light":
        rebase = LIGHT

    params = {"ytick.color": rebase["0"],  # 'k'
              "xtick.color": rebase["0"],  # 'k'
              "text.color": rebase["0"],  # 'k'
              "savefig.facecolor": rebase["03"],  # 'w'
              "patch.facecolor": COLOR["blue"],  # 'b'
              "patch.edgecolor": rebase["0"],  # 'k'
              "grid.color": rebase["0"],  # 'k'
              "figure.edgecolor": rebase["03"],  # 'w'
              "figure.facecolor": rebase["02"],  # '0.75'
              "axes.color_cycle": [COLOR["blue"], COLOR["green"], COLOR["red"],
                                   COLOR["cyan"], COLOR["magenta"],
                                   COLOR["yellow"], rebase["0"]],
              # ['b', 'g', 'r', 'c', 'm', 'y', 'k']
              "axes.edgecolor": rebase["0"],  # 'k'
              "axes.facecolor": rebase["03"],  # 'w'
              "axes.labelcolor": rebase["0"],  # 'k'
              }

    mpl.rcParams.update(params)


def dark():
    """dark()

    Changes default colors of matplotlib to solarized dark theme.

    """
    solarize()


def light():
    """dark()

    Changes default colors of matplotlib to solarized light theme.

    """
    solarize("light")
