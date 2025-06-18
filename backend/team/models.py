from django.db import models
from django.core.validators import RegexValidator

phone_validator = RegexValidator(
    regex=r'^\d{10}$',
    message="Phone number must be 10 digits."
)

class TeamMember(models.Model):
    ROLE_CHOICES = [
        ('regular', "Regular - Can't delete members"),
        ('admin', "Admin - Can delete members"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True, validators=[phone_validator])
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='regular')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
