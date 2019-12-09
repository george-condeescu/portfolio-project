from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=255)
    pub_data=models.DateTimeField()
    body=models.TextField()
    image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]
    
    def pub_data_pretty(self):
        return self.pub_data.strftime('%b %e %Y')
