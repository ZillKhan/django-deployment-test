from django.shortcuts import render
from basicapp import forms
# Create your views here.

def index(request):
    return render(request,'basicapp/index.html')

def forms_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("text: "+form.cleaned_data['text'])
    return render(request,'basicapp/forms_page.html',{'form':form})
