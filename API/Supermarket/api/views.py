#from django.http.response import JsonResponse
#from django.shortcuts import render
from django.views import View

#from .models import Products


# Create your views here.
"""
class ProductsView(View):

    def get(self, request):
        products = list(Products.objects.values())
        if len(products)>0:
            datos={'message':"Success", 'products':products}
        else:
            datos={'message':"Products not found..."}
            return JsonResponse    

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass

"""