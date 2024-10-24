from django.db import models

class FoodType(models.Model):
    nomi = models.CharField(max_length=100, verbose_name="Tur nomi")

    class Meta:
        verbose_name = "Oziq-ovqat turi"
        verbose_name_plural = "Oziq-ovqat turlari"

    def __str__(self):
        return self.nomi


class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE, verbose_name="Oziq-ovqat turi")
    nomi = models.CharField(max_length=100, verbose_name="Oziq-ovqat nomi")
    tarkibi = models.TextField(verbose_name="Tarkibi")
    narxi = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Narxi")
    korishlar_soni = models.PositiveIntegerField(default=0, verbose_name="Ko'rishlar soni")
    rasm = models.ImageField(upload_to='food_images/', blank=True, null=True, verbose_name="Rasm")

    class Meta:
        verbose_name = "Oziq-ovqat"
        verbose_name_plural = "Oziq-ovqatlar"

    def __str__(self):
        return self.nomi
