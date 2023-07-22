from django.db import models
from django.contrib.auth.models import User
from django.forms import ValidationError
from datetime import datetime

# Create your models here.


class Confession(models.Model):

    answer_choices = (
        ('YES', 'Yes'),
        ('NO', 'No'),
        ('IDK', "I don't know what to say"),
        ('IWT', "I Will Think About It"),
    )

    slug = models.CharField(max_length=64, primary_key=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    sender = models.CharField(max_length=30, null=False, blank=False)
    target = models.CharField(max_length=30, null=False, blank=False)
    title = models.CharField(max_length=30, null=False, blank=False)
    message = models.TextField(null=False, blank=False)

    answer = models.CharField(choices=answer_choices, max_length=30)
    response = models.TextField(null=True, blank=True)
    is_answerred = models.BooleanField(default=False)

    create = models.DateTimeField(default=datetime.now())
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

        def has_invalid_characters(url_string):
            invalid_url_characters = [
                " ", "<", ">", "#", "%", "{", "}", "|", "\\", "^", "~",
                "[", "]", "`", "\"", "'", ";", "?", ":", "@", "=", "&"
            ]

            for char in url_string:
                if char in invalid_url_characters:
                    return True

            return False
        if has_invalid_characters(slug):
            raise ValidationError('Slug contains invalid characters')

        return self
