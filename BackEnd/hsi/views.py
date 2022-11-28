from django.shortcuts import render
from django.http import HttpResponse
from PIL import Image
import numpy as np
import io

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
    for img_arr in images:
        png_buffer = io.BytesIO()
        image = Image.fromarray(img_arr)
        image.save(png_buffer, format='png')
        png_images.append(png_buffer.seek(0))
    return HttpResponse(png_images, status=200)

def one_png(request):
    images = []
    img = Image.open('multipage.tiff')
    for page in range(img.n_frames):
        try:
            img.seek(page)
            images.append(np.array(img))
        except EOFError:
            break

    png_images = []
    for img_arr in images:
        png_buffer = io.BytesIO()
        image = Image.fromarray(img_arr)
        image.save(png_buffer, format='png')
        png_images.append(png_buffer.seek(0))
    return HttpResponse(png_images[0], status=200)
