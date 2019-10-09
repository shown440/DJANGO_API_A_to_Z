# For serialize data
from django.core.serializers import serialize
import json

from django.conf import settings
from django.db import models

# Create your models here.

###################     Profile Update Model    #######################

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user=instance.user, filename=filename)


class UpdateQuerySet(models.QuerySet):

    def serialize(self):
        qs_list_with_values = list(self.values('id', 'user', 'content', 'image',)) # 'user', 'content', 'image', 'updated'
        # print(qs_list_with_values)
        return json.dumps(qs_list_with_values)  # serialize("json", qs, fields=('user', 'content', 'image')) # , fields=('user', 'content', 'image')


class UpdateManager(models.Manager):

    def get_queryset(self):
        return UpdateQuerySet(self.model, using=self._db)


class Update(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_update_image, blank=True, null=True)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = UpdateManager()

    def __str__(self):
        return self.content or ""

    def serialize(self):
        try:
            image = self.image.url
        except:
            image = ""
            
        data = {
            "content": self.content,
            "user": self.user.id,
            "image": image,
            # "updated": self.updated
        }

        data = json.dumps(data)
        #print(type(json_list[0]["fields"]))

        return data