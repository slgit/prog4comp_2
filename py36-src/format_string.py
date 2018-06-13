time = 1.0
height = 4.0

# printf syntax (for comparison)
print 'At t=%g s, y=%.2f m' % (time, height)   

# format string syntax
print 'At t={t:g} s, y={y:.2f} m'.format(t=time, y=height)

# format string syntax
print 'At t={t:g} s, y={y:.2f} m'.format(y=height, t=time)
