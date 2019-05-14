from django.db import models
# from django.utils import timezone
# Create your models here.
class Blog(models.Model):
    title =  models.CharField(max_length=255)
    publication_date = models.DateTimeField()
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:60]
    def time(self):
        return self.publication_date.strftime('%b %e %Y')