from matplotlib import pyplot 
import scipy.interpolate  as interpolate
import scipy.ndimage  as ndimage

frame= pyfits.open('frame-u-000752-3-0090.fits')
image= frame[0].data

sky= frame[2].data
xinterp=sky[0].field('xinterp')
yinterp=sky[0].field('yinterp')
allsky=numpy.array(sky[0].field('allsky'))
nx= len(xinterp)
ny= len(yinterp)
xall= numpy.outer(numpy.ones(ny, dtype='float32'), xinterp)
yall= numpy.outer(yinterp, numpy.ones(nx, dtype='float32'))
xy= ([yall.flatten(), xall.flatten()])
skyinterp= numpy.reshape(ndimage.map_coordinates(allsky, xy), [ny, nx], 
                         mode='nearest')
