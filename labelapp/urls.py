from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>/', views.showall, name='showall'),
    # path('<str:username>/<str:label>/', views.)
    path('<str:username>/add/', views.addView, name='addView'),
    path('<str:username>/<str:label>/update/', views.modifyView, name='modifyView'),
    # path('<str:username>/<str:label>/delete/', views.deleteView, name='deleteView'),
    path('', views.entry, name="entry"),
]
