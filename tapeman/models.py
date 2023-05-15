from django.db import models

# Create your models here.


class Library(models.Model):
    hostname = models.CharField(max_length=16, unique=True)
    management_ip = models.GenericIPAddressField(protocol="IPv4", unique=True)
    slots = models.IntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return self.hostname


class TapePool(models.Model):
    name = models.CharField(max_length=16, unique=True)
    library = models.ForeignKey(Library, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Tape(models.Model):
    barcode = models.CharField(max_length=16, unique=False)
    capacity = models.FloatField(max_length=8, blank=True, null=True)
    pool = models.ForeignKey(TapePool, on_delete=models.CASCADE, blank=True, null=True)
    full = models.BooleanField()
    data_expiration = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.barcode
