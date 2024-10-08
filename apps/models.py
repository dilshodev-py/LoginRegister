from django.contrib.auth.models import AbstractUser
from django.db.models import Model, CharField


class User(AbstractUser):
    pass

class Category(Model):
    name = CharField(max_length=255)
    def __str__(self):
        return self.name


# center:
#     qahramon
#     daler
#     daniyor
#
#      1-17 talik
#
#
# left:
#     yulduz
#     behruz
#     mahsud
#     sarvinoz
#
#     2-(7,5)
#
# right:
#     umar
#     hasan
#     lochin
#
#     3-(13,3)