import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
import datetime as dt
from django.urls import reverse
from . models import Order, Order_lodge, Product, Uslugi, Service
# from django.db.models import Sum
import decimal
try:
    import StringIO
except:
    from io import StringIO,BytesIO
from docxtpl import DocxTemplate, R
from django.template.defaultfilters import linebreaks


from datetime import timedelta
from datetime import date
from jinja2 import Environment
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet, DateFilter
from . serializers import OrderSerializer, Order_lodgeSerializer, ProductSetSerializer, UslugiSerializer, ServiceSerializer
from django.http import JsonResponse
from rest_framework.decorators import action

# Create your views here.
class ServiceSetFilter(FilterSet):
    start_date = DateFilter(field_name='start_date',lookup_expr=('date__exact'),)    
    class Meta:
        model = Service
        fields = ['start_date', 'name']

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    model = Service
    serializer_class = ServiceSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class  = ServiceSetFilter

class Order_lodgeSetFilter(FilterSet):
    start_date = DateFilter(field_name='start_date',lookup_expr=('gte'),)
    end_date = DateFilter(field_name='end_date',lookup_expr=('lte'),)
    class Meta:
        model = Order_lodge
        fields = ['order', 'lodge', 'start_date', 'end_date']

class Order_lodgeViewSet(viewsets.ModelViewSet):
    queryset = Order_lodge.objects.all()
    model = Order_lodge
    serializer_class = Order_lodgeSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class  = Order_lodgeSetFilter


class OrderSetFilter(FilterSet):    
    class Meta:
        model = Order
        fields = ['number','status','id']

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    model = Order
    serializer_class = OrderSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class  = OrderSetFilter  

    @action(detail=False, methods=['get'],permission_classes=[])
    def last(self, request):        
        order = Order.objects.all().last()
        tmp = {'order_id': order.id + 1}
        return JsonResponse(tmp,safe=False)

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['order']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    model = Product
    serializer_class = ProductSetSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class  = ProductFilter

class UslugiViewSet(viewsets.ModelViewSet):
    queryset = Uslugi.objects.all()
    model = Uslugi
    serializer_class = UslugiSerializer
    filter_backends = [DjangoFilterBackend,]

class Order_lodgeSetFilter(FilterSet):
    start_date = DateFilter(field_name='start_date',lookup_expr=('gte'),)
    end_date = DateFilter(field_name='end_date',lookup_expr=('lte'),)
    class Meta:
        model = Order_lodge
        fields = ['order', 'lodge', 'start_date', 'end_date']

class Order_lodgeViewSet(viewsets.ModelViewSet):
    queryset = Order_lodge.objects.all()
    model = Order_lodge
    serializer_class = Order_lodgeSerializer
    filter_backends = [DjangoFilterBackend,]
    filterset_class  = Order_lodgeSetFilter

def DogovorView2(request,order):    
    steam = BytesIO()
    if order.ul:
        doc = DocxTemplate('ul.docx')
    else:
        doc = DocxTemplate('fl.docx')

    lodge_list=[]
    service_list = []
    total_cost = 0
    for lodge in  order.order_lodge_set.all():
        lodge_list.append({'name':lodge.lodge.name,
                           'id':lodge.lodge.id,
                           'num':lodge.lodge.num,
                           'cost':lodge.cost,
                           'start': lodge.start_date.strftime(u'%d %B  %Y'),
                           'end':lodge.end_date.strftime(u'%d %B %Y')})
        total_cost += decimal.Decimal(lodge.cost)
    for service in  order.services.all():
        service_list.append({
            'name': service.get_name_display(),
            'cost': service.cost,
            'start_date': service.start_date.strftime(u'%d %B %Y %H:%M'),
            'end_date': service.end_date.strftime(u'%d %B %Y %H:%M'),
        })
        total_cost += service.cost
    context = {'company_name' : u"Строгановские просторы",
               'pasport': R(order.pasport),
               'addres':order.addres,
               'phone':order.phone,
               'order_date': order.order_date.strftime('%d.%m.%Y'),
               'order_date_pay': (order.order_date +timedelta(days=2)).strftime('%d.%m.%Y'),
               'order_year': order.order_date.strftime(u'%Y'),
               'customer':order.customer,
               'number':order.number,
               'facimile':order.facimile,
               'lodge_list':lodge_list,
               'service_list':service_list,
               'total_cost': total_cost,
            #    'cost':u'%.0f' %order.get_cost(),
            #    'cost_avans':u'%.0f' %(order.get_cost()/2),
            #    'text_cost_avans':(order.get_text_cost_avans()),
            #    'text_cost':order.get_text_cost(),
               'company':order.company
               }
    jinja_env = Environment()
    jinja_env.filters['linebreaks'] = linebreaks
    doc.render(context,jinja_env)
    doc.save(steam)
    # connect_lenght = steam.tell()
    steam.seek(0)
    # response = FileResponse(steam)

    # response['Content-Disposition'] = 'attachment; filename=dogovor_%s.docx' %str(order.number)
    # response['Content-Length'] = connect_lenght
    # response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'

    return steam.getvalue()



