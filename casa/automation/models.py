from django.db import models

# Create your models here.


class ActiveManager(models.Manager):
    def get_active(self):
        return self.filter(
            is_active=True
        )


class SubNav(models.Model):
    title = models.CharField(max_length=65)
    url = models.CharField(max_length=65)
    icon = models.CharField(max_length=40)
    is_active = models.BooleanField(default=False)

    objects = ActiveManager()


class SubNavContent(models.Model):
    title = models.CharField(max_length=65)
    content = models.TextField()
    subcontent = models.TextField()
    function_button = models.CharField(max_length=65, blank=True)
    is_active = models.BooleanField(default=False)

    objects = ActiveManager()


class Banner(models.Model):
    title = models.CharField(max_length=150)
    title_highlight = models.CharField(max_length=150, blank=True)
    title_finish = models.CharField(max_length=150, blank=True)
    subtitle = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)

    objects = ActiveManager()
