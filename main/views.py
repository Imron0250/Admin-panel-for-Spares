from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


@api_view(['GET'])
def get_Spares(request):
    spares = Spares.objects.all()
    spares_ser = SparesSerializers(spares, many=True)
    data = {
        "spares": spares_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_featured_products(request):
    featured_products = Featured_Products.objects.all()
    featured_products_ser = Featured_ProductSerializers(featured_products, many=True)
    data = {
        "featured_products": featured_products_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_helper(request):
    helper = Helper.objects.all()
    helper_ser = HelperSerializers(helper, many=True)
    data = {
        'helper': helper_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_Partner(request):
    partner = Partner.objects.all()
    partner_ser = PartnerSerializers(partner, many=True)
    data = {
        'partner': partner_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_Info(request):
    info = Info.objects.last()
    info_ser = InfoSerializers(info)
    data = {
        "info": info_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_Debt(request):
    debt = Debt.objects.all()
    debt_ser = DebtSerializers(debt, many=True)
    data = {
        "debt": debt_ser.data
    }
    return Response(data)


@api_view(['GET'])
def get_Machine(request):
    machine = Machine.objects.all()
    machine_ser = MachineSerializers(machine, many=True)
    data = {
        "machine": machine_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_The_deliveryman(request):
    the_deliveryman = The_deliveryman.objects.all()
    the_deliveryman_ser = The_deliverymanSerialziers(the_deliveryman, many=True)
    data = {
        "the_deliveryman": the_deliveryman_ser.data
    }
    return Response(data)

@api_view(['GET'])
def get_Cleaner(request):
    cleaner = Cleaner.objects.all()
    cleaner_ser = CleanerSerializer(cleaner, many=True)
    data = {
        'cleaner': cleaner_ser.data
    }
    return Response(data)
