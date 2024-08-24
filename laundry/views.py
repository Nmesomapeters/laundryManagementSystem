from django.shortcuts import  render, redirect, get_object_or_404
from django.contrib import messages
from .form import AddServiceForm, AddToCartForm, AddServiceToCartForm, CheckoutForm,  ProductForm
from .models import Cart, ServiceCart, Checkout, Product, Order
from payment.models import Wallet

def home(request):
    context = {}
    return render(request, 'laundrySys/home.html', context)

def add_service(request):
    if request.method == 'POST':
        form = AddServiceForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()
            messages.info(request, 'New Service added successfully.')
            return redirect('add-service')
        else:
            messages.warning(request, 'Oops! Something went wrong.')
            return redirect('add-service')
    else:
        form = AddServiceForm()
        context = {'form':form}
        return render(request, 'laundrySys/add_service.html', context)

def add_to_cart(request):
    if request.method == 'POST':
        form = AddToCartForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            var.save()

            request.session['cart_id'] = var.id

            return redirect('add-service-to-cart')
        else:
            messages.warning(request, 'Oops! Something went wrong.')
            return redirect('add-to-cart')
    else:
        form = AddToCartForm()
        context = {'form':form}
        return render(request, 'laundrySys/add_to_cart.html', context)
    

def add_services_to_cart(request):
    if request.method == 'POST':
        form = AddServiceToCartForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            cart = Cart.objects.get(id=request.session['cart_id'])
            var.cart = cart
            var.save()
            update_cart_total_amount(cart)
            messages.info(request, 'Service added to cart.')
            return redirect('add-service-to-cart')
        else:
            messages.warning(request, 'Oops! Something went wrong.')
            return redirect('add-service-to-cart')
    else:
        form = AddServiceToCartForm()
        cart = Cart.objects.get(id=request.session['cart_id'])
        get_obj = ServiceCart.objects.filter(cart=cart)
        context = {'form': form, 'get_obj': get_obj, 'cart': cart}
        return render(request, 'laundrySys/add_service_to_cart.html', context)

def delete_service_from_cart(request, pk):
    get_obj = ServiceCart.objects.get(pk=pk)
    get_obj.delete()
    cart = Cart.objects.get(id=request.session['cart_id'])
    update_cart_total_amount(cart)
    messages.warning(request, 'Service has been removed from cart')
    return redirect('add-service-to-cart')

def update_cart_total_amount(cart):
    get_obj = ServiceCart.objects.filter(cart=cart)
    total_amount = sum(obj.service.price * cart.total_clothes() for obj in get_obj)
    cart.total_amount = total_amount
    cart.save()

def checkout_here(request):
    cart = Cart.objects.get(id=request.session['cart_id'])
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.cart = cart
            var.save()
            context = {'cart': cart}
            return render(request, 'payment/make_payment_from_wallet.html', context)
        else:
            messages.warning(request, 'Oops! Something went wrong.')
            return redirect('checkout-here')
    else:
        form = CheckoutForm()
        get_obj = ServiceCart.objects.filter(cart=cart)
        context = {'form': form, 'cart': cart, 'get_obj': get_obj}
        return render(request, 'laundrySys/checkout_here.html', context)

def pay_for_laundry(request):
    cart = Cart.objects.get(id=request.session['cart_id'])
    wallet = Wallet.objects.get(user=request.user)
    total_amount = cart.total_amount  # The total amount should be already calculated

    if wallet.balance >= total_amount:
        wallet.balance -= total_amount
        cart.is_verified = True
        cart.save()
        wallet.save()
        messages.info(request, 'Payment completed! You can now proceed to take your clothes')
        return redirect('home')
    else:
        messages.warning(request, 'Sorry, Insufficient Funds in your wallet')
        return redirect('history')


def completed_payment(request):
    obj = Checkout.objects.filter(cart__is_verified=True)
    context = {'obj':obj}
    return render(request, 'laundrySys/completed_payment.html', context)


def services(request):
    return render(request, 'laundrySys/services.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('add-product')
        else:
            messages.warning(request, 'Oops! Something went wrong.')
    else:
        form = ProductForm()
    return render(request, 'laundrySys/add_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'laundrySys/product_list.html', {'products': products})

def mark_complete(request, id):
    checkout = get_object_or_404(Checkout, id=id)
    checkout.status = 'Completed'
    checkout.save()
    return redirect('order_history') 

def mark_delivered(request, id):
    checkout = get_object_or_404(Checkout, id=id)
    checkout.status = 'Delivered'
    checkout.save()
    return redirect('order_history') 

def order_history(request):
    orders = Order.objects.all()
    return render(request, 'order_history.html', {'orders': orders})