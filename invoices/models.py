from django.db import models

class Invoice(models.Model):
    date = models.DateField(null=False, blank=False)
    customerName = models.CharField(max_length=50, null=False, blank=False)

class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE,
        related_name='invoice',
    )
    description = models.CharField(max_length=1000, null=True, blank=True)
    quantity = models.PositiveIntegerField(null=False, blank=False)
    unit_price = models.FloatField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)


    # invoice_id = 2, description = "Some Really Shady Stuff", quantity = 1000, unit_price = 10, price = "10000"