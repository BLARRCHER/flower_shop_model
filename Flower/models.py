from django.db import models


class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50, unique=True)
    role = models.ForeignKey('Role', on_delete=models.PROTECT, null=False)

    def __str__(self):
        return self.login


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=250)


class Flower(models.Model):
    seller = models.ForeignKey('User', on_delete=models.PROTECT)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=100)
    amount = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.type


class Feedback(models.Model):
    author = models.ForeignKey('User', on_delete=models.PROTECT, related_name='comments')
    object_seller = models.ForeignKey('User', on_delete=models.PROTECT, null=True, blank=True, related_name='reviews')
    object_product = models.ForeignKey('Flower', on_delete=models.PROTECT, null=True, blank=True)
    comment = models.TextField()

    def __str__(self):
        return self.comment


class Order(models.Model):
    seller = models.ForeignKey('User', on_delete=models.PROTECT, related_name='sells')
    customer = models.ForeignKey('User', on_delete=models.PROTECT, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.created


class OrderItem(models.Model):
    order = models.ForeignKey('Order', on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey('Flower', on_delete=models.PROTECT, related_name='order_items')
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.quantity


def do_your_job():
    seller_dict = []
    seller_and_buyers = User.objects.filter(role=1)
    for seller in seller_and_buyers:
        seller_dict.append({})
        seller_dict[-1].setdefault('login', seller.login)
        seller_dict[-1].setdefault('total_purchases', [])
        for sells in seller.sells.all():
            seller_dict[-1].setdefault('buyers_login', []).append(sells.customer.login)
            counter = [(price.quantity * price.product.price) for price in sells.items.all()]
            seller_dict[-1]['total_purchases'].append(counter)
