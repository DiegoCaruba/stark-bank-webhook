from django.db import models


class Invoice(models.Model):

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recipient_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f" ==>> Invoice {self.id} * amount {self.amount} * status {self.status} * recipient name {self.recipient_name}"
