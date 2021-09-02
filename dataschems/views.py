from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView

from dataschems.forms import ModelSchemaForm
from dataschems.models import ModelSchema


# Create your views here.

# class ViewsDataSchema(ListView):
#     template_name = 'schemas_tables.html'
#     model = ModelSchema

@login_required
def schema_views(request):
    schems = ModelSchema.objects.filter(creator=request.user)
    content = {'schems': schems, 'title': 'User datalist'}

    return render(request, 'schemas_tables.html', content)


class ModelSchemaCreateView(CreateView):
    model = ModelSchema
    template_name = 'schema_create.html'
    form_class = ModelSchemaForm

    # success_url = reverse_lazy('users:profile')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Schemas registration'
        return context

    # @method_decorator(user_passes_test(lambda u: u.is_superuser))
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)


# ==============================================================================

@login_required()
def schema_remove(request, b_id):
    ModelSchema.objects.get(id=b_id).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required()
def schema_edit(request, p_id, quantity):
    if request.is_ajax():
        basket = ModelSchema.objects.get(id=p_id)
        if quantity > 0:
            basket.quantity = quantity
            basket.save()
        else:
            basket.delete()

        baskets = ModelSchema.objects.filter(user=request.user)
        context = {'baskets': baskets}
        result = render_to_string('schemas_tables.html', context)
        return JsonResponse({'result': result})
