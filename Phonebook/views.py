from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
from rest_framework.decorators import api_view

from .models import Contact
from .serializers import ContactSerializer

@api_view(['POST'])
def insert_contact(request):
    """
    Insert a new contact into the database.
    """
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

def insert_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def update_contact(request, pk):
    """
    Update an existing contact identified by pk.
    """
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)

def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_contact(request, pk):
    """
    Delete a contact identified by pk.
    """
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return JsonResponse({'message': 'Contact deleted successfully'}, status=204)

def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return JsonResponse({'message': 'Contact deleted successfully'}, status=204)


@api_view(['GET'])
def search_contact(request):
    """
    Search for contacts based on query parameters.
    """
    query = request.GET.get('query')
    if query:
        contacts = Contact.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone_number__icontains=query) |
            Q(address__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        filters = {
            'first_name__icontains': request.GET.get('param1'),
            'last_name__icontains': request.GET.get('param2'),
            'phone_number__icontains': request.GET.get('param3'),
            'address__icontains': request.GET.get('param4'),
            'email__icontains': request.GET.get('param5'),
        }
        filters = {k: v for k, v in filters.items() if v}
        contacts = Contact.objects.filter(**filters)

    serializer = ContactSerializer(contacts, many=True)
    return JsonResponse(serializer.data, safe=False)
def search_contact(request):
    
    query = request.GET.get('query')
    
    if query:
        contacts = Contact.objects.filter(
        first_name=query) | \
        Contact.objects.filter(last_name=query) | \
        Contact.objects.filter(phone_number=query) | \
        Contact.objects.filter(address=query) | \
        Contact.objects.filter(email=query) 
        
        
    else:    
        first_name = request.GET.get('param1')
        last_name = request.GET.get('param2')
        phone_number= request.GET.get('param3')
        address = request.GET.get('param4')
        email = request.GET.get('param5')
        contacts = Contact.objects.filter(
            first_name=first_name) | \
            Contact.objects.filter(last_name=last_name) | \
            Contact.objects.filter(phone_number=phone_number) | \
            Contact.objects.filter(address=address) | \
            Contact.objects.filter(email=email)


    serializer = ContactSerializer(contacts, many=True)
    return JsonResponse(serializer.data, safe=False)
