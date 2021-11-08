from django.db import models

class Person(models.Model):
    first_name = models.CharField(verbose_name= 'First name',max_length=30)
    last_name = models.CharField(verbose_name= 'Last name', max_length=80)
    age = models.IntegerField(verbose_name= 'Age', default=0)
    sector = models.CharField(verbose_name= 'Sector', max_length=30)
    photo = models.ImageField(verbose_name= 'Photo', upload_to='images/',
                            null=True, blank=True
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clentes'
        ordering = ['first_name',]

