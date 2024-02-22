from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, NoteSerializer, NoteHistorySerializer
from .models import *
from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class NoteAPI(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer
    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(user=user)


class CreateNoteAPI(generics.CreateAPIView):
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        user = User.objects.filter(id=self.request.user.id)
        print(self.request)
        print(user)
        serializer.save(user=user)

class NoteUpdateAPI(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def put(self, request, pk):
        user = User.objects.filter(id=self.request.user.id)
        note = Note.objects.filter(id=pk)
        
        note1 = note
        data = request.POST
        print(user.values()[0]['username'])
        note = note.values()[0]
        print(note)
        print(note1)
       
        changes = {"title": False, "description":False}
        text = {'tftf':""}
        if data["title"]!=note["title"]:
            changes["title"] = True

        if data["description"]!=note["description"]:
            changes["description"] = True

        print(changes)
        if changes['title']==True and changes['description']==True:
            text = "Title and description updated by" + " " + user.values()[0]['username']
        elif changes['title']==True and changes['description']==False:
            text = "Title updated by" + " " + user.values()[0]['username']
        elif changes['title']==False and changes['description']==True:
            text = "Description updated by" + " " + user.values()[0]['username']
        elif changes['title']==False and changes['description']==False:
            text = "No changes"
        Note.objects.filter(id=pk).update(title=data["title"], description=data["description"])
        NoteHistory.objects.create(user=user[0], note=note1[0], change=text)
        
        return HttpResponse("Note Updated")
    
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def share_note(request, **kwargs):
    note_id = request.POST["note_id"]
    user = User.objects.get(id=request.POST["user_id"])
    note = Note.objects.get(id=note_id)
    note.user.add(user)
    note.save()
    return HttpResponse("Note shared")

class NoteHistoryAPI(generics.ListAPIView):
    queryset = NoteHistory.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = NoteHistorySerializer