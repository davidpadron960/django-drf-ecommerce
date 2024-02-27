from rest_framework import serializers
from producto.models import Producto,Categoria

"""
class ProductoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    price = serializers.DecimalField(max_digits=9,decimal_places=2)
    image = serializers.ImageField(max_length=None, use_url=True, required=False,allow_null = True)
    active = serializers.BooleanField()

    def create(self,validate_data):
        return Producto.objects.create(**validate_data)
    
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.price = validate_data.get('price',instance.price)
        instance.active = validate_data.get('active',instance.active)
        if 'image' in validate_data:
            instance.image = validate_data['image']
        instance.save()
        return instance
    
    def validate(self,data):
        if data['price'] <= 0:
            raise serializers.ValidationError("El precio del producto debe ser mayor que 0")
        else:
            return data
"""
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class ProductoSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    image = serializers.ImageField(max_length=None, use_url=True, read_only=True)
    class Meta:
        model = Producto
        fields = "__all__"
    
    def update(self,instance,validate_data):
        instance.name = validate_data.get('name',instance.name)
        instance.price = validate_data.get('price',instance.price)
        instance.active = validate_data.get('active',instance.active)
        print(instance.category)
        instance.save()
        return instance
