from django.shortcuts import render
from .forms import DadosPessoaisForm

def cadastrar_prestador_view(request):
    if request.method == 'POST':
        form = DadosPessoaisForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'sucesso.html')
    else:
        form = DadosPessoaisForm()
    return render(request, 'rat_s.html', {'form': form})


