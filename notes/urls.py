from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
    path('tags', views.render_all_tags, name='tags'),
    path('tag-notes', views.render_tag_notes, name='tag-notes')
]

