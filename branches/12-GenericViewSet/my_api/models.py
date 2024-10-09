from django.db import models


# Create your models here.
class MenuItems(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)

    # class Meta:
    #     permissions = [
    #         ("view_document", "Can view document"),
    #         ("change_document", "Can change document"),
    #         ("delete_document", "Can delete document"),
    #     ]

    def __str__(self):
        return self.title
