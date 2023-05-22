
from django.db import models
from django.core.exceptions import ValidationError


from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _



class User(AbstractUser):
    password = models.CharField(_('password'), max_length=128)
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def clean(self):
        super().clean()
        if User.objects.filter(password=self.password).exists():
            raise ValidationError('Password must be unique')
