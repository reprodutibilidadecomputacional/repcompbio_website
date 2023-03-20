from django.db import models


class People(models.Model):
    public_name = models.CharField('public name', max_length=200)
    pronoums = models.CharField('pronoums', max_length=200)
    short_bio = models.TextField('short bio', max_length=2000)
    institution_name = models.CharField('institution', max_length=200)
    email_address = models.EmailField('email address', max_length=300)
    country = models.CharField('country', max_length=200)
    state = models.CharField('state', max_length=200)
    lattes = models.URLField('link to lattes', max_length=200,
                               null=True, blank=True)
    google_scholar = models.URLField('link to google scholar', max_length=200,
                               null=True, blank=True)
    twitter = models.URLField('link to twitter', max_length=200,
                               null=True, blank=True)
    instagram = models.URLField('link to instagram', max_length=200,
                               null=True, blank=True)
    facebook = models.URLField('link to facebook', max_length=200,
                               null=True, blank=True)
    linkedin = models.URLField('link to linkedin', max_length=200,
                               null=True, blank=True)

    def __str__(self):
        return self.public_name




