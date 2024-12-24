from django.urls import path
from .views import index, about, contact, faq, feature, project, service, team, testimonial, BlogPostListCreateView, BlogPostDetailView

urlpatterns = [
    path('posts/', BlogPostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post-detail'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('faq/', faq, name='faq'),
    path('feature/', feature, name='feature'),
    path('project/', project, name='project'),
    path('service/', service, name='service'),
    path('team/', team, name='team'),
    path('testimonial/', testimonial, name='testimonial'),
]