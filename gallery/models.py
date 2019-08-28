from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    @classmethod
    def delete_location(cls,name):
        cls.objects.filter(name = name).delete()

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos')
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default='LOCATION')



    def save_photo(self):
        self.save()

    @classmethod
    def search_by_category(cls,search_term):
        photo = cls.objects.filter(category__name__icontains = search_term)
        return photo