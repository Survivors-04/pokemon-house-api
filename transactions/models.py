from django.db import models
import uuid

class Transaction(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    buyed_id = models.CharField(max_length=150)
    seller_id =   models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="transactions"
    )
