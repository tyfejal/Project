from django.db import models

class MetalPrice(models.Model):
    METAL_CHOICES = [
        ('gold', 'Gold'),
        ('silver', 'Silver'),
    ]

    date = models.DateField()
    metal_type = models.CharField(max_length=10, choices=METAL_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        unique_together = ('date', 'metal_type')
        ordering = ['-date']

    def __str__(self):
        return f"{self.date} - {self.metal_type} - {self.price}"
