from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from .models import Photo, Category, Location

# Create your views here.

def index(request):
    photos = Photo.objects.all()
    locations = Location.objects.all()
    return render (request, 'index.html',{'photos':photos, 'locations':locations})

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You have not entered what to search"
        return render(request, 'search.html',{"message":message})

def show_location(request, location_id):
    try:
        locations = Location.objects.all()
        location = Location.objects.get(id=location_id)
        photos = Photo.Objects.filter(location = location.id)
    except:
        raise Http404()

        return render(request, 'location.html', {'location':location, 'photos':photos, 'locations':locations})

