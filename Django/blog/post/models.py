from django.db import models
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=120, verbose_name="Başlık")      # Max_lengt belirtilmek zorundaymış.
    text = models.TextField(verbose_name="Metin")
    published_date = models.DateTimeField(verbose_name="Yayınlanma Tarihi")     #verbose_name="Yayınlanma Tarihi"
                                                                                # değişkeniyle orada görünmesini                                                          # istediğimiz ismi söylemiş olduk

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})
        #return "/post/{}".format(self.id)


# Create your models here.
