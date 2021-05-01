from django.shortcuts import render,redirect
from CRUDoperations.form import customerForm

# Create your views here.
from CRUDoperations.models import customer


def insertdata(request):
    if request.method == 'GET':
        data=customerForm()
    elif request.method == 'POST':
        data = customerForm(request.POST)
        try:
            data.is_valid()
            data.save()
        except:
            data = customerForm()
        return render(request,'show.html')
    return render(request, 'index.html', {'form': data})


def show(request):
    obj = customer.objects.all()

    return render(request, 'show.html', {'d': obj})


def edit(request, id):

    obj = customer.objects.get(id=id)

    return render(request, 'edit.html', {'d': obj})

# def Update(request,id):


def delete(request,id):
    obj=customer.objects.get(id=id)
    obj.delete()
    return redirect('/show')
