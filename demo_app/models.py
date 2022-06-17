from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length= 100)
    dob = models.DateField(max_length = 100)
    address = models.CharField(max_length=100)
    photo = models.ImageField(null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    user = models.CharField(max_length = 100)
    conent = models.CharField(max_length=1000)
    date_posted = models.DateField()
    no_likes = models.IntegerField()
    photo = models.ImageField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

class Theme(models.Model):
    name = models.CharField(max_length=30)
    article = models.ManyToManyField(Article)

class Comics(models.Model):
    brand = models.CharField(max_length= 40)
    no_pages = models.IntegerField()
    price = models.FloatField()




