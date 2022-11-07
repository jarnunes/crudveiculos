import csv
import io

from commons.python.utils import Help, Format, Utils
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse, FileResponse, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from app.python.form import VeiculoForm
from .models import Veiculo
from .python.constants import Const


def listar_veiculos(request):
    query = request.GET.get('search')
    if query:
        veiculos = Veiculo.objects.filter(Q(marca__icontains=query) | Q(modelo__icontains=query))
    else:
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


def export_csv(request):
    response = HttpResponse(content_type=Const.CONTENT_TYPE_CSV)
    response['Content-Disposition'] = f'attachment; filename=veiculos_{Utils.datetime_now_integer()}.csv'

    writer = csv.writer(response)
    writer.writerow(Veiculo.get_all_fields_name())
    for vc in Veiculo.objects.all():
        writer.writerow([vc.id, vc.modelo, vc.marca, vc.ano, vc.valor, vc.data_cadastro])
    return response


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
            f'{vc.marca} | {vc.modelo} | {vc.ano} | {Format.price(vc.valor)} | {Format.date_time(vc.data_cadastro)}')

    # Finish up
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename=f'veiculos_{Utils.datetime_now_integer()}.pdf',
                        content_type=Const.CONTENT_TYPE_PDF)


def vehico(request):
    return render(request=request, template_name='app/vehico.html')
