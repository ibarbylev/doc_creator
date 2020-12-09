from django.db import models


class Doc(models.Model):
    doc_name = models.CharField(max_length=255)
    doc_template = models.CharField(max_length=255)
    doc_image = models.ImageField(upload_to='docs')
    doc_price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)

    def __str__(self):
        return self.doc_name

