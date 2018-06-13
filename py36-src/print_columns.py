#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from math import sin

t0 = 2
dt = 0.55

t = t0 + 0*dt; g = t*sin(t)
print('{:6.2f} {:8.3f}'.format(t, g))

t = t0 + 1*dt; g = t*sin(t)
print('{:6.2f} {:8.3f}'.format(t, g))

t = t0 + 2*dt; g = t*sin(t)
print('{:6.2f} {:8.3f}'.format(t, g))

print("""hei1
      hei2 {}
      hei3   {}                     hei4
      yes!""".format(t, g))