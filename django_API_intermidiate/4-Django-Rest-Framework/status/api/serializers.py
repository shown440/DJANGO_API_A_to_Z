from rest_framework import serializers
from status.models import Status

"""
Serializers  ==> JSON
Serializers  ==> Validation like forms or Instead of form
"""


class StatusSerializer(serializers.ModelSerializers):

    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]