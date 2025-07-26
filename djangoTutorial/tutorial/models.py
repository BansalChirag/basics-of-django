from django.db import models
from django.utils import timezone
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
