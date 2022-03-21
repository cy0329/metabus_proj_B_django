from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from lost_pet_board.models import LostPetBoard, LostPetBoardImage
from lost_pet_board.serializers import LostPetBoardSerializer, LostPetBoardCreateSerializer
from lost_pet_board.serializers import LostPetBoardImageSerializer, LostPetBoardImageCreateSerializer
from notice.paginations.Pagination import Pagination


class LostPetViewSet(viewsets.ModelViewSet):
    queryset = LostPetBoard.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return LostPetBoardSerializer
        return LostPetBoardCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        location = self.request.query_params.get("location", "")
        if location:
            qs = qs.filter(lost_location__icontains=location)

        animaltype = self.request.query_params.get("animaltype", "")
        if animaltype:
            qs = qs.filter(animal_type__icontains=animaltype)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class LostPetBoardImageViewSet(viewsets.ModelViewSet):
    queryset = LostPetBoardImage.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return LostPetBoardImageSerializer
        return LostPetBoardImageCreateSerializer

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
