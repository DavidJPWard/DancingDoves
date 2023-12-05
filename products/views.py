from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category, Gender

# Create your views here. 

def all_products(request):

    products = Product.objects.all()
    query = None
    categories = None
    genders = None

    if request.GET:
        print(request.GET)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            print(categories)
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'gender' in request.GET:
            genders = request.GET['gender'].split(',')
            print(genders)
            products = products.filter(gender__genderValue__in=genders)
            genders = Gender.objects.filter(genderValue__in=genders)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "you didnt enter a search criteria.")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context={
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_genders': genders,
    }

    return render(request, 'products/products.html', context)

def product_detail(request, product_id):

    products = get_object_or_404(Product, pk=product_id)

    context={
        'product': products,
    }

    return render(request, 'products/product_detail.html', context)