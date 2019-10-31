from rest_framework import serializers
from status.models import Status

"""
Serializers  ==> JSON
Serializers  ==> Validation like forms or Instead of form
"""


class StatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Status
        fields = [
            'id',
            'user',
            'content',
            'image'
        ]

    #  format of validate fields function is like below:
    # def validate_<field>(self, value):
    #     return something

    # def validate_content(self, value):
    #     if len(value) > 500:
    #         raise serializers.ValidationError('Content is longer than 500 character')
    #     return value

    def validate(self, data):
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get('image', None)

        if content is None and image is None:
            raise serializers.ValidationError('Content or Image is required')
        return data