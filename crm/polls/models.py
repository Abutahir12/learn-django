from django.db import models


# Create your models here.
class Dev(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    organisation = models.CharField(max_length=128)
    address = models.TextField()
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(null=True, blank=True, max_length=128)
    updated_at = models.DateTimeField(null=True, default=None, blank=True)
    updated_by = models.CharField(null=True, blank=True, max_length=128)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
