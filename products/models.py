from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import post_save
from django.util import slugfly



# Create your models here.
class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self.db)

    def all(self, *args, **kwargs):
        return self.get_queryset().active()


class Product(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False )
    discription = models.TextField(max_length=4000, null=True, blank=True)
    price    = models.DecimalField(decimal_places=2,max_digits=20, default=99.99)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk":self.pk})


class Variation(models.Model):
    product = models.ForeignKey(Product)
    title = models.CharField(max_length=120, null=False, blank=False)
    discription = models.TextField(null=True, blank=True)
    price    = models.DecimalField(decimal_places=2,max_digits=20)
    sale_price    = models.DecimalField(decimal_places=2,max_digits=20, null=True, blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_price(self):
        if sale_price is None:
            return self.price
        else:
            return self.sale_price

    def get_absolute_url(self):
        return self.product.get_absolute_url()



#此function是要在product的資料儲存後，自動新增一筆預設的價格檔
#如要的效果是資料儲存前就自動新增的話，可以使用pre_seve
def product_saved_recevier(sender, instance, created, *args, **kwargs):

    product = instance
    variations = product.variation_set.all()
    if variations.count() == 0:
        new_vari = Variation()
        new_vari.product = product
        new_vari.title = "Default"
        new_vari.price = product.price
        new_vari.save()


post_save.connect(product_saved_recevier, sender=Product)


def image_upload_to(instance, filename):
    title = instance.product.title
    slug = slugfly(title)
    return "products/%s/%s" %(slug, filename)

class ProductImage(models.Model):
    product = models.ForeignKey(Product)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.product.title
