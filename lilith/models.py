from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Comentario(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=False, blank=False, on_delete=models.CASCADE,default=settings.AUTH_USER_MODEL)
    text = models.TextField(verbose_name='Text', max_length=200, null=False, blank=False)
    create = models.DateTimeField(auto_now_add=True, null=False)
    update = models.DateTimeField(auto_now=True, null=False)
    
    class Meta:
        ordering = ['-create']
    
    def __str__(self) -> str:
        return str(self.user)
    

class Noticia(models.Model):
    manchete = models.CharField(max_length=200)
    materia = models.CharField(max_length=1000)
    link_imagem = models.URLField
    imagem = models.ImageField
    autor = models.CharField(max_length=200)
    data = models.DateTimeField
    categoria = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'Notícias'
        verbose_name = 'Notícia'
    
    def __str__(self) -> str:
        return self.manchete


class Video(models.Model):
    titulo = models.CharField(max_length=200)
    link_video = models.URLField
    thumbnail = models.ImageField
    descricao = models.CharField(max_length=500)
    data = models.DateTimeField
    autor = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Vídeos'
        verbose_name = 'Vídeo'

    def __str__(self) -> str:
        return self.titulo
