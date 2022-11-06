from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest, JsonResponse
from app.python.form import VeiculoForm
from .models import Veiculo
from .python.utils import Help


def listar_veiculos(request):
    query = request.GET.get('search')
    if query:
        veiculos = Veiculo.objects.filter(marca__contains=query)
        return render(request, template_name='app/listar-veiculo.html', context={'veiculos': veiculos})

    veiculos = Veiculo.objects.all()
    paginator = Paginator(veiculos, per_page=5)
    page_number = request.GET.get('page')
    veiculos = paginator.get_page(page_number)

    context = {'veiculos': veiculos}
    return render(request=request, template_name='app/listar-veiculo.html', context=context)


def cadastrar_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Veículo salvo com sucesso')
        return redirect('listar_veiculos')
    return render(request, template_name='app/veiculo.html', context={'form': form, 'edit': False})


def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if Help.is_post_method(request):
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            messages.success(request, 'Veículo salvo com sucesso')
            form.save()
            return redirect('listar_veiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, template_name='app/veiculo.html', context={'form': form, 'edit': True})


def deletar_veiculo(request, id):
    if Help.is_ajax(request=request):
        veiculo = get_object_or_404(Veiculo, id=id)
        msg = f'Veículo "{veiculo.marca}" removido com sucesso!'
        if veiculo and Help.is_delete_method(request):
            veiculo.delete()
            messages.success(request, msg)
            return JsonResponse({'data': 1})
