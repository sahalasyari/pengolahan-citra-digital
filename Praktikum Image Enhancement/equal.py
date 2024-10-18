import imageio as img
import numpy as np
import matplotlib.pyplot as plt

def blend(image1,op1,image2,op2):
    img1 = image1.astype(np.float32)
    img2 = image2.astype(np.float32)
    imgBlend = (img1*op1) + (img2*op2)
    imgBlend = np.clip (imgBlend,0,255)
    return imgBlend.astype (np.uint8)

img1 = img.imread ("C:\Users\sahal\pcd\image.jpg")
img2 = img.imread ("C:\Users\sahal\pcd\pngtree-blue-and-purple-neon-star-3d-art-background-with-a-cool-image_3705286.jpg")


imgBlend =blend (img1,0,3,img2,0.7)

plt.figure (figsize=(10,10))
plt.subplot (3,2,1)
plt.imshow(img1)
plt.subplot(3,2,3)
plt.imshow(img2)
plt.subplot(3,2,5)
plt.imshow(imgBlend)
plt.show()
