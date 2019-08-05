from django.urls import path

urlpatterns = [
    path('', views.index, name='index' ),
    path('vrform', views.vrform, name='vrform'),
]
