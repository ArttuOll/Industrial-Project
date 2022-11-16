from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import numpy as np

def tiff(request):
    images = []
    img = Image.open('multipage.tiff')
    for page in range(img.n_frames):
        try:
            img.seek(page)
            images.append(np.array(img))
        except EOFError:
            break

    png_images = []
    for img in images:
        png_image = Image.fromarray(img.astype(np.uint8))
        png_images.append(png_image)
    return HttpResponse(png_images, status=200)
