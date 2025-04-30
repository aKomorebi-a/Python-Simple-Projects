import imageio.v3 as iio

filenames = ['nyan-cat1.png', 'nyan-cat2.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('nyacat.gif', images, duration=500, loop=0)

# la dependencia tiene un error
