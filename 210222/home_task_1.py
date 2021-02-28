import numpy as np
from PIL import Image

image_name = 'img.jpg'
image = Image.open(image_name)
image_np = np.array(image)
# print(image_np.size, image_np.shape)
# print(image_np) # uint8 -> 0..255
image_np_conv = image_np
image_np_conv = image_np  + 20
# image_np_conv[:, :, 0] = 255
# image_np_conv[:, :, 1] = 127
# print(image_np[:, :, 0].mean(), image_np[:, :, 1].mean(),
# image_np[:, :, 2].mean())
# print(image_np_conv[:, :, 0].mean(), image_np_conv[:, :, 1].mean(),
# image_np_conv[:, :, 2].mean())

new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'img_conv.jpg'
new_image.save(save_name)