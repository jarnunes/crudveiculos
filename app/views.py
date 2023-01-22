import csv
import io

from commons.python.formatter import price, date_time, datetime_now_integer
from commons.python.helper import is_post_method, is_ajax, is_delete_method
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from django.contrib.auth.decorators import login_required
from app.python.form import VeiculoForm
from .models import Veiculo
from .python.constants import Const
from core.settings import LOGIN_URL
import json


@login_required(login_url=LOGIN_URL)
def listar_veiculos(request):
    query = request.GET.get('search')
    if query:
        veiculos = Veiculo.objects.filter(Q(marca__icontains=query)
                                          | Q(modelo__icontains=query)
                                          | Q(ano__exact=_to_int(query))).order_by('id')
    else:
        veiculos = Veiculo.objects.get_queryset().order_by('id')
    paginator = Paginator(veiculos, per_page=5)
    page_number = request.GET.get('page')
    veiculos = paginator.get_page(page_number)

    context = {'veiculos': veiculos}
    return render(request=request, template_name='app/listar-veiculo.html', context=context)


def _to_int(value):
    try:
        return int(value)
    except Exception as e:
        print(e)


@login_required(login_url=LOGIN_URL)
def cadastrar_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Veículo salvo com sucesso')
        return redirect('listar_veiculos')
    return render(request, template_name='app/veiculo.html', context={'form': form, 'edit': False})


@login_required(login_url=LOGIN_URL)
def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if is_post_method(request):
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            messages.success(request, 'Veículo salvo com sucesso')
            form.save()
            return redirect('listar_veiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, template_name='app/veiculo.html', context={'form': form, 'edit': True})


@login_required(login_url=LOGIN_URL)
def deletar_veiculo(request, id):
    if is_ajax(request=request):
        veiculo = get_object_or_404(Veiculo, id=id)
        msg = f'Veículo "{veiculo.marca}" removido com sucesso!'
        if veiculo and is_delete_method(request):
            veiculo.delete()
            messages.success(request, msg)
            return JsonResponse({'data': 1})


@login_required(login_url=LOGIN_URL)
def export_csv(request):
    response = HttpResponse(content_type=Const.CONTENT_TYPE_CSV)
    response['Content-Disposition'] = f'attachment; filename=veiculos_{datetime_now_integer()}.csv'

    writer = csv.writer(response)
    writer.writerow(Veiculo.get_all_fields_name())
    for vc in Veiculo.objects.all():
        writer.writerow([vc.id, vc.modelo, vc.marca, vc.ano, vc.valor, vc.data_cadastro])
    return response


@login_required(login_url=LOGIN_URL)
def export_pdf(request):
    # crate bytestream buffer
    buf = io.BytesIO()
    # create canvas
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    # create a text object
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)

    # Add Vehicles to pdf
    textob.textLine(f'Marca | Modelo | Ano | Valor R$ | Cadastro')
    for vc in Veiculo.objects.all():
        textob.textLine(
            f'{vc.marca} | {vc.modelo} | {vc.ano} | {price(vc.valor)} | {date_time(vc.data_cadastro)}')

    # Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=f'veiculos_{datetime_now_integer()}.pdf',
                        content_type=Const.CONTENT_TYPE_PDF)


@login_required(login_url=LOGIN_URL)
def obter_marca_veiculo(request, id):
    response = {'marca': None}

    if is_ajax(request):
        veiculo = get_object_or_404(Veiculo, id=id)
        response['marca'] = veiculo.marca
    return JsonResponse(data=response)


@login_required(login_url=LOGIN_URL)
def delete_all(request):
    if is_ajax(request) and is_post_method(request):
        ids = _get_ids_list(request)
        if len(ids) > 0:
            veiculos = Veiculo.objects.filter(id__in=ids)
            for veiculo in veiculos:
                veiculo.delete()
            messages.success(request, "Veiculos removidos com sucesso")
    return JsonResponse({'code': 0, 'message': 'Veiculos removidos com sucesso'})


def _get_ids_list(request):
    list_ids = []
    try:
        for id_value in str.split(json.loads(request.body).get('ids'), sep=','):
            list_ids.append(int(id_value))
    except Exception as error:
        raise Exception(error)

    return list_ids


def _to_list(value: str) -> list:
    return str.split(value)
