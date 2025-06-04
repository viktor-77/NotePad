from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username


class Note(models.Model):
    body = models.TextField(
        null=False,
        blank=False,
        validators=[MinLengthValidator(10)]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name_plural = "Notes"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.body[:30]
