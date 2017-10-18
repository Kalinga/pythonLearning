import matplotlib.pyplot as plt
from skimage import io

baseUrl = "http://www.comicsmanics.com/wp-content/uploads/2017/01/"
suffix = "-2-1024x819.jpg"

for i in range(120, 121):
#for i in range(1, 2):
    print str(i).zfill(3)
    finalUrl = baseUrl + str(i).zfill(3) + suffix
    print finalUrl

    image = io.imread(finalUrl)
    io.imsave(str(i)+".jpg", image)

    #fig1 = plt.figure()  # create a figure with the default size
    #ax1 = fig1.add_subplot(2, 2, 1)
    #ax1.imshow(image, aspect='equal')
    #plt.show()

    #io.imshow(image)