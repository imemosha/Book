"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from demo_app import views
from demo import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard),
    path('', views.list_art, name ='list_articles'),
    path('add_article/', views.add_article, name='add_article'),
    path('edit_article/<int:id>/', views.edit_article, name='edit_article'),
    path('delete_article/<int:id>/', views.delete_article, name ='delete_article'),
    path('list_author/', views.list_author, name='list_author'),
    path('add_author/', views.add_author, name='add_author'),
    path('edit_author/<int:id>/',views.edit_author, name='edit_author'),
    path('delete_author/<int:id>/', views.delete_author, name= 'delete_author'),
    path('detail_author/<int:id>/', views.detail_author, name='detail_author'),
    path('api/article_detail/<int:id>/', csrf_exempt(views.ArticleAPIView.as_view())),
    path('api/article_detail/', csrf_exempt(views.MultiArticleAPIView.as_view())),
    path('add_comics/', views.AddComics.as_view(), name='add_comics'),
    path('list_comics/', views.ListComics.as_view(), name='list_comics'),
    path('edit_comics/<int:pk>/', views.UpdateComics.as_view(), name='edit_comics')



]

urlpatterns+= static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
