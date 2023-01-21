from django.db import models
from django.conf import settings


class Category(models.Model):
   name = models.CharField(max_length=255)

   def __str__(self):
       return self.name

   class Meta:
      verbose_name = "Category"
      verbose_name_plural = "Kategorie"


TYPE_INSTITUTION = (
   (1, "Fundacja"),
   (2, "Organizacja pozarządowa"),
   (3, "Zbiórka lokalna"),
)


class Institution(models.Model):

   name = models.CharField(max_length=255)
   description = models.TextField(null=True, blank=True)
   type = models.IntegerField(choices=TYPE_INSTITUTION, default=1)
   categories = models.ManyToManyField(Category)

   def __str__(self):
       return self.name

   class Meta:
      verbose_name = "Institution"
      verbose_name_plural = "Instytucje"


class Donation(models.Model):
   quantity = models.IntegerField()
   categories = models.ManyToManyField(Category)
   institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
   street_address = models.CharField(max_length=64)
   city = models.CharField(max_length=64)
   zip_code = models.CharField(max_length=12)
   phone_number = models.IntegerField(max_length=15, blank=True, null=True)
   pick_up_date = models.DateField()
   pick_up_time = models.TimeField()
   pick_up_comment = models.TextField(null=True, blank=True)
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=None)
   is_taken = models.BooleanField(null=True, default=False)

   class Meta:
      verbose_name = "Donation"
      verbose_name_plural = "Darowizny"

