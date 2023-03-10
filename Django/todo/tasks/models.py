from django.db import models

class Task(models.Model):
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done')
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    done = models.CharField(
        max_length=5,
        choices=STATUS,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title