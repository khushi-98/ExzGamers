from django.shortcuts import render

# filepath: /c:/Users/bansa/myblog/blog/views.py
from rest_framework import generics
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html')

def faq(request):
    return render(request, 'main/faq.html')

def feature(request):
    return render(request, 'main/feature.html')

def project(request):
    return render(request, 'main/project.html')

def service(request):
    return render(request, 'main/service.html')

def team(request):
    return render(request, 'main/team.html')

def testimonial(request):
    return render(request, 'main/testimonial.html')