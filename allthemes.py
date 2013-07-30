#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os

# settings
themes = ['AnnArbor',
          'Antibes',
          'Bergen',
          'Berkeley',
          'Berlin',
          'Boadilla',
          'boxes',
          'CambridgeUS',
          'Copenhagen',
          'Darmstadt',
          'default',
          'Dresden',
          'Frankfurt',
          'Goettingen',
          'Hannover',
          'Ilmenau',
          'JuanLesPins',
          'Luebeck',
          'Madrid',
          'Malmoe',
          'Marburg',
          'Montpellier',
          'PaloAlto',
          'Pittsburgh',
          'Rochester',
          'Singapore',
          'Szeged',
          'Warsaw'
          ]
path_tex = "testtalk.tex"
mytheme = "Frankfurt"

for theme in themes:
    path_cur = path_tex[:-4] + "_" + theme + path_tex[-4:]
    os.system("cp " + path_tex + " " + path_cur)
    os.system("sed -i 's/" + mytheme + "/" + theme + "/g' " + path_cur)
    os.system("xelatex " + path_cur)
    os.system("rm " + path_cur[:-4] + ".aux")
    os.system("rm " + path_cur[:-4] + ".log")
    os.system("rm " + path_cur[:-4] + ".nav")
    os.system("rm " + path_cur[:-4] + ".out")
    os.system("rm " + path_cur[:-4] + ".snm")
    os.system("rm " + path_cur[:-4] + ".toc")
