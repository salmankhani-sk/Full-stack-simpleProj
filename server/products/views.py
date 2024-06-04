from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Product
from .serializers import ProductSerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    parser_classes = (MultiPartParser, FormParser)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        data = request.data

        if "image" in data:
            instance.image = data["image"]
        instance.name = data.get("name", instance.name)
        instance.price = data.get("price", instance.price)
        instance.description = data.get("description", instance.description)
        instance.category = data.get("category", instance.category)

        instance.save()

        serializer = self.get_serializer(instance)
        return Response(serializer.data)
