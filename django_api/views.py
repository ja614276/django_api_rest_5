from decimal import Decimal

import json
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from django_api.models import Product


# Create your views here.


class ProductView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if id>0:
            products = list(Product.objects.filter(id=id).values())
            if len(products)>0:
                product=products[0]
                mensaje={'message': "Producto encontrado.", 'products': product}
            else:
                mensaje = {'message': "Producto no encontrado."}
            return JsonResponse(mensaje)
        else:
            products = list(Product.objects.values())
            if len(products)>0:
                mensaje = {'message': "Productos encontrados.", 'products': products}
            else:
                mensaje = {'message':"Productos no encontrados."}
        return JsonResponse(mensaje)

    def post(self, request):
        #print(request.body)
        jd =json.loads(request.body)
        #print(jd)
        Product.objects.create(
            nombre=jd['nombre'],
            descripcion=jd['descripcion'],
            precio=jd['precio'],
            stock=jd['stock'],
            fecha_vencimiento=jd['fecha_vencimiento']
        )
        mensaje = {'message': "Producto registrado con exito."}
        return JsonResponse(mensaje)

    def put(self, request, id):
        jd =json.loads(request.body)
        products = list(Product.objects.filter(id=id).values())
        if len(products) > 0:
            product = Product.objects.get(id=id)
            product.nombre=jd['nombre']
            product.descripcion = jd['descripcion']
            product.precio = Decimal(jd['precio'])
            product.stock = jd['stock']
            product.fecha_vencimiento = jd['fecha_vencimiento']
            product.save()
            mensaje = {'message': "Producto actualizado con exito."}
        else:
            mensaje = {'message': "Producto no existe."}
        return JsonResponse(mensaje)

    def delete(self, request, id):
        products = list(Product.objects.filter(id=id).values())
        if len(products) > 0:
            Product.objects.filter(id=id).delete()
            mensaje = {'message': "Producto eliminado con exito."}
        else:
            mensaje = {'message': "Error en delete."}
        return JsonResponse(mensaje)
