from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    
    products = Product.objects.all()
    
    #search code
    productname = request.GET.get('productname')
    if productname != '' and productname is not None:
        products = Product.objects.filter(product_name__icontains=productname) 
    
    #paginator code     
    paginator = Paginator(products,'4')
    page = request.GET.get('page')
    products = paginator.get_page(page)
    
       
    return render(request,'shop/index.html',{'product_objects':products})

#detail view 
def detail(request,id):
    product  = Product.objects.get(id=id)
    return render(request,'shop/detail.html',{'product':product})