from PIL import Image, ImageOps
import PIL.ImageOps
from io import BytesIO
import base64
import json
from pprint import pprint
import requests

def classify_cat_vs_dog(sketch_png):
    '''
    Args
        sketch_png: bytes, output of process_received_img

    Returns
        str, the predicted label (either 'cat' or 'dog')
    '''
    url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/a9ac2db7-7ee1-4e17-8547-62b52e7fb516/image?iterationId=81da5c82-ac79-43be-8c15-c4265e8cdd62"
    headers = {
        "Prediction-Key": "34f2036b4dc0448f92b4d76d12cba35c",
        "Content-Type": "application/octet-stream"
    }

    r = requests.post(url=url, data=sketch_png, headers=headers)
    response = json.loads(r.text)

    tags_to_probs = {}
    best_tag = None
    max_prob = 0

    for tag in response["Predictions"]:
        tag_name = tag["Tag"]
        prob = tag["Probability"]
        tags_to_probs[tag_name] = prob
        
        if prob > max_prob:
            max_prob = prob
            best_tag = tag_name

    pprint(tags_to_probs)
    print("best tag: %s" % best_tag)
    return best_tag

def process_received_img(input_data):
    # write input image to file
    # save_path = "input_image.png"
    # with open(save_path, "wb") as input_png:
    #     input_png.write(input_data)

    # RGBA image
    input_sketch = Image.open(BytesIO(input_data))

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
    # now, the background is white, edges are black
    edges_gray = ImageOps.autocontrast(input_sketch_gray, cutoff=0, ignore=None)

    # convert back to RGB
    edges_rgb = edges_gray.convert("RGB")

    mem_buffer = BytesIO()
    edges_rgb.save(mem_buffer, format="PNG")
    return mem_buffer.getvalue()

def pngdata_to_base64(png_data):
    # convert image to base64 string
    input_b64data = base64.urlsafe_b64encode(png_data)
    return input_b64data