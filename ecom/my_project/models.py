from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    count=models.IntegerField()
    category=models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    def __str__(self):
        return self.name
class Customer(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    def __str__(self):
        return self.full_name
    
    def save(self, *args, **kwargs):
        if self.full_name:
            self.full_name=self.full_name.title()
        super().save(*args, **kwargs)
        
class Order(models.Model):
    customer=models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='orders',
        blank=True,
        null=True
    )
    product=models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='orders',
        blank=True,
        null=True
    )


