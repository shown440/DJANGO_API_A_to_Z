from django.conf import settings
from django.db import models

# Create your models here.

def upload_status_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass
    # def serialize(self):
    #     qs_list_with_values = list(self.values('id', 'user', 'content', 'image',)) # 'user', 'content', 'image', 'updated'
    #     # print(qs_list_with_values)
    #     return json.dumps(qs_list_with_values)  # serialize("json", qs, fields=('user', 'content', 'image')) # , fields=('user', 'content', 'image')


class StatusManager(models.Manager):

    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Status(models.Model): 
    # Thsi model like: fb status, instagram post, tweet, linkedin post

    user            = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content         = models.TextField(blank=True, null=True)
    image           = models.ImageField(upload_to=upload_status_image, blank=True, null=True) # Django Storage = AWS S3
    updated         = models.DateTimeField(auto_now=True)
    timestamp       = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:50]

    class Meta:
        # managed = False
        db_table = "Status"
        
        verbose_name = 'Status post'
        verbose_name_plural = 'Status posts'
