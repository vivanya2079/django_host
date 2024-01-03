from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Filter_Price(models.Model):
    FILTER_PRICE = [
        ('1000 TO 10000', '1000 TO 10000'),
        ('10000 TO 20000', '10000 TO 20000'),
        ('20000 To 30000', '20000 To 30000'),
        ('30000 TO 40000', '30000 TO 40000'),
        ('40000 TO 50000', '40000 TO 50000')
    ]
    price = models.CharField(choices=FILTER_PRICE, max_length=60)


    def __str__(self):
        return self.price
class Product(models.Model):
    CONDITION = [('New', 'New'), ('Old', 'Old')]
    STOCK = [('IN STOCK', 'IN STOCK'), ('OUT OF STOCK', 'OUT OF STOCK')]
    STATUS = [('Publish', 'Publish'), ('Draft', 'Draft')]
    
    unique_id = models.CharField(unique=True, max_length=200, null=False)
    image = models.ImageField(upload_to='product_images/img')
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    condition = models.CharField(choices=CONDITION, max_length=100)
    information = models.TextField()
    description = models.TextField()
    stock = models.CharField(choices=STOCK, max_length=200)
    status = models.CharField(choices=STATUS, max_length=200)
    created_date = models.DateTimeField(default=timezone.now)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    filter_price = models.ForeignKey(Filter_Price, on_delete=models.CASCADE)


    def __str__(self):
        return self.name




    def save(self, *args, **kwargs):
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('%Y%m%d23') + str(self.id)
        return super().save(*args, **kwargs)
class Images (models.Model):
    image= models. ImageField(upload_to='product_images/img')
    product =models.ForeignKey(Product ,on_delete=models.CASCADE)
class Tag(models. Model):
    name =models.CharField(max_length= 288)
    product =models.ForeignKey (Product,on_delete=models.CASCADE)

###CONTACT PAGE:
class Contact_us(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=200)
    message=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email 

#####CHECKOUT PAGE(ORDER)))#######
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    address = models.TextField()
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=250)
   
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust max_digits and decimal_places as needed
    payment_id=models.CharField(max_length=300,null=True,blank=True)
    paid=models.BooleanField(default=False,null=True)
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    product=models.CharField(max_length=250)
    image=models.ImageField(upload_to='Product_image/Order')
    quantity=models.CharField(max_length=250)
    price=models.CharField(max_length=100)
    total=models.CharField(max_length=250)


    def __str__(self):
        return self.order.user.username




