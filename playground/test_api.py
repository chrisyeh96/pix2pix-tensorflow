from PIL import Image
from io import BytesIO
import requests


# edges_img_path = "known_edges/cats1.png"
# edges_img_path = "known_edges/cats2.png"
# edges_img_path = "known_edges/cats3.png"
# edges_img_path = "known_edges/cats4.png"
# edges_img_path = "known_edges/cats5.png"
# edges_img_path = "known_edges/dogs1.png"
# edges_img_path = "known_edges/dogs2.png"
edges_img_path = "known_edges/dogs3.png"
# edges_img_path = "known_edges/dogs4.png"
# edges_img_path = "known_edges/dogs5.png"
# edges_img_path = "dogs_edges/white.png"


with open(edges_img_path, "rb") as edges_rgb:
    processed_png = edges_rgb.read()

data = processed_png


##########################################

# url = "https://cors-anywhere.herokuapp.com/" + "https://pix2pix.affinelayer.com/edges2cats_AtoB"
# url = "https://pix2pix.affinelayer.com/edges2cats_AtoB"
# url = "http://13.92.99.130:7000/edges2cats_AtoB"
url = "http://13.92.99.130:7000/x"
# url = "http://13.92.99.130:7000/edges2dogs2"
headers = {
    'Content-Type': 'image/png'
}

r = requests.post(url=url, data=data, headers=headers)
print(r.content)
img = Image.open(BytesIO(r.content))
img.show()

##########################################

# url = "https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/a9ac2db7-7ee1-4e17-8547-62b52e7fb516/image?iterationId=81da5c82-ac79-43be-8c15-c4265e8cdd62"
# headers = {
#     "Prediction-Key": "34f2036b4dc0448f92b4d76d12cba35c",
#     "Content-Type": "application/octet-stream"
# }

# import json
# from pprint import pprint

# r = requests.post(url=url, data=data, headers=headers)
# response = json.loads(r.text)

# tags_to_probs = {}
# best_tag = None
# max_prob = 0

# for tag in response["Predictions"]:
#     tag_name = tag["Tag"]
#     prob = tag["Probability"]
#     tags_to_probs[tag_name] = prob
    
#     if prob > max_prob:
#         max_prob = prob
#         best_tag = tag_name

# pprint(tags_to_probs)