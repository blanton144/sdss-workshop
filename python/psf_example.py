from matplotlib import pyplot 

center= 20.
peak1= 0.75
width1= 3.
peak2= 0.25
width2= 6.

xx= numpy.arange(40,dtype='float32')
yy1= peak1*numpy.exp(-0.5*((xx-center)/width1)**2)
yy2= peak2*numpy.exp(-0.5*((xx-center)/width2)**2)
yy= yy1+yy2

pyplot.plot(xx, yy, color='black', linewidth=2)
pyplot.ylim(-0.05, 1.05)
pyplot.xlabel('pixel')
pyplot.ylabel('flux')
pyplot.plot(xx, yy1, color='red', linestyle=':', linewidth=2)
pyplot.plot(xx, yy2, color='green', linestyle=':', linewidth=2)
pyplot.savefig('gaussian.pdf', format='pdf')
pyplot.close()

