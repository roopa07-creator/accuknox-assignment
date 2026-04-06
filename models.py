from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=100)

    def _str_(self):
        return self.name