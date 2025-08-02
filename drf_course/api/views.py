from django.shortcuts import get_object_or_404
from api.serializer import ProductSerializer,OrderSerializer,ProductInfoSerializer
from api.models import Product,Order
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Max

# Create your views here.
from django.http import JsonResponse

# def product_list(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return JsonResponse({'data' : serializer.data})


# This decorator from DRF allows only GET requests to this view.
@api_view(['GET'])  
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
    orders = Order.objects.prefetch_related('items__product')
    serializer = OrderSerializer(orders,many = True)
    return Response(serializer.data)

@api_view(["GET"])
def product_info(request):
    products = Product.objects.all()
    serializer = ProductInfoSerializer({
        'products': products,
        'count': len(products),
        'max_price': products.aggregate(max_price=Max('price'))['max_price']
    })
    return Response(serializer.data)



# 🧪 Example:
# Let's say your max price is 12.99
# With ['max_price']:

# python
# Copy
# Edit
# max_price = 12.99
# Without ['max_price']:

# python
# Copy
# Edit
# max_price = {'max_price': 12.99}