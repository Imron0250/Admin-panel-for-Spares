from rest_framework.serializers import ModelSerializer
from .models import *

class SparesSerializers(ModelSerializer):
    class Meta:
        model = Spares
        fields = "__all__"

class Featured_ProductSerializers(ModelSerializer):
    class Meta:
        model = Featured_Products
        fields = "__all__"

class Helpers_TaskSerializers(ModelSerializer):
    class Meta:
        model = Helpers_Task
        fields = "__all__"

class HelperSerializers(ModelSerializer):
    class Meta:
        model = Helper
        fields = "__all__"

class PartnerSerializers(ModelSerializer):
    class Meta:
        model = Partner
        fields = "__all__"

class InfoSerializers(ModelSerializer):
    class Meta:
        model = Info
        fields = "__all__"

class DebtSerializers(ModelSerializer):
    class Meta:
        model = Debt
        fields = "__all__"

class Earning_Info(ModelSerializer):
    class Meta:
        model = Earning_Info
        fields = "__all__"

class MachineSerializers(ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"

class The_deliverymanSerialziers(ModelSerializer):
    class Meta:
        model = The_deliveryman
        fields = "__all__"

class Cleaning_locationSerializer(ModelSerializer):
    class Meta:
        model = cleaning_location
        fields = "__all__"

class CleanerSerializer(ModelSerializer):
    class Meta:
        model = Cleaner
        fields = "__all__"


The_deliveryman
cleaning_location
Cleaner