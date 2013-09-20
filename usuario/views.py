# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import UsuarioForm
from models import Usuario

def index(request):
    return render_to_response("index.html")

def formulario(request):
        if request.method == 'POST':
            form = UsuarioForm(request.POST, request.FILES)
            
            if form.is_valid():
                nome = form.cleaned_data['nome']
                email = form.cleaned_data['email']
                senha = form.cleaned_data['senha']
                idade = form.cleaned_data['idade']
                profissao = form.cleaned_data['profissao']
                salario = form.cleaned_data['salario']
                tipopessoa = form.cleaned_data['tipopessoa']
                cpf_cnpj = form.cleaned_data['cpf_cnpj']
                p = Usuario(nome=nome, email=email,senha=senha, idade=idade, profissao=profissao, salario=salario, tipopessoa=tipopessoa, cpf_cnpj=cpf_cnpj)
                p.save()

                return render_to_response("salvo.html", {})
        else:
                form = UsuarioForm()
                

        return render_to_response("formulario.html", {'form' : form}, context_instance=RequestContext(request))
    
def lista(request):
    usuarios = Usuario.objects.all()
    print usuarios
    return render_to_response("lista.html", {'usuarios': usuarios} )
    #return render_to_response("formulario.html", {'form' : form}, context_instance=RequestContext(request))
