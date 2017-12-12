from rest_framework import generics
from rest_framework.response import Response

from accounts.models import Profile
from accounts.serializers import UserSerializer
from reservations.serializers.favorites import FavoriteSerializer
from restaurants.models import Restaurant
from restaurants.serializers import RestaurantListSerializer


class RestaurantFavoriteToggle(generics.GenericAPIView):
    queryset = Restaurant.objects.all()

    def post(self, request, *args, **kwargs):
        instance = self.get_object()
        user = request.user
        if user.profile.favorites.filter(pk=instance.pk):
            user.profile.favorites.remove(instance)
            favorite_status = False
        else:
            user.profile.favorites.add(instance)
            favorite_status = True
        data = {
            'user': UserSerializer(user).data,
            'Restaurant': RestaurantListSerializer(instance).data,
            'result': favorite_status,
        }
        return Response(data)


class CustomerFavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        queryset = Profile.objects.filter(user=self.request.user)
        return queryset
