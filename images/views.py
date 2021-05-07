from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

import requests
from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    context = {'hey': 'hola'}
    return render(request, 'images/index.html', context)

@csrf_exempt
def get_images(request):
    
    image1 = getNewImage()
    image2 = getNewImage()

    reponse = {
        'image1': image1,
        'image2': image2,
    }
    return JsonResponse(reponse)



def getNewImage():
    page = requests.get('https://commons.wikimedia.org/wiki/Special:Random/File')

    soup = BeautifulSoup(page.content, 'html.parser')
    try:
        image = soup.select('.mw-thumbnail-link')[0]
        href = image.get('href')
    except:
        href = getNewImage()
    return href
