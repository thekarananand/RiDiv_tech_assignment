from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'