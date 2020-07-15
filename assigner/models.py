from django.contrib.postgres.fields import ArrayField
from django.db import models

class AssignedList(models.Model):
    name = models.CharField(max_length=200)
    assigned = ArrayField(
        models.TextField(blank=True),
        size=10
    )

    def __str__(self):
        return self.name
    