from djongo import models


class Option(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=200)

    class Meta:
        abstract = True


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    description = models.TextField(null=True)
    options = models.ArrayField(
        model_container=Option,
        blank=True
    )
