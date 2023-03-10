
from django.shortcuts import render
from rat_s.models import DadosPessoais
from rat_s.forms import DadosPessoaisForm


def index(request):
    return render(request,'rat/index.html')   

def cadastrar_prestador_view(request):
    form = DadosPessoaisForm()

    if request.method == 'POST':
        form = DadosPessoaisForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM')

    return render(request, 'rat/rat_s.html',{'form': form})




