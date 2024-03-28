from django.db import models
from .constants import transaction_status

class Transaction(models.Model):
    status = models.CharField(
        "Transaction Status",
        max_length=9,
        choices=transaction_status,
        default="PENDING",
    )
    created_at = models.DateTimeField(
        "Created at",
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.id} - {self.status} | {self.created_at}"
