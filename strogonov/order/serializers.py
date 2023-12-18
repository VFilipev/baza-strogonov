from . models import Order, Order_lodge, Product, Uslugi, Service
from lodge.models import Lodge
from rest_framework import serializers
from lodge.serializers import LodgeSerializer
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template
from django.core.mail import EmailMessage

class ProductInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('order',)
        depth = 1

class ServiceInlineSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    end_date = serializers.DateTimeField(format="%Y-%m-%dT%H:%M")
    class Meta:
        model = Service
        exclude = ('order',)
        depth = 1

class LodgeInlineSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(format="%Y-%m-%d")
    end_date = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Order_lodge
        exclude = ('order',)
        depth = 1
##################
class UslugiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uslugi
        fields = '__all__'

class ProductSetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Product
        exclude = ('order',)

class Order_lodgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_lodge
        fields = '__all__'
        depth = 1

class OrderLodgeSetSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(input_formats=["%d.%m.%Y"])
    end_date = serializers.DateField(input_formats=["%d.%m.%Y"])
    cost = serializers.CharField()           
        
    class Meta:
        model = Order_lodge
        fields = '__all__'     

    def to_representation(self, instance):
        representation = super(OrderLodgeSetSerializer, self).to_representation(instance)
        representation['lodge'] = LodgeSerializer(instance.lodge).data
        return representation

class ServiceSetSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Service
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    services = ServiceInlineSerializer(many=True, required=False, read_only=True)
    products = ProductInlineSerializer(many=True, required=False, read_only=True)
    order_lodge_set= LodgeInlineSerializer(many=True, required=False, read_only=True)
    services_set = ServiceSetSerializer(many=True, required=False)
    orderlodge_set = OrderLodgeSetSerializer(many=True, required=False)
    products_set = ProductSetSerializer(many=True, required=False)
    class Meta:
        model = Order
        fields = '__all__'
        depth = 1

    def create(self, validated_data):
        # product_set = validated_data.pop('products_set')
        # orderlodge_set = validated_data.pop('orderlodge_set')        
        # services_set = validated_data.pop('services_set')
        # order = Order.objects.create(**validated_data)
        # if services_set:
        #     for services in services_set:
        #         if services['start_date'] is not None:
        #             Service.objects.create(order = order, **services)
        # if product_set:
        #     for product in product_set:
        #         if product['value'] is not None:
        #             Product.objects.create(order = order, **product)
        # for orderlodge in orderlodge_set:
        #     Order_lodge.objects.create(order = order,  **orderlodge)


        from . views import DogovorView2
        dogovor_pdf = DogovorView2({}, 1)        
        order = {}
        subject = 'Тема письма'
        message = 'Текст сообщения'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = ['vasiliy20122009@mail.ru']
        file_list = []
        file_list.append(["test.docx", dogovor_pdf, "application/vnd.openxmlformats-officedocument.wordprocessingml.document"])        
        send_email_with_attachment(subject, message, from_email, recipient_list, file_list)
        
        
        # msg = get_template('order/order_detail_mail.html')
        # message_body = msg.render()
        # send_mail('Заказ Строгоновские просторы', message_body, settings.EMAIL_HOST_USER, ['vasiliy20122009@mail.ru'])
        
        return order
    def update(self, instance, validated_data):
        orderlodge_set = validated_data.pop('orderlodge_set')
        product_set = validated_data.pop('products_set')
        services_set = validated_data.pop('services_set')
        instance = super().update(instance, validated_data)
        instance.save()
        for x in orderlodge_set:
            if 'id' in x:
                lodge = Order_lodge.objects.get(pk = x['id'])
                lodge = Order_lodge(order = instance, **x)
                lodge.save()
            else:
                Order_lodge.objects.create(order = instance,  **x)
        for x in product_set:
            if 'id' in x:
                product = Product.objects.get(pk = x['id'])
                product = Product(order = instance, **x)
                product.save()
            else:
                Product.objects.create(order = instance, **x)
        for x in services_set:
            if 'id' in x:
                service = Service.objects.get(pk = x['id'])
                service = Service(order = instance, **x)
                service.save()
            else:
                Service.objects.create(order = instance, **x)
        return instance
class Order_lodgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order_lodge
        fields = '__all__'
        depth = 1

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        depth = 1

def send_email_with_attachment(subject, message, from_email, recipient_list, attachment):
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=from_email,
        to=recipient_list,
        attachments = attachment
    )
 
    email.send()