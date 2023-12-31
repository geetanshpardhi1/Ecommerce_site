from django.shortcuts import render
from .models import Product,Order
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

#checkout view

def checkout(request):
    
    if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        city = request.POST.get('city',"")
        address = request.POST.get('address',"")
        state = request.POST.get('state',"")
        zip  = request.POST.get('zip',"")
        total = request.POST.get('total',"")
        
        orders = Order(items=items,name=name,email=email,city=city,address=address,state=state,zip=zip,total=total)
        orders.save()
        
    return render(request,'shop/checkout.html')
