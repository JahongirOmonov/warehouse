from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Material, ProductMaterial, Warehouse
from .serializers import ProductSerializer, MaterialSerializer, ProductMaterialSerializer, WarehouseSerializer
from rest_framework import generics

class ProductListCreateAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MaterialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer


def calculating():
    products = Product.objects.all()

    result = []
    for product in products:
        product_materials = []
        product_qty = 0

        #umumiy quantity va har bir material uchun narx
        for product_material in product.materials.all():
            material_name = product_material.material.title
            # print(material_name)
            material_qty = product_material.quantity * product_qty
            print(material_qty)
            sklad = Warehouse.objects.filter(material=product_material.material).first()

            if sklad:
                warehouse_id = sklad.id
                # print(warehouse_id)
                warehouse_qty = sklad.remainder
                warehouse_price = sklad.price
            else:
                warehouse_id = None
                warehouse_qty = None
                warehouse_price = None




            product_material_data = {
                "warehouse_id": warehouse_id,
                "material_name": material_name,
                "price": warehouse_price
            }

            if warehouse_qty:

                product_material_data["qty"] = min(material_qty, warehouse_qty)
            else:
                product_material_data["qty"] = None

            product_materials.append(product_material_data)

            product_qty += product_material.quantity



        result.append({
            "product_name": product.title,
            "product_qty": product_qty,
            "product_materials": product_materials
        })
        # print(result)

    return {"result": result}

class ProductMaterialsAPIView(APIView):
    def get(self, request):
        result = calculating()
        return Response(result)



