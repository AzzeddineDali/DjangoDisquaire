from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Album, Artist, Booking, Contact


def index(request):
    albums = Album.objects.filter(available=True).order_by('-created_at')[:10]
    context = {
        'albums': albums
    }
    return render(request, 'store/index.html', context)


def listing(request):
    albums = Album.objects.filter(available=True)
    context = {
        'albums': albums
    }
    return render(request, 'store/listing.html', context)


def detail(request, album_id):
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artists.all()])
    artists_name = "".join(artists)
    context = {
        'album_title': album.title,
        'artists_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.image

    }
    return render(request, 'store/detail.html', context)


def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
            albums = Album.objects.filter(artists__name__icontains=query)

    title = "Résultats pour la requête %s" % query
    context = {
        'albums': albums,
        'title': title
    }

    return render(request, 'store/search.html', context)

