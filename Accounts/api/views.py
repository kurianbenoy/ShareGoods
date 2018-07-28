from Accounts.models import Usernames
from .serializers import UserNameSerializer
from rest_framework import generics
from rest_framework.response import Response

class UserList(generics.ListCreateAPIView):
    queryset = Usernames.objects.all()
    serializer_class = UserNameSerializer

    def list(self, request):
    # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserNameSerializer(queryset, many=True)
        return Response(serializer.data)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usernames.objects.all()
    serializer_class = UserNameSerializer
