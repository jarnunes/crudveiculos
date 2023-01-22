from django import template
from app.models import Veiculo

register = template.Library()


@register.filter(name='get_ids')
def get_ids(veiculos):
    ids = []
    for v in veiculos.paginator.object_list:
        ids.append(v.id)
    return ids
