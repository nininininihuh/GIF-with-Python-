import imageio.v3 as iio
filenm=['team-pic1.png','team-pic2.png']
imgs=[]
for file in filenm:
  imgs.append(iio.imread(file))
iio.imwrite('team.gif', imgs, duration = 500, loop=0)
#loop = 0 means that it will keep looping until and unless external change.




