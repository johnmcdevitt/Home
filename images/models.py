from django.db import models

# imports for foreign keys
from house.models import Room
from todos.models import ToDo

# Create your models here.
# create Image model
class Image(models.Model):
    image_type_choices = (
        ('b', 'Before'),
        ('i', 'Inspiration'),
        ('a', 'After'),
        ('p', 'To Do'),
    )

    image = models.ImageField(upload_to="uploads/images/")
    image_type = models.CharField(max_length=1,
                                  choices=image_type_choices)
    # TODO only make foreign key fields available by image type
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE, blank=True)
    todo = models.ForeignKey(ToDo, null=True, on_delete=models.CASCADE, blank=True)
