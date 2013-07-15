import pylab

def do_solarize(var="dark"):

    base03 = "#002B36"
    base02 = "#073642"
    base01 = "#586e75"
    base00 = "#657b83"
    base0 = "#839496"
    base1 = "#93a1a1"
    base2 = "#EEE8D5"
    base3 = "#FDF6E3"
    yellow = "#B58900"
    orange = "#CB4B16"
    red = "#DC322F"
    magenta = "#D33682"
    violet = "#6C71C4"
    blue = "#268BD2"
    cyan = "#2AA198"
    green = "#859900"

    p_d = {"ytick.color": base0,  # 'k'
           "xtick.color": base0,  # 'k'
           "text.color": base0,  # 'k'
           "savefig.facecolor": base03,  # 'w'
           "patch.facecolor": blue,  # 'b'
           "patch.edgecolor": base0,  # 'k'
           "grid.color": base0,  # 'k'
           "figure.edgecolor": base03,  # 'w'
           "figure.facecolor": base02,  # '0.75'
           "axes.color_cycle": [blue, green, red, cyan, magenta, yellow,
                                base0],  # ['b', 'g', 'r', 'c', 'm', 'y', 'k']
           "axes.edgecolor": base0,  # 'k'
           "axes.facecolor": base03,  # 'w'
           "axes.lablecolor": base0,  # 'k'
           }

    p_l = {"ytick.color": base00,  # 'k'
           "xtick.color": base00,  # 'k'
           "text.color": base00,  # 'k'
           "savefig.facecolor": base3,  # 'w'
           "patch.facecolor": blue,  # 'b'
           "patch.edgecolor": base00,  # 'k'
           "grid.color": base00,  # 'k'
           "figure.edgecolor": base3,  # 'w'
           "figure.facecolor": base2,  # '0.75'
           "axes.color_cycle": [blue, green, red, cyan, magenta, yellow,
                                base00],  # ['b', 'g', 'r', 'c', 'm', 'y', 'k']
           "axes.edgecolor": base00,  # 'k'
           "axes.facecolor": base3,  # 'w'
           "axes.lablecolor": base00,  # 'k'
          }

    if var == "dark":
        pylab.rcParams.update(p_d)
    elif var == "light":
        pylab.rcParams.update(p_l)

do_solarize()
