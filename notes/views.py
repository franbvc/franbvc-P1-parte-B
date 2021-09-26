from django.shortcuts import render, redirect
from .models import Note, Tag


def render_all_notes(request):
    all_notes = Note.objects.all()
    return render(request, 'notes/note.html', {'notes': all_notes})

def render_all_tags(request):
    all_tags = Tag.objects.all()
    return render(request, 'notes/tag.html', {'tags': all_tags})

def verify_tag_existence(tag_title):
    if Tag.objects.filter(title=tag_title).exists():
        return True
    return False

def create_new_tag(tag_title):
    tag = Tag(title=tag_title)
    tag.save()
    return tag

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag_title = request.POST.get('tag')

        if tag_title == "":
            new_note = Note(title=title, content=content)
            new_note.save()
            return redirect('index')

        if verify_tag_existence(tag_title):
            tag = Tag.objects.get(title=tag_title)
        else:
            tag = create_new_tag(tag_title)

        new_note = Note(title=title, content=content, tag=tag)
        new_note.save()

        return redirect('index')

    else:
        return render_all_notes(request)

def delete(request):
    if request.method == 'POST':
        id_to_delete = int(request.POST.get('delete'))
        Note.objects.get(id=id_to_delete).delete()
        
        return redirect('index')
    
    else:
        print(request)
        return render_all_notes(request)

def update(request):
    if request.method == 'POST':
        id_to_update = int(request.POST.get('update'))

        note_to_update = Note.objects.get(id=id_to_update)
        note_to_update.title = request.POST.get('titulo')
        note_to_update.content = request.POST.get('detalhes')

        note_to_update.save()

        return redirect('index')
    
    else:
        return render_all_notes(request)


def render_tag_notes(request):
    tag_title = request.GET.get('tag')
    tag = Tag.objects.get(title=tag_title)
    tag_notes = Note.objects.filter(tag=tag.id)
    return render(request, 'notes/tag_notes.html', {'tag': tag_notes, 'tag_title': tag_title})
