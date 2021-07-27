from PIL import Image

def resize_image(img, dimensions):
	image= Image.open(img)
	image.thumbnail(dimensions,Image.ANTIALIAS)
	return image