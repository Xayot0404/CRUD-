from django.db import models


class CRUDmodel(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "crud"
