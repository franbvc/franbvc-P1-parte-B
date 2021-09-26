from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        new_note = Note(title=title, content=content)
        new_note.save()
        # TAREFA: Utilize o title e content para criar um novo Note no banco de dados
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id_to_delete = int(request.POST.get('delete'))
        Note.objects.get(id=id_to_delete).delete()
        
        return redirect('index')
    
    else:
        all_notes = Note.objects.all()
        print(request)
        return render(request, 'notes/note.html', {'notes': all_notes})

def update(request):
    if request.method == 'POST':
        id_to_update = int(request.POST.get('update'))

        note_to_update = Note.objects.get(id=id_to_update)
        note_to_update.title = request.POST.get('titulo')
        note_to_update.content = request.POST.get('detalhes')

        note_to_update.save()

        return redirect('index')
    
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/note.html', {'notes': all_notes})