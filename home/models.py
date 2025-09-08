# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Gyártó(models.Model):

    #__Gyártó_FIELDS__
    név = models.CharField(max_length=255, null=True, blank=True)

    #__Gyártó_FIELDS__END

    class Meta:
        verbose_name        = _("Gyártó")
        verbose_name_plural = _("Gyártó")


class Típus(models.Model):

    #__Típus_FIELDS__
    név = models.TextField(max_length=255, null=True, blank=True)

    #__Típus_FIELDS__END

    class Meta:
        verbose_name        = _("Típus")
        verbose_name_plural = _("Típus")


class Altípus(models.Model):

    #__Altípus_FIELDS__
    név = models.CharField(max_length=255, null=True, blank=True)
    típus = models.ForeignKey(Típus, on_delete=models.CASCADE)

    #__Altípus_FIELDS__END

    class Meta:
        verbose_name        = _("Altípus")
        verbose_name_plural = _("Altípus")


class Vonatok(models.Model):

    #__Vonatok_FIELDS__
    gyártó = models.ForeignKey(Gyártó, on_delete=models.CASCADE)
    típus = models.ForeignKey(Típus, on_delete=models.CASCADE)
    altípus = models.ForeignKey(Altípus, on_delete=models.CASCADE)
    modellszám = models.CharField(max_length=255, null=True, blank=True)
    egyéb azonosító = models.CharField(max_length=255, null=True, blank=True)
    megjegyzés = models.TextField(max_length=255, null=True, blank=True)
    ár = models.IntegerField(null=True, blank=True)
    becsült = models.BooleanField()
    valuta = models.ForeignKey(Valuta, on_delete=models.CASCADE)
    tárolás helye = models.CharField(max_length=255, null=True, blank=True)
    rögzítés ideje = models.DateTimeField(blank=True, null=True, default=timezone.now)
    rögzítő = models.CharField(max_length=255, null=True, blank=True)

    #__Vonatok_FIELDS__END

    class Meta:
        verbose_name        = _("Vonatok")
        verbose_name_plural = _("Vonatok")


class Valuta(models.Model):

    #__Valuta_FIELDS__
    név = models.CharField(max_length=255, null=True, blank=True)
    rövid = models.CharField(max_length=255, null=True, blank=True)
    tohuf = models.IntegerField(null=True, blank=True)

    #__Valuta_FIELDS__END

    class Meta:
        verbose_name        = _("Valuta")
        verbose_name_plural = _("Valuta")


class Fényképek(models.Model):

    #__Fényképek_FIELDS__
    név = models.CharField(max_length=255, null=True, blank=True)
    hely = models.CharField(max_length=255, null=True, blank=True)
    vonat = models.ForeignKey(Vonatok, on_delete=models.CASCADE)

    #__Fényképek_FIELDS__END

    class Meta:
        verbose_name        = _("Fényképek")
        verbose_name_plural = _("Fényképek")



#__MODELS__END
