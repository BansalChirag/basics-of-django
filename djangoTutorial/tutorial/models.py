from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('Masala', 'Masala Chai'), 
        ('Ginger', 'Ginger Chai'),
        ('Lemon', 'Lemon Chai'),
        ('Plain', 'Plain Chai'),]
    name = models.CharField(max_length=100)
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(upload_to='chai_images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=50,choices=CHAI_TYPE_CHOICE,default='Plain')

    def __str__(self):
        return self.name

# one to many relationship 
class ChaiReview(models.Model):
    chai_variety = models.ForeignKey(ChaiVariety, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Review for {self.chai_variety.name} by {self.user.username}'
    


# Many to Many relationship

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    chai_varieties = models.ManyToManyField(ChaiVariety, related_name='stores') # dusre table me kis name se jana jau

    def __str__(self):
        return self.name


# one to one relationship

class ChaiCertificate(models.Model):
    chai_variety = models.OneToOneField(ChaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=50)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai_variety.name} - {self.certificate_number}'
