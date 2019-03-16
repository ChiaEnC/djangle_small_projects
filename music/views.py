# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Album, Song

from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse


def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums,
    }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except(KeyError, Song.DoesNotExit):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "you did not select a valid song",
        })
    else:
        print(request.POST['song'])
        selected_song.is_favorite = True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})