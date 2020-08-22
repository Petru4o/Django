from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

User = get_user_model()


# **********
# 1 Category
# 2 Product
# 3 CartProduct
# 4 Cart
# 5 Order
# 6 Customer
# 7 Specific


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name category')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        abstract = True

    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Product name')
    slug = models.SlugField(unique=True)
    image = models.ImageField(verbose_name="Image")
    description = models.TextField(verbose_name="Description")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Price")

    def __str__(self):
        return self.title


class CartProduct(models.Model):
    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Total price")

    def __str__(self):
        return "Cart product {}".format(self.product.title)


class Cart(models.Model):
    owner = models.ForeignKey('Customer', verbose_name='Owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
    total_products = models.PositiveIntegerField(default=8)
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="Total price")

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name="Phone")
    address = models.CharField(max_length=255, verbose_name="Address")

    def __str__(self):
        return "User: {} {}".format(self.user.first_name, self.user.last_name)

class Notebook(Product):
    diagonal = models.CharField(max_length=255, verbose_name="Diagonal")
    display = models.CharField(max_length=255, verbose_name="Display type")
    processor = models.CharField(max_length=255, verbose_name="Processor")
    ram = models.CharField(max_length=255, verbose_name="RAM")
    video = models.CharField(max_length=255, verbose_name="Videocard")
    time_without_charge = models.CharField(max_length=255, verbose_name="Working time")

    def __str__(self):
        return  "{} : {}".format(self.category.name, self.title)

class Smartphone(Product):
    diagonal = models.CharField(max_length=255, verbose_name="Diagonal")
    display = models.CharField(max_length=255, verbose_name="Display type")
    resolution = models.CharField(max_length=255, verbose_name="Resolution")
    accum_volume = models.CharField(max_length=255, verbose_name="Acumulator")
    ram = models.CharField(max_length=255, verbose_name="RAM")
    sd = models.BooleanField(default=True)
    sd_volume_max = models.CharField(max_length=255, verbose_name="Max volume sd")
    main_can_mp = models.CharField(max_length=255, verbose_name="Main camera")
    frontal_can_mp = models.CharField(max_length=255, verbose_name="Frontal camera")

    def __str__(self):
        return  "{} : {}".format(self.category.name, self.title)