from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from myapp.models import Song
import json

def save_date(request:HttpRequest):
    file_path='myapp/melon'
    with open(file_path,'r',encoding='utf-8') as json_file:
        data=json_file.load()
    for item in data:
        Song.objects.create(
            rank=item["곡일련번호"]
            album=item["앨범"]
            name=item["곡명"]
            singer=item["가수"]
            cover_image=item["커버이미지_주소"]
            lyric=item["가사"]
            genre=item["장르"]
            date=item["발매일"]
            good=item["좋아요"]
        )
    