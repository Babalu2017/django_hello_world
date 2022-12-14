from multiprocessing import context
import re
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items' : items
    }
    return render(request, 'todo/todo_list.html', context)
    # return HttpResponse("Hello!")


def add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Item.objects.create(name=name, done=done)
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form' : form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        # name = request.POST.get('item_name')
        # done = 'done' in request.POST
        # Item.objects.create(name=name, done=done)
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form' : form
    }
    return render(request, 'todo/edit_item.html', context)

