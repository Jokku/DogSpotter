from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

from math import radians, sin, cos, acos

import numpy as np
import requests

from django.http import HttpResponse
from .models import File, FileUpload
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .dog1 import executeUpload

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.template import RequestContext
from django.template import Context
from django.shortcuts import render_to_response
from django import forms
from django.http import HttpResponseRedirect

from django.template.response import TemplateResponse
from django.http import JsonResponse
# import requests
import urllib.request
import  os

from selenium import webdriver

# for Splash
from queue import Queue, Empty
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin, urlparse

from geopy.geocoders import Nominatim
geolocator = Nominatim()

def index(request):
    html = '<h1>This is the Page</h1>'
    return HttpResponse(html)

#forClientIPUse request.META.get('REMOTE_ADDR')

def detail(request, file_id):
    # try:
    #     f1=File.objects.get(id=file_id)
    # except File.DoesNotExist:
    #     raise Http404("Does Not Exist")

    f1=get_object_or_404(File,id=file_id)
    # This one is the shortcut

    all_files=File.objects.all()
    # html=''
    # for f in all_files:
    #     url='/fileupload/'+str(f.id)+'/'
    #     html += '<a href="'+f.filename+'">'+f.filename+'</a><br>'
    template = loader.get_template('fileupload/index.html')
    context = {
        'all_files':all_files,
    }
    return HttpResponse(template.render(context, request))
    # return render(request,'fileupload/index.html',context)


def uploading(request , fileid):
    # fileupload = get_object_or_404(FileUpload, fileid)
    my_object = FileUpload.objects.get(id=fileid)
    value = executeUpload(my_object.image.path)
    #FileUpload.objects.model(id=fileid).clean()
    #path = my_object.image.url
    #my_object.image.delete()

    # uploaded = FileUpload.objects.filter(id=kwargs.items(0))
    return HttpResponse("<img src='"+my_object.image.url+"'><br><h1>"+value+"</h1>")
    # print(project_id)

# def uploadprocess(request):
#     if request.method == 'POST':
#         image = request.POST['data']
#
#         FileUpload.objects.create(
#             image = image
#         )
#     return HttpResponse('')

def uploadprocess(request):
    if request.method == 'POST':
        image = request.FILES['image']
        lat = request.POST.get('lat')
        lng = request.POST.get('lng')



        print('Latitde:'+lat+' Longitde:'+lng)

        # image = request.FILES['https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg']
        # url = 'https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg'
        # path = os.path.abspath('C:/Users/CsKJsK/Desktop/dogspotter/a.jpg')
        # image = urllib.request.urlretrieve(url)
        # url = "https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg"
        # image=requests.get(url)

        f = FileUpload(image=image)
        f.save()
        # mylist = ['item 1', 'item 2', 'item 3']
        # c = {'mylist': mylist}
        # return render_to_response('fileupload/fileupload_form.html', c)
        value = executeUpload(f.image.path)
        # value = executeUpload('https://i.ytimg.com/vi/SfLV8hD7zX4/maxresdefault.jpg')
        # c=RequestContext(request, {'foo': 'bar', })
        # return render_to_response('fileupload/fileupload_form.html', c)
        # return HttpResponse('')
        # return render_to_response('fileupload/fileupload_form.html', RequestContext(request))
        # class FileUploadd(CreateView):
        #     model = FileUpload
        #     fields = ['image']
        # template = loader.get_template('fileupload/index.html')
        # all_files = File.objects.all()
        # context = {
        #     'all_files': all_files,
        # }
        # return HttpResponse(template.render(context, request))
    # context = "hhh"
    # return render(request, 'fileupload/fileupload_form.html',{"context": context})
    template = loader.get_template('fileupload/fileupload_form.html')
    context = Context({'context': 'jokku'})
    # return HttpResponse("<img src='" + f.image.url + "'>")
    # return HttpResponse(template.render(context))
    # return TemplateResponse(request,'fileupload/fileupload_form.html', {'context': 'jokku'} )

    my_url = "https://www.gumtree.com.au/s-dogs-puppies/" + value +"/k0c18434"
    my_url = my_url.replace(" ","+")
    print(my_url)
    #uClient = urlopen(my_url)

    #page_html = uClient.read()

    #uClient.close()
    # HTML parsing
    # page_soup = soup(page_html, "html.parser")




    # page_soup = soup(page_html, "html5lib")
    # page = requests.get(my_url,)
    # page_soup = soup(page.content, "html.parser")




    res = requests.get(my_url)
    print(res.text)
    page_soup = soup(res.text, "html.parser")
    container = page_soup.find_all("a", {"class": "user-ad-row"})

    print("container len")
    print(len(container))
    # Creates a list containing len(container) number of lists, each of 8 items, all set to 0
    w, h = 8, len(container);
    Matrix = [[0 for x in range(w)] for y in range(h)]
    i=0;

    # Google API
    # from geolocation.main import GoogleMaps

    # google_maps = GoogleMaps(api_key='AIzaSyDNHpu2_7QvJH5rvGRZN0F69r-GnAnlfFU')
    # location = google_maps.search(location)  # search for our location.

    # my_location = location.first()  # returns only first location.
    # print(my_location.lat)
    # print(my_location.lng)




    for contain in container:
        ad_title = contain.p.text
        price = contain.span.text
        postedDate = contain.find("p", {"class": "user-ad-row__age"}).text
        fullArea = contain.find("div", {"class": "user-ad-row__location"}).text.strip()
        city = contain.find("span", {"class": "user-ad-row__location-area"}).text
        suburb = fullArea.replace(city, "")
        try:
            imgPath = contain.find("img", {"class": "user-ad-row__image"})["src"]
        except:
            imgPath = "Image is not available"
        pathToOpen = "https://www.gumtree.com.au" + contain["href"]

        Matrix[i][1] = ad_title
        Matrix[i][2] = price
        Matrix[i][3] = postedDate
        Matrix[i][4] = city
        Matrix[i][5] = suburb
        Matrix[i][6] = imgPath
        Matrix[i][7] = pathToOpen

        location = geolocator.geocode(suburb + ", Australia")

        slat = radians(float(lat))
        slon = radians(float(lng))
        elat = radians(float(location.latitude))
        elon = radians(float(location.longitude))

        dist = 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))
        dist = np.round(dist,1)
        Matrix[i][0] = dist
        i=i+1
        if i == 6:
            break
        #Matrix = sorted(Matrix, key=lambda x: x[0])

    return JsonResponse({'context': value, 'path': f.image.url, 'Matrix': Matrix, 'url': my_url})

def upload(request):
    template = loader.get_template('fileupload/fileupload_form.html')
    return render(request, 'fileupload/fileupload_form.html')