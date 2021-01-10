import os
from PIL import Image
import cv2
import numpy as np
import sys

faceCascade = cv2.CascadeClassifier("extra/images/haar_cascade.xml")

def face_detect(img):
  img = np.array(img)[:, :, ::-1].copy()
  img_height, img_width, _ = img.shape
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

  faces = faceCascade.detectMultiScale(
      gray,
      scaleFactor=1.1,
      minNeighbors=5,
      minSize=(30, 30),
      flags=cv2.CASCADE_SCALE_IMAGE
  )

  best_face = None
  # Draw a rectangle around the faces
  for face in faces:
    if best_face is None or best_face[2] < face[2]:
      best_face = face

  if best_face is not None:
    shift = 0.5
    x, y, w, h = best_face

    # # Draw rectangle
    #cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    x1 = max(0, int(x - shift*w))
    x2 = min(img_width, int(x + (1+shift)*w))
    y1 = max(0, int(y - shift*h))
    y2 = min(img_height, int(y + (1+shift)*h))
    img = img[y1:y2, x1:x2]

  return Image.fromarray(img[:, :, ::-1])


src_dir = 'people/'
tgt_dir = "src/assets/people/"
for filename in os.listdir(src_dir):
    im = Image.open(src_dir + filename)
    im = im.convert("RGB")

    im = face_detect(im)


    width, height = im.size   # Get dimensions
    if width != height:
      dim = min(width, height)
      left = (width - dim)/2
      top = (height - dim)/2
      right = (width + dim)/2
      bottom = (height + dim)/2

      # Crop the center of the image
      im = im.crop((left, top, right, bottom))

    print(filename)
    size = (512, 512) if "ido_dagan" in filename or "yoav_goldberg" in filename or "reut_tsarfaty" in filename else (256, 256)

    im.thumbnail(size, Image.ANTIALIAS)

    new_name = filename.split(".")[0] + ".jpg"


    im.save(tgt_dir + new_name, "JPEG")
