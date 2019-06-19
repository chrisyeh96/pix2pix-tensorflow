from PIL import Image, ImageOps
import PIL.ImageOps
import base64
from io import BytesIO

# RGBA image
input_sketch = Image.open("input_image.png")

# convert to single grayscale channel
input_sketch_gray = input_sketch.convert("L")

# set the gray background color to be white
img_arr = input_sketch_gray.load()
width, height = input_sketch_gray.size
for y in range(height):
    for x in range(width):
        if img_arr[x, y] == 192:
            img_arr[x, y] = 255

# set the darkest color to black, brightest to white
edges_gray = ImageOps.autocontrast(input_sketch_gray, cutoff=0, ignore=None)

# invert colors => black background, white edges
inverted_edges_gray = ImageOps.invert(edges_gray)

# convert back to RGB
inverted_edges_rgb = inverted_edges_gray.convert("RGB")


            mem_buffer = BytesIO()
            inverted_edges_gray.save(mem_buffer, format="PNG")
            input_b64data = base64.urlsafe_b64encode(mem_buffer.getvalue())

print(input_b64data)