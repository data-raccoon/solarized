# -*- coding: utf-8 -*-

"""solarize_me.py

"""

__author__ = "Stephan Porz"


def int_to_hex(val_r, val_g, val_b, concat=True, hashtag=False):
    """ TODO
    """
    hex_r = "%02x" % val_r
    hex_g = "%02x" % val_g
    hex_b = "%02x" % val_b
    
    if concat:
        if hashtag:
            return "#" + hex_r + hex_g + hex_b
        else:
            return hex_r + hex_g + hex_b
    else:
        return hex_r, hex_g, hex_b


def hex_to_int(hex_r, hex_g=None, hex_b=None):
    """ TODO
    """
    # in case we get a concated version "ffffff"
    if len(hex_r) == 6:
        hex_b = hex_r[4:6]
        hex_g = hex_r[2:4]
        hex_r = hex_r[0:2]
    
    # in case the concated version is html formatted "#ffffff"
    if len(hex_r) == 7:
        hex_b = hex_r[5:7]
        hex_g = hex_r[3:5]
        hex_r = hex_r[1:3]

    val_r = int(hex_r, 16)
    val_g = int(hex_g, 16)
    val_b = int(hex_b, 16)
    
    return val_r, val_g, val_b
      

def xyz_to_rgb(val_X, val_y, val_z):
    """ TODO
    """
    # (Observer = 2°, Illuminant = D65)
    var_x = val_x / 100.  # val_x from 0 to  95.047      
    var_y = val_y / 100.  # val_y from 0 to 100.000
    var_z = val_z / 100.  # val_z from 0 to 108.883

    var_r = var_x *  3.2406 + var_y * -1.5372 + var_z * -0.4986
    var_g = var_x * -0.9689 + var_y *  1.8758 + var_z *  0.0415
    var_b = var_x *  0.0557 + var_y * -0.2040 + var_z *  1.0570

    if var_r > 0.0031308:
	var_r = 1.055 * (var_r ** (1. / 2.4)) - 0.055
    else:
        var_r = 12.92 * var_r
    
    if var_g > 0.0031308:
        var_g = 1.055 * (var_g ** (1. / 2.4)) - 0.055
    else:
        var_g = 12.92 * var_g
    
    if var_b > 0.0031308:
        var_b = 1.055 * (var_b ** (1. / 2.4)) - 0.055
    else:
        var_b = 12.92 * var_b
    
    res_r = var_r * 255
    res_g = var_g * 255
    res_b = var_b * 255

    return (res_r, res_g, res_b)


def rgb_to_xyz(val_r, val_g, val_b):
    """ TODO
    """
    # Observer. = 2°, Illuminant = D65
    var_r = val_r / 255.  # val_r from 0 to 255
    var_g = val_g / 255.  # val_g from 0 to 255
    var_b = val_b / 255.  # val_b from 0 to 255

    if var_r > 0.04045:
        var_r = ((var_r + 0.055) / 1.055) ** 2.4
    else:
        var_r = var_r / 12.92
    
    if var_g > 0.04045: 
        var_g = ((var_g + 0.055) / 1.055) ** 2.4
    else:
        var_g = var_g / 12.92

    if var_b > 0.04045: 
        var_b = ((var_b + 0.055) / 1.055) ** 2.4
    else:
        var_b = var_b / 12.92

    var_r = var_r * 100
    var_g = var_g * 100
    var_b = var_b * 100

    val_x = var_r * 0.4124 + var_g * 0.3576 + var_b * 0.1805
    val_y = var_r * 0.2126 + var_g * 0.7152 + var_b * 0.0722
    val_z = var_r * 0.0193 + var_g * 0.1192 + var_b * 0.9505

    return val_x, val_y, val_z


def cielab_to_xyz(cie_l, cie_a, cie_b):
    """ TODO
    CIE-L*ab not Hunter
    """
    var_y = ( cie_l + 16. ) / 116.
    var_x = cie_a / 500. + var_y
    var_z = var_y - cie_b / 200.

    if var_y ** 3 > 0.008856:
        var_y = var_y ** 3
    else:
        var_y = (var_y - 16. / 116.) / 7.787
    if var_x ** 3 > 0.008856:
        var_x = var_x ** 3
    else:
        var_x = (var_x - 16. / 116.) / 7.787
        
    if var_z ** 3 > 0.008856:
        var_z = var_z ** 3
    else:
        var_z = (var_z - 16./ 116.) / 7.787

    # Observer= 2°, Illuminant= D65
    ref_x = 95.047
    ref_y = 100.000
    ref_z = 108.883
    
    val_x = ref_x * var_x
    val_y = ref_y * var_y
    val_z = ref_z * var_z
    
    return val_x, val_y, val_z


def xyz_to_cielab(val_x, val_y, val_z):
    """ TODO 
    CIE-L*ab not Hunter
    """
    # Observer= 2°, Illuminant= D65
    ref_x = 95.047
    ref_y = 100.000
    ref_z = 108.883

    var_x = val_x / ref_x
    var_y = val_y / ref_y
    var_z = val_z / ref_z

    if var_x > 0.008856:
        var_x = var_x ** (1. / 3.)
    else:
        var_x = 7.787 * var_x + 16. / 116.

    if var_y > 0.008856: 
        var_y = var_y ** (1. / 3.)
    else:
        var_y = 7.787 * var_y + 16. / 116.

    if var_z > 0.008856:
        var_z = var_z ** (1. / 3.)
    else
        var_z = 7.787 * var_z + 16. / 116.

    cie_l = 116 * var_y - 16
    cie_a = 500 * (var_x - var_y)
    cie_b = 200 * (var_y - var_z)

    return cie_l, cie_a, cie_b


def sol_from_base():
    pass

