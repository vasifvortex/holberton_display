from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return self.title

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='events/') 
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image uploaded on {self.upload_date}"
