from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
from django.template import RequestContext
from app.models import Combo, Componentes, Pedido
from app.forms import PedidoForm


def home(request):
    pedidos = Pedido.objects.all()
    form = PedidoForm()
    if request.method == 'GET':
        return render(request,'app/novo_pedido.html', {'form':form, 'pedidos':pedidos})
    elif request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            nome_combo = form.cleaned_data['combo']
            pedido = Pedido()
            combo = Combo()
            combo.nome = nome_combo
            combo.save()
            pedido.combo = combo
            constroi_combo(nome_combo=form.cleaned_data['combo'], combo=combo)
            pedido.nome_cliente = form.cleaned_data['nome_cliente']
            pedido.save()
            return HttpResponseRedirect('/')
        else:
            return render(request,'app/novo_pedido.html', {'form':form, 'pedidos':pedidos})
    

def constroi_combo(nome_combo, combo):
    COM_SUCO = "Combo com Suco"
    COM_REFRI = "Combo com Refrigerante"
    SUCO_BATATA = "Combo com Suco e batata"
    REFRI_BATATA = "Combo com Refrigerante e batata"
    SUCO_BATATA_BRINDE = "Combo com Suco, batata e brinde"
    REFRI_BATATA_BRINDE = "Combo com Refrigerante, batata e brinde"
    
    if nome_combo is COM_SUCO:
        combo.componentes.add(constroi_ham("Simples"))
        combo.componentes.add(constroi_bebida("Suco"))
        
    elif nome_combo is COM_REFRI:
        combo.componentes.add(constroi_ham("Simples"))
        combo.componentes.add(constroi_bebida("Refrigerante"))
        
    elif nome_combo is SUCO_BATATA:
        combo.componentes.add(constroi_ham("Completo"))
        combo.componentes.add(constroi_bebida("Suco"))
        combo.componentes.add(constroi_acompanhamento())
        
    elif nome_combo is REFRI_BATATA:
        combo.componentes.add(constroi_ham("Completo"))
        combo.componentes.add(constroi_bebida("Refrigerante"))
        combo.componentes.add(constroi_acompanhamento())
        
    elif nome_combo is SUCO_BATATA_BRINDE:
        combo.componentes.add(constroi_ham("Completo"))
        combo.componentes.add(constroi_bebida("Suco"))
        combo.componentes.add(constroi_acompanhamento())
        combo.componentes.add(constroi_brinde())
        
    else:
        combo.componentes.add(constroi_ham("Completo"))
        combo.componentes.add(constroi_bebida("Refrigerante"))
        combo.componentes.add(constroi_acompanhamento())
        combo.componentes.add(constroi_brinde())
    
    combo.save()
    return combo
    

def constroi_ham(nome):
    # nome é 'simples' ou 'completo'
    ham = Componentes()
    ham.nome = nome
    ham.tipo = Componentes.TiPO_COMPONENTE_COMBO[0]
    ham.save()
    return ham

def constroi_bebida(nome):
    # nome é 'suco' ou 'refri'
    bebida = Componentes()
    bebida.nome = nome
    bebida.tipo = Componentes.TiPO_COMPONENTE_COMBO[1]
    bebida.save()
    return bebida

def constroi_acompanhamento():
    acomp = Componentes()
    acomp.nome = "Batata"
    acomp.tipo = Componentes.TiPO_COMPONENTE_COMBO[2]
    acomp.save()
    return acomp

def constroi_brinde():
    brinde = Componentes()
    brinde.nome = "Brinquedo"
    brinde.tipo = Componentes.TiPO_COMPONENTE_COMBO[3]
    brinde.save()
    return brinde