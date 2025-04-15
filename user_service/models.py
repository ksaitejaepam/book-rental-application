from tortoise.models import Model
from tortoise import fields

class User(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.CharField(max_length=255)
    rented_books = fields.JSONField(default=[])

    class Meta:
        table = "users"
