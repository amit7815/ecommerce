from django import template

register=template.Library();


@register.filter(name='rupee')
def addRupeeSign(value):
    return f"₹ {value}"

@register.filter(name='sale_price')
def getsaleprice(product):
    return (product.price-(product.price*(product.descount/100)))