# coding=utf-8
from django.db import models

class Teg(models.Model):
    name = models.CharField(max_length=20)