import numpy as np
from PIL import Image

image_name = 'img.jpg'
image = Image.open(image_name)
image_np = np.array(image)
image_np_conv = image_np
image_np_conv += 50
new_image = Image.fromarray(image_np_conv.astype('uint8'))
save_name = 'img_conv.jpg'
new_image.save(save_name)
