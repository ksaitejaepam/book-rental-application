from tortoise.models import Model
from tortoise import fields

class Book(Model):
    id = fields.UUIDField(pk=True)
    title = fields.CharField(max_length=255)
    author = fields.CharField(max_length=255)
    genre = fields.CharField(max_length=100)
    available_copies = fields.IntField()

    class Meta:
        table = "books"

    def __str__(self):
        return self.title
