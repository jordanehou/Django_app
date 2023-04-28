from rest_framework import generics
from ..models import Subject
from .serializers import SubjectSerializer
# view for user to enroll
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Course
# handling authentication
from rest_framework.authentication import BasicAuthentication
# adding permission
from rest_framework.permissions import IsAuthenticated
# creating viewsets
from rest_framework import viewsets
from .serializers import CourseSerializer
from rest_framework.decorators import action
# view that mimics the behavior of the retrieve
from .permissions import IsEnrolled
from .serializers import CourseWithContentsSerializer


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

# view for user to enroll
class CourseEnrollView(APIView):
    # handling authentication
    authentication_classes = (BasicAuthentication,)
    # adding permission
    permission_classes = (IsAuthenticated,)
    def post(self, request, pk, format=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)
        return Response({'enrolled':True})

# creating viewsets
class CourseViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['post'], authentication_classes=[BasicAuthentication], permission_classes=[IsAuthenticated])
    def enroll(self, request, *args, **kwargs):
        course = self.get_object()
        course.students.add(request.user)
        return Response({'enrolled': True})
    
    @action(detail=True, methods=['get'], serializer_class=CourseWithContentsSerializer,authentication_classes=[BasicAuthentication], permission_classes=[IsAuthenticated, IsEnrolled])
    def contents(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)