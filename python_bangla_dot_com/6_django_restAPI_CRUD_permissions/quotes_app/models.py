from django.db import models


# Create your models here.
class QuoteCategory(models.Model):
    #id  = IntegerField()
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Quote(models.Model):
    #id = IntegerField()
    quote = models.TextField()
    author = models.CharField(max_length=200)

    quote_category = models.ForeignKey(
        'QuoteCategory',
        on_delete = models.CASCADE
    )

    def __str__(self):
        if len(self.quote)>50:
            return self.quote[:50]+"..." #
        return self.quote
