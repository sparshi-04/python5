# -*- coding: utf-8 -*-
"""Q4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dQEtbSwASCl_HKdFV46Ssy3JPFyoomMY
"""

from operator import itemgetter
list = [('paratha', 150), ('pasta', 189), ('coffee', 100),('wrap', 210)]
sort_list = sorted(list, key=itemgetter(1), reverse = True)
print(sort_list)