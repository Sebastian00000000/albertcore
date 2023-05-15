from typing import Any
from django.db import models

# Create your models here.
class Region(models.Model):
    def __init__(self, name) -> None:
        self.name = name
        
    def __str__(self) -> str:
        return self.name