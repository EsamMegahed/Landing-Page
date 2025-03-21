from rest_framework import viewsets
from.models import Comment
from.serializers import CommentSerializer

class CommentViewsets(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer