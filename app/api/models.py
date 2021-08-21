from mongoengine import Document, fields


class Product(Document):
    name = fields.StringField(null=False)
    description = fields.StringField(null=True)
    options = fields.DictField(null=True)
