from django.urls import path, include
from .views import getPsychologistList, getPyschologistById, createPyschologist, updatePsychologist, deletePsychologist


urlpatterns = [
    path('psychologists/', getPsychologistList, name='psychologist-list'),
    path('psychologists/<int:pk>/', getPyschologistById, name='psychologist-detail'),
    path('psychologists/create/', createPyschologist, name='psychologist-create'),
    path('psychologists/update/<int:pk>/', updatePsychologist, name='psychologist-update'),
    path('psychologists/delete/<int:pk>/', deletePsychologist, name='psychologist-delete'),
]