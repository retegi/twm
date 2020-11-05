from django.db import models

# Create your models here.
class Post(models.Model):
    title_post = models.CharField('Título', max_length=400, null=True,blank=True)
    text_post = models.TextField('Texto', max_length=1000, null=True,blank=True)
    link_post = models.CharField('Enlace', max_length=500, null=True, blank=True)
    date_post = models.DateTimeField('Fecha',null=True, blank=True)
    author_post = models.CharField('Autor', max_length=20,null=True, blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural= 'Post'
        ordering = ['date_post']

    def __str__(self):
        return self.link_post