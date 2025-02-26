from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Note
from django.db.models import Q

class NoteListView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        field = request.GET.get('field', 'name')  # ค่าเริ่มต้นเป็น 'name'

        if query:
            if field == 'name':
                notes = Note.objects.filter(name__icontains=query)
            elif field == 'tags':
                notes = Note.objects.filter(tags__icontains=query)
            else:
                return Response({'error': 'Invalid search field'}, status=400)
        else:
            notes = Note.objects.all()

        notes_list = list(notes.values('id', 'name', 'file_url', 'thumbnail_url', 'tags', 'created_at', 'updated_at'))
        return Response(notes_list)
