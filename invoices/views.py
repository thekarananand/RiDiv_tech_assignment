from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializers, InvoiceDetailSerializers

@api_view(['POST', 'GET', 'PUT'])
def invoices(request):
    if (request.method == 'POST'):
        serializer = InvoiceSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    if (request.method == 'GET'):
        data = Invoice.objects.all()
        serializer = InvoiceSerializers(data, many=True)
        return Response(serializer.data)
    
    if (request.method == 'PUT'):
        data_id = request.data['id']

        try: 
            invoice = Invoice.objects.get(id=data_id)
            serializer = InvoiceSerializers(invoice, data=request.data)
        except Invoice.DoesNotExist:
            serializer = InvoiceSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       

@api_view(['POST', 'GET', 'PUT', 'PATCH', 'DELETE'])
def invoicesDetails(request, pk):

    try:
        Invoice.objects.filter(id=pk)
    except Invoice.DoesNotExist:
        return Response(f'No Invoice Entry Exist with Invoice id: {pk}')

    if (request.method == 'POST'):
        serializer = InvoiceDetailSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if (request.method == 'GET'):
        invoice_data = Invoice.objects.get(id=pk)
        invoice_detail_data = InvoiceDetail.objects.filter(invoice_id=pk)

        invoice_data_serializer = InvoiceSerializers(invoice_data)
        invoice_detail_data_serializer = InvoiceDetailSerializers(invoice_detail_data, many=True)

        data_to_send = invoice_data_serializer.data
        data_to_send['invoice_detail'] = invoice_detail_data_serializer.data

        print(data_to_send)

        return Response(data_to_send)
    
    if (request.method == 'PUT'):
        try:
            invoice_detail = InvoiceDetail.objects.get(id=request.data['id'])
            serializer = InvoiceDetailSerializers(invoice_detail, data=request.data)
        except InvoiceDetail.DoesNotExist:
            return Response(f'No Invoice Detail Entry Exist with Invoice id: {request.data['id']}')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if (request.method == 'PATCH'):
        try:
            invoice_detail = InvoiceDetail.objects.get(id=request.data['id'])
            serializer = InvoiceDetailSerializers(invoice_detail, data=request.data, partial=True)
        except InvoiceDetail.DoesNotExist:
            return Response(f'No Invoice Detail Entry Exist with Invoice id: {request.data['id']}')

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    
    if (request.method == 'DELETE'):
        try: 
            invoice = Invoice.objects.get(id=pk)
            invoice.delete()
            return Response("Invoice Entry Deleted")
        except Invoice.DoesNotExist:
            return Response("Invoice Entry Don't Exist")
    