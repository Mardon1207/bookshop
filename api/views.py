from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.views import View
from .models import Customer,Contact
from django.forms import model_to_dict
from django.core.exceptions import ObjectDoesNotExist
import json


class RegistratsiyaView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'registratsiya.html')
    
class HomeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'home.html')
    
class CustomerViev(View):
    def get(self,requests: HttpRequest):
        """customer get request

        Args:
            requests (HttpRequest): _description_

        Returns:
            response (HttpResponse): _description_
        """        
        results=[]
        for customer in Customer.objects.all():
            results.append(model_to_dict(customer,fields=['id','first_name','last_name','username']))
        return JsonResponse(results,safe=False)
    
    def post(self,request: HttpRequest):
        """customer create

        Args:
            request (HttpRequest): _description_

        Returns:
            response (HttpResponse): _description_
        """        
        data = json.loads(request.body.decode())

        customer=Customer.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            password=data.get('password'),
            username=data.get('username')
        )
        result=model_to_dict(customer)
        return JsonResponse(result, status=201)
    def put(self,request: HttpRequest,pk:int):
        """customer update

        Args:
            request (HttpRequest): _description_
            pk (int): _description_

        Returns:
            response (HttpResponse): _description_
        """        
        try:
            customer=Customer.objects.get(id=pk)
        except:
            return JsonResponse({'error':'Bunaqa id li customer yuq!!!'},status=404)
        data=json.loads(request.body.decode())

        customer.first_name=data.get('first_name',customer.first_name)
        customer.last_name=data.get('last_name',customer.last_name)
        customer.username=data.get('username',customer.username)
        customer.password=data.get('password',customer.password)
        customer.save()
        return JsonResponse({"message":"Yangilandi"},status=203)
    
    def delete(self,request: HttpRequest,pk:int):
        """customer delete

        Args:
            request (HttpRequest): _description_
            pk (int): _description_

        Returns:
            response (HttpResponse): _description_
        """        
        try:
            customer=Customer.objects.get(id=pk)
        except:
            return JsonResponse({"error":"Bunaqa id li customer yuq!!!"},status=404)
        customer.delete()
        return JsonResponse({"message":"customer delete"},status=204)
    
class ContactView(View):
    def get(self,reqeust : HttpRequest,pk:int):
        """contact get request

        Args:
            request (HttpRequest): _description_
            pk (int): _description_

        Returns:
            response (HttpResponse): _description_
        """ 
        customer=Customer.objects.get(id=pk)
        contact=Contact.objects.get(customer=customer)
        result=model_to_dict(contact)
        return JsonResponse(result)
    def post(self,reqeust : HttpRequest,pk : int):
        """contact create

        Args:
            request (HttpRequest): _description_
            pk (int): _description_

        Returns:
            response (HttpResponse): _description_
        """ 
        try:
            customer=Customer.objects.get(id=pk)
        except ObjectDoesNotExist:
            return JsonResponse({"error":"customer does not exist"})
        data= json.loads(reqeust.body.decode())

        contact=Contact.objects.create(
            customer=customer,
            email=data.get('email'),
            address=data.get('address'),
            phone=data.get('phone')
        )
        result=model_to_dict(contact)
        return JsonResponse(result, status=201)