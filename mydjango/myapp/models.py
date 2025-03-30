from django.db import models


class Singer(models.Model):
    singer=models.CharField(max_length=10)

class Song(models.Model):
    rank=models.IntegerField()
    album=models.CharField(max_length=50)
    name=models.CharField(max_length=30)
    singer=models.ForeignKey(Singer,on_delete=models.CASCADE)
    cover_image=models.URLField(blank=True)
    lyric=models.TextField()
    genre=models.CharField(max_length=15)
    date=models.DateField()
    good=models.IntegerField()