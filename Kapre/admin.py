from django.contrib import admin
from .models import Customer
from .models import Category
from .models import Product
from .models import Cart
from .models import Payment
from .models import Review

# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Payment)
admin.site.register(Review)





