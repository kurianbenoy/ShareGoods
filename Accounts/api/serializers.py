from rest_framework import serializers

from Accounts.models import Usernames

class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usernames
        fields = ('__all__')
