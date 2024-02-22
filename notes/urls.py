from django.urls import path
from rest_framework.authtoken import views
from .views import *


urlpatterns = [
    path('notes/', NoteAPI.as_view(), name='notes'),
    path('signup/', RegisterView.as_view(), name='register'),
    path('login/', views.obtain_auth_token),
    path('notes/create/', CreateNoteAPI.as_view(), name='create'),
    path('notes/<str:pk>/', NoteUpdateAPI.as_view(), name='update'),
    path('note/share/', share_note, name='share'),
    path('notes/version-history/<str:pk>/', NoteHistoryAPI.as_view(), name='history')
]