from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.decorators import api_view

@api_view(['POST'])
def insert_contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)
    return JsonResponse(serializer.errors, status=400)

@api_view(['PUT'])
def update_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    serializer = ContactSerializer(contact, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_contact(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    contact.delete()
    return JsonResponse({'message': 'Contact deleted successfully'}, status=204)


@api_view(['GET'])
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
