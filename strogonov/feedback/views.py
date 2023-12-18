from django.shortcuts import render
from feedback.models import Comment
from . serializers import CommentSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet

class CommentSetFilter(FilterSet):
    class Meta:
        model = Comment
        fields = ['avalible']

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    model = Comment
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend,]  
    filterset_class  = CommentSetFilter

