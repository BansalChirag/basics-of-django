from rest_framework import serializers
from .models import Product,Order,OrderItem
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')  # Add other fields as needed
        
class ProductSerializer(serializers.ModelSerializer):
    # class ProductSerialzer(serializers.Serializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'stock',
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than 0."
            )
        return value
    
class OrderItemSerializer(serializers.ModelSerializer):
    
 # Nesting the ProductSerializer
    # product = ProductSerializer(read_only=True)
    
    product_name = serializers.CharField(source='product.name')
    product_price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        source='product.price')
    
    # item_subtotal = serializers.ReadOnlyField()  # <-- This will call the property using this 
    # or
    item_subtotal = serializers.SerializerMethodField()
    
    
    class Meta:
        model = OrderItem
        fields = (
            'quantity',
            # 'product',
            'product_name',
            'product_price',
            'order',
            'item_subtotal',
    
        )
        
    def get_item_subtotal(self, obj):
        return obj.item_subtotal

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many = True,read_only = True)
    
    total_price = serializers.SerializerMethodField(method_name = 'total') # if method_name is not passed then the function name should be get_total_price
    
    def total(self,obj):
        return sum(item.item_subtotal for item in obj.items.all())
    
      # ✅ Nested UserSerializer if you want to include user details in the order response
    # user = UserSerializer(read_only=True)
    
    user_id = serializers.CharField(source='user.id')
    user_name = serializers.CharField(source='user.username')
    
    
    class Meta:
        model = Order
        fields = (
            'order_id',
            # 'user',
            'user_id',
            'user_name',
            'status',
            'products',
            'items',
            'total_price'
        )