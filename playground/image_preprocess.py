from PIL import Image
import hashlib
import os
import sys

# need to make the directories ourselves first
input_dir = "./cats/"
output_dir = "./cats_resized/"

def get_file_hash(input_path):
    # BUF_SIZE is totally arbitrary, change for your app!
    BUF_SIZE = 65536  # lets read stuff in 64kb chunks!
    sha256 = hashlib.sha256()

    with open(input_path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)

    return sha256.hexdigest()

def process_img(img, output_path):
    # if the image is too oblong, then it probably isn't a single dog
    width, height = img.size
    if width > height*2 or height > width*2:
        return

    img = img.convert("RGB")

    # make square by padding with white pixels
    new_size = max(width, height)
    out_img = Image.new("RGB", size=(new_size, new_size), color=(255, 255, 255))
    out_img.paste(img, (int(new_size-width)//2, int(new_size-height)//2))  # center

    # resize to 256x256
    out_img = out_img.resize((256, 256))
    out_img.save(output_path, 'PNG')


seen_hashes = set()
num_processed = 0

for filename in os.listdir(input_dir):
    num_processed += 1
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith("jpeg"):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        file_hash = get_file_hash(input_path)

        if file_hash not in seen_hashes:
            seen_hashes.add(file_hash)
            with Image.open(input_path) as img:
                process_img(img, output_path)