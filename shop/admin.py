from django.contrib import admin
from .models import  ProductImages,Product,User,Payment
from django.utils.html import format_html
from instamojo_wrapper import Instamojo
from fullecomm.settings import PAYMENT_API_AUTH_TOKEN,PAYMENT_API_KEY 
from django.contrib import messages

API = Instamojo(api_key=PAYMENT_API_KEY,
                auth_token=PAYMENT_API_AUTH_TOKEN,endpoint='https://test.instamojo.com/api/1.1/')



# Register your models here.

# for seeing images form in Product Form
class ProductImageModel(admin.StackedInline):
    model=ProductImages

class ProductModel(admin.ModelAdmin):
    list_display=['id','name','get_description','get_price','get_descount','get_sale_price','get_thumbnail']
    inlines=[ProductImageModel]

    def get_thumbnail(self,obj):
        return format_html(f'''
            <img height="80px" src="{obj.thumbnail.url}">
        ''')

    def get_sale_price(self,obj):
        return ((obj.price)-(obj.price*(obj.descount/100)))

    def get_description(self,obj):
        # return obj.description[0:30]+"..."
        # if we want to return as html
        return format_html(f'<span title="{obj.description}"><b>{obj.description[0:30]+"...."}</b>')

    def get_price(self,obj):
        return '₹ '+str(obj.price)
    
    def get_descount(self,obj):
        return str(obj.descount)+' %'

    get_sale_price.short_description="Sale Price"
    get_descount.short_description="Discount"
    get_price.short_description="Price"
    

class UserModel(admin.ModelAdmin):
    list_display=['id','name','phone','active','email']
    sortable_by=['id','name']
    list_editable=['active']
    
class PaymentModel(admin.ModelAdmin):
    list_display=['id','get_product','get_user','payment_request_id','payment_id','get_status','get_ammount']

    def get_user(self,obj):
        return format_html(f'''
            <a target="_blank" href="/admin/shop/user/{obj.user.id}/change/">{obj.user.name}</a>
        ''')
    def get_product(self,obj):
        return format_html(f'''
            <a target="_blank" href="/admin/shop/product/{obj.name.id}/change/">{obj.name.name}</a>
        ''')

    def get_status(self,obj):
        response=response = API.payment_request_payment_status(obj.payment_request_id, obj.payment_id)
        print(response)
        obj.paymentdetails=response
        if obj.status!="Failed":
            return True
        else:
            return False

    
    def get_ammount(self,obj):
        return obj.paymentdetails['payment_request']['amount']


    get_user.short_description="User"
    get_product.short_description="Product"
    get_status.short_description="status"
    get_status.boolean=True
    

# admin.site.register(ProductImages,ProductImageModel)
admin.site.register(Product,ProductModel)
admin.site.register(User,UserModel)
admin.site.register(Payment,PaymentModel)

