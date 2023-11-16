from django.shortcuts import render
from django.http import HttpRequest,HttpResponse,JsonResponse
from django.views import View
from .models import Customer,Contact,Publisher,Language,Book,Author,Genre
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
        return JsonResponse(result, status=201)\
        
class PublishersView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        results=[]
        for publisher in Publisher.objects.all():
            results.append(model_to_dict(publisher))
        return JsonResponse(results,safe=False)
    
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        publisher=Publisher.objects.create(
            name=data.get('name'),
            description=data.get('description')
        )
        result=model_to_dict(publisher)
        return JsonResponse(result, status=201)
    

class PublisherDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        publisher=Publisher.objects.get(id=pk)
        result=model_to_dict(publisher)
        return JsonResponse(result)
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            publisher=Publisher.objects.get(id=pk)
        except:
            return JsonResponse({'error':'Bunaqa id li customer yuq!!!'},status=404)
        data=json.loads(request.body.decode())

        publisher.name=data.get('name',publisher.name)
        publisher.description=data.get('description',publisher.description)
        publisher.save()
        return JsonResponse({"message":"Yangilandi"},status=203)
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            publisher=Publisher.objects.get(id=pk)
        except:
            return JsonResponse({"error":"Bunaqa id li customer yuq!!!"},status=404)
        publisher.delete()
        return JsonResponse({"message":"customer delete"},status=204)


class LanguagesView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        results=[]
        for lang in Language.objects.all():
            results.append(model_to_dict(lang))
        return JsonResponse(results,safe=False)
    
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        lang=Language.objects.create(
            lang=data.get('lang')
        )
        result=model_to_dict(lang)
        return JsonResponse(result, status=201)
    

class LanguageDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        lang=Language.objects.get(id=pk)
        result=model_to_dict(lang)
        return JsonResponse(result)
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            lang=Language.objects.get(id=pk)
        except:
            return JsonResponse({'error':'Bunaqa id li customer yuq!!!'},status=404)
        data=json.loads(request.body.decode())

        lang.lang=data.get('lang',lang.lang)
        lang.save()
        return JsonResponse({"message":"Yangilandi"},status=203)
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            lang=Language.objects.get(id=pk)
        except:
            return JsonResponse({"error":"Bunaqa id li customer yuq!!!"},status=404)
        lang.delete()
        return JsonResponse({"message":"customer delete"},status=204)


class BooksView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        params = request.GET

        if params.get('title', False):
            books = Book.objects.filter(title__icontains=params.get('title'))
        elif params.get('description', False):
            books = Book.objects.filter(description__icontains=params.get('description'))
        elif params.get('price', False):
            books = Book.objects.filter(price__lte=params.get('price'))
        elif params.get('lang', False):
            books = Book.objects.filter(lang__lang__icontains=params.get('lang'))
        elif params.get('publisher', False):
            books = Book.objects.filter(publisher__name__icontains=params.get('publisher'))
        else:
            books = Book.objects.all()

        result = [model_to_dict(book) for book in books]
        return JsonResponse(result, safe=False)
         
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        Book.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            price=data.get('price'),
            quantity=data.get('quantity'),
            isbn=data.get('isbn'),
            lang=data.get('lang'),
            pages=data.get('pages'),
            publisher=data.get('publisher'),
            pubished_date=data.get('pubished_date')
        )
        return JsonResponse({"message":"ok"}, status=201)
    

class BookDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        book=Book.objects.get(id=pk)
        result=model_to_dict(book)
        return JsonResponse(result)
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            book=Book.objects.get(id=pk)
        except:
            return JsonResponse({'error':'Bunaqa id li customer yuq!!!'},status=404)
        data=json.loads(request.body.decode())

        book.title=data.get('title',book.title)
        book.description=data.get('description',book.description)
        book.price=data.get('price',book.price)
        book.quantity=data.get('quantity',book.quantity)
        book.isbn=data.get('isbn',book.isbn)
        book.lang=data.get('lang',book.lang)
        book.pages=data.get('pages',book.pages)
        book.publisher=data.get('publisher',book.publisher)
        book.pubished_date=data.get('pubished_date',book.pubished_date)
        book.authors=data.get('authors',book.authors)
        book.genres=data.get('genres',book.genres)
        book.save()
        return JsonResponse({"message":"Yangilandi"},status=203)
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            book=Book.objects.get(id=pk)
        except:
            return JsonResponse({"error":"Bunaqa id li customer yuq!!!"},status=404)
        book.delete()
        return JsonResponse({"message":"customer delete"},status=204)

class AuthorView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        results=[]
        for lang in Author.objects.all():
            results.append(model_to_dict(lang))
        return JsonResponse(results,safe=False)
    
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        publisher=Publisher.objects.create(
            first_name=data.get('first_name'),
            last_name=data.get('last_name'),
            bio=data.get('bio')
        )
        result=model_to_dict(publisher)
        return JsonResponse(result, status=201)
    

class AuthorDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        aut=Author.objects.get(id=pk)
        result=model_to_dict(aut)
        return JsonResponse(result)
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            aut=Author.objects.get(id=pk)
        except:
            return JsonResponse({'error':'Bunaqa id li customer yuq!!!'},status=404)
        data=json.loads(request.body.decode())

        aut.name=data.get('first_name',aut.first_name)
        aut.description=data.get('last_name',aut.last_name)
        aut.bio=data.get('bio',aut.bio)
        aut.save()
        return JsonResponse({"message":"Yangilandi"},status=203)
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            aut=Author.objects.get(id=pk)
        except:
            return JsonResponse({"error":"Bunaqa id li customer yuq!!!"},status=404)
        aut.delete()
        return JsonResponse({"message":"customer delete"},status=204)


class GenreView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        results=[]
        for genre in Genre.objects.all():
            results.append(model_to_dict(genre))
        return JsonResponse(results,safe=False)
    
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        genre=Genre.objects.create(
            genre=data.get('genre')
        )
        result=model_to_dict(genre)
        return JsonResponse(result, status=201)
    

class GenreDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        genre=Genre.objects.get(id=pk)
        result=model_to_dict(genre)
        return JsonResponse(result)
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            genre=Genre.objects.get(id=pk)
        except:
            return JsonResponse({'error':'Bunaqa id li customer yuq!!!'},status=404)
        data=json.loads(request.body.decode())

        genre.name=data.get('lang',genre.name)
        genre.save()
        return JsonResponse({"message":"Yangilandi"},status=203)
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        try:
            genre=Genre.objects.get(id=pk)
        except:
            return JsonResponse({"error":"Bunaqa id li customer yuq!!!"},status=404)
        genre.delete()
        return JsonResponse({"message":"customer delete"},status=204)
