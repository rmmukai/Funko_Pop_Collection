from django.db import models

class Pop_Entry(models.Model):
    CONDITION_CHOICES = (
        ('EXCELLENT', 'Excellent'),
        ('GOOD', 'Good'),
        ('FAIR', 'Fair'),
        ('POOR', 'Poor'),
        ('DAMAGED', 'Damaged'),
    )

    character = models.CharField(max_length=30)
    series = models.CharField(max_length=50)
    series_number = models.IntegerField()
    special_edition = models.CharField(max_length=30)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    image = models.ImageField(upload_to="images/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



