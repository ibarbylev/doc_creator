from django.db import models

from authentication.models import UserProfile
from docs.models import Doc


# class AvailableDocs(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     doc_name = models.ForeignKey(Doc, on_delete=models.CASCADE)


class Сustomer(models.Model):
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)


# class DocumentsJournal(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     doc_name = models.ForeignKey(Doc, on_delete=models.CASCADE)
#     principal = models.ForeignKey(Сustomer, on_delete=models.CASCADE)
#     attorney = models.ForeignKey(Сustomer, on_delete=models.CASCADE)
