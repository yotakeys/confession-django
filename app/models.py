from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError

# Create your models here.


class Confession(models.Model):
    slug = models.CharField(max_length=30, primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    message = models.TextField(null=False, blank=False)

    answer = models.BooleanField(null=True, blank=False)
    response = models.TextField(null=True, blank=True)

    create = models.DateTimeField(auto_now_add=True)
    answer_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.slug

    class Meta:
        ordering = ['create']

    def clean(self):
        # data from the form is fetched using super function
        super(Confession, self).clean()
        slug = self.slug
        # conditions to be met for the username length
        if ' ' in slug:
            raise ValidationError('Slug is not allowed to contain spaces')

        return self
