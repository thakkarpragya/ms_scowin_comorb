from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import Student_reaction
from .serializers import StudentReactionSerializer
from rest_framework.response import Response

# Create your views here.

class StudentsVacReact(ListCreateAPIView):
    queryset = Student_reaction.objects.all()
    serializer_class = StudentReactionSerializer

class StudentsVacReactDetails(RetrieveUpdateDestroyAPIView):
    queryset = Student_reaction.objects.all()
    serializer_class = StudentReactionSerializer

