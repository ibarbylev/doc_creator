from django.db import models

from authentication.models import User
from docs.models import Doc


# class AvailableDocs(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     doc_name = models.ForeignKey(Doc, on_delete=models.CASCADE)


class Сustomer(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    def __str__(self):
        return f'for owner {str(self.owner).upper()}: {self.first_name}.{self.last_name}'


# class DocumentsJournal(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
#     doc_name = models.ForeignKey(Doc, on_delete=models.CASCADE)
#     principal = models.ForeignKey(Сustomer, on_delete=models.CASCADE)
#     attorney = models.ForeignKey(Сustomer, on_delete=models.CASCADE)
