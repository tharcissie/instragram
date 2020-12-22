from django.db import models

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-pk"]

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


    def __str__(self):
        return self.name

