from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class user_details(models.Model):
    
    name = models.TextField(max_length=10 ,null=False,blank=False)
    password = models.CharField(max_length=8, default='12345678')
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    
class Movie(models.Model):
    
    #imdbID = models.TextField(default='none')
    title = models.TextField(_("title"),null=False,blank=False)
    year = models.IntegerField(_("releaseYear"),default =2000)
    genre = models.TextField(_("genre"),default='none',null=False,blank=False)
    actors = models.TextField(_("actors"),default='none' ,null=False,blank=False)
    hitFlop = models.IntegerField(_("hitFlop"),default=0,null=False,blank=False)

    def __str__(self):
        return self.title

class Song(models.Model):
    
    #imdbID = models.TextField(default='none')
    title = models.TextField(_("title"),null=False,blank=False)
    singer = models.TextField(_("singer"),default='none',null=False,blank=False)
    genre = models.TextField(_("genre"),default='none',null=False,blank=False)
    album = models.TextField(_("album"),default='none' ,null=False,blank=False)
    user_rating = models.DecimalField(_("user_rating"),default=0.0,null=False,blank=False,decimal_places=2,max_digits=4)

    def __str__(self):
        return self.title
