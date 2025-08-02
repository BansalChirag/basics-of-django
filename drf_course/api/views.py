from django.shortcuts import get_object_or_404
from api.serializer import ProductSerializer,OrderSerializer
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
from django.http import JsonResponse

# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return JsonResponse({'data' : serializer.data})



@api_view(['GET'])  # ✅ Add this decorator
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response({'data': serializer.data})

# or directly use this without serializer => return Response({'data': products.values()})

@api_view(['GET'])
def product_detail(request,id):
    product = get_object_or_404(Product, pk=id)
    print("product : ",product)
    serializer = ProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def order_list(request):
    orders = Order.objects.all();
    serializer = OrderSerializer(orders,many = True)
    return Response(serializer.data)