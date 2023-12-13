from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import *
from django.db.models import F
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
import logging
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

logger = logging.getLogger(__name__)

def product(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
           
            selected_option1 = request.POST.get('option1')
            selected_option2 = request.POST.get('option2')
            selected_option3 = request.POST.get('option3')

            selected_option4 = request.POST.get('option4')
            selected_option5 = request.POST.get('option5')
            selected_option6 = request.POST.get('option6')
            wzrost = request.POST.get('wzrost')
            
            price = request.POST.get('priceSend')

            product_name = str(selected_option1)+str(selected_option2)+str(selected_option3)
            try:
                product = Product.objects.get(name=product_name)
                product_id = product.pk
            except Product.DoesNotExist:
                product_id = None

            user = request.user
            product = Product.objects.get(pk=product_id)  

            item, created = UserItem.objects.get_or_create(
                        product=product, user=user, height=wzrost, hand=selected_option4, size=selected_option5, 
                        drawer=selected_option6, price=price, shredder=selected_option3, water=selected_option2
                    )
            if not created:
                item.quantity = F('quantity') + 1
                item.save()

            messages.success(request, ("Produkt został dodany do koszyka."))
            return redirect('/product/')

        else:
            messages.success(request, ("Zaloguj się, aby dodać do koszyka."))
            return redirect('/product/')

    products = Product.objects.all()
    product = Product.objects.all().order_by('id').first()

    context = {'products':products, 'product':product}
    return render(request, 'product.html', context)

def cart(request):
    if request.user.is_authenticated:
        user = request.user
        if UserItem.objects.filter(user=user).exists():
            products = UserItem.objects.filter(user=user)

            if request.method == 'POST':
                product_pk = request.POST.get('delete_product')
                item = UserItem.objects.filter(pk=product_pk)
                item.delete()

            total = sum(
                product.price for product in products
            )

            context = {'products':products, 'total':total}
        else:
            return redirect('/cartBlank/')
    else:
        return redirect('/cartBlank/')
    
    return render(request, 'cart.html', context)

def cartBlank(request):
    return render(request, 'cartBlank.html')

def order(request):

    user = request.user
    products = UserItem.objects.filter(user=user)
    total = sum(
                product.price for product in products
            )
    
    context = {'products':products, 'total':total}

    if request.method == 'POST':
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        street = request.POST.get('street')
        number = request.POST.get('number')
        city = request.POST.get('city')
        postcode = request.POST.get('postcode')
        delivery_method = request.POST.get('delivery')
        price = request.POST.get('priceSend')

        try:
            validate_email(email)
        except ValidationError as e:
            user = request.user
            products = UserItem.objects.filter(user=user)
            total = sum(product.price for product in products)
            context = {'products': products, 'total': total}
            messages.error(request, "Niepoprawny adres email!")
            return render(request, 'order.html', {'message': 'message', **context})
        
        context = {'products':products, 'total':total, 'totalPrice':price}

        user = request.user

        item = Order(user=user, name=name, surname=surname, email=email, telephone=telephone,
                        street=street, number=number, city=city, postcode=postcode, delivery_method=delivery_method)
        item.save()
 
        subject = 'ZAMÓWIENIE'
        message = render_to_string("orderEmail.html", {
            'user': request.user.username,
            'products': UserItem.objects.filter(user=user),
            'total': sum(product.total_price for product in products),
            'order': Order.objects.filter(user=user).order_by('-id').first(),
            'totalPrice': price
            })

        from_email = 'foczkiSklep@gmail.com'
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=False)

        messages.success(request, ("Dziękujemy za złożenie zamówienia."))

        UserItem.objects.filter(user=user).delete()
        return redirect('/home/')

    return render(request, 'order.html', context)