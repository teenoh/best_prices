from django.db import models
from django.utils.html import format_html

# Create your models here.

class JumiaItem(models.Model):
    brand = models.CharField(max_length=200)
    discount = models.IntegerField()
    image = models.CharField(max_length=200)
    is_global = models.BooleanField(default=False)
    link = models.CharField(max_length=300)
    name = models.CharField(max_length=200)
    sku = models.CharField(max_length=200)
    latest_price = models.IntegerField()

    def image_preview(self):
        if self.image:
            html = f"""
                <a target='_blank' href='{self.link}'> <img src={self.image} style='height: 80px' /> </a>
                <br />
            """
            return format_html(html)
        return None

    def __str__(self):
        return self.name


class PriceLog(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    amount =  models.IntegerField()
    item = models.ForeignKey(JumiaItem, related_name='prices', on_delete=models.CASCADE)

    def __str__(self):
        return self.item.name + '_' + str(self.date)

