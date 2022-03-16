from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from adopt_assignment.models import AdoptAssignment
from adopt_assignment.serializers import AssignmentSerializer, AssignmentCreateSerializer
from notice.paginations.Pagination import Pagination


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = AdoptAssignment.objects.all()

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AssignmentSerializer
        return AssignmentCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(assignment_no__icontains=query) or qs.filter(adopter_name__icontains=query) or qs.filter(animal__animal_reg_num__icontains=query) or qs.filter(user__nickname__icontains=query) or qs.filter(user__userID__icontains=query)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]



class AssignmentPagingViewSet(viewsets.ModelViewSet):
    queryset = AdoptAssignment.objects.all()
    pagination_class = Pagination

    def get_serializer_class(self):
        method = self.request.method
        if method == "GET":
            return AssignmentSerializer
        return AssignmentCreateSerializer

    def get_queryset(self):
        qs = super().get_queryset()

        query = self.request.query_params.get("query", "")
        if query:
            qs = qs.filter(assignment_no__icontains=query) or qs.filter(adopter_name__icontains=query) or qs.filter(animal__animal_reg_num__icontains=query) or qs.filter(user__nickname__icontains=query) or qs.filter(user__userID__icontains=query)

        return qs

    def get_permissions(self):
        method = self.request.method
        if method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
