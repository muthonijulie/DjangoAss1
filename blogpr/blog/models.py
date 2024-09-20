from django.db import models # type: ignore

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField(max_length=600)
    author=models.CharField(max_length=100)
    date_created =models.DateField()
    image=models.ImageField(upload_to='media/images',blank=True,null=True)

def __str__(self):
         return f"Title:{self.title}\nAuthor{self.author}\n{self.image}"
