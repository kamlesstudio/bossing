from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from rest_framework.response import Response
from .models import Comment



@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return Response({'business': self.object, 'form':form}, template_name='detail_view.html')

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return Response({'business': self.object, 'form':form}, template_name='detail_view.html')