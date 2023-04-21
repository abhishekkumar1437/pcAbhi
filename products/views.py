
from django.shortcuts import render
from django.conf import settings
import json
from django.views.decorators.csrf import csrf_exempt
from myFirstProject.settings import RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET
import razorpay
from products.constant import PaymentStatus
from .models import Category,image,Order

# Create your views here.
def payment(request):
    return render(request,'payment.html')
def home(request):
    category=Category.objects.all().values()
    categories={
        'category':category,
    }
    return render(request,'home.html',categories)
    


def show_category(request,pkid):
    show_categ=Category.objects.get(pk=pkid)
    categ=Category.objects.all()
    images=image.objects.filter(cate=show_categ)
    category_data={
        'imgs':images,
        'category':categ,
    }
    return render(request,'home.html',category_data)
    


def order_payment(request):
        if request.method == "POST":
            name = request.POST.get("name")
            amount = request.POST.get("price")
            product_id=request.POST.get("product_id")
            payment_id=request.POST.get("oder_id")
            
            
            client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
            razorpay_order = client.order.create(
                {"amount": amount, "currency": "INR", "payment_capture": "1"}
            )
            order = Order.objects.create( name=name, amount=amount)
            order.save()
            return render(request,"pay.html",{
                    "callback_url": "http://" + "127.0.0.1:8000" + "callback/",
                    "razorpay_key": RAZORPAY_KEY_ID,
                    "order": order,
                },
            )
        return render(request, "pay.html")


@csrf_exempt
def callback(request):
    def verify_signature(response_data):
        client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))
        return client.utility.verify_payment_signature(response_data)

    if "razorpay_signature" in request.POST:
        payment_id = request.POST.get("razorpay_payment_id", "")
        provider_order_id = request.POST.get("razorpay_order_id", "")
        signature_id = request.POST.get("razorpay_signature", "")
        order = Order.objects.all()
        order.payment_id = payment_id
        order.signature_id = signature_id
        order.save()
        if not verify_signature(request.POST):
            order.status = PaymentStatus.SUCCESS
            order.save()
            return render(request, "callback.html")
        else:
            order.status = PaymentStatus.FAILURE
            order.save()
            return render(request, "callback.html", context={"status": order.status})
    else:
        payment_id = json.loads(request.POST.get("error[metadata]")).get("payment_id")
        provider_order_id = json.loads(request.POST.get("error[metadata]")).get(
            "order_id"
        )
        order = Order.objects.get(provider_order_id=provider_order_id)
        order.payment_id = payment_id
        order.status = PaymentStatus.FAILURE
        order.save()
        return render(request, "callback.html", context={"status": order.status})