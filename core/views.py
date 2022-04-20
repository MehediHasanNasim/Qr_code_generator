from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from core import models
from .models import Clients, Client_certificate
from django.views.generic import ListView


from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


def home(request):
    diction = {}
    return render(request, 'home.html', context=diction)


def clients(request):
    client_list = Clients.objects.all().order_by('client_name')
    diction = {
        'client_list': client_list
    }
    return render(request, 'clients.html', context=diction)


def client_info(request, id):
    client = Clients.objects.filter(pk=id)
    if client:
        client = Clients.objects.get(pk=id)
    diction = {'client': client}
    print('client')
    return render(request, 'client_info.html', context=diction)


# def project_update(request, project_id):
#     project_info = Project.objects.get(pk=project_id)
#     update_form = form.ProjectForm(instance=project_info)

#     if request.method =="POST":
#         update_form = form.ProjectForm(request.POST, instance=project_info)

#         if update_form.is_valid():
#             update_form.save(commit=True)
#             return projects(request)

#     diction = {'update_form': update_form}
#     return render (request, 'core/project_update.html', context=diction)

class ClientListView(ListView):
    model = Client_certificate
    template_name = 'main.html'
    
def client_render_pdf_view(request, *arg, **kwargs):
    pk = kwargs.get('pk')
    client = get_object_or_404(Client_certificate, pk=pk)
    
    template_path = 'pdf2.html'
    context = {'client': client}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display:
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response







# def render_pdf_view(request):
#     template_path = 'pdf1.html'
#     context = {'myvar': 'this is your template context'}
#     # Create a Django response object, and specify content_type as pdf
#     response = HttpResponse(content_type='application/pdf')
#     # if download:
#     # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
#     # if display:
#     response['Content-Disposition'] = 'filename="report.pdf"'
#     # find the template and render it.
#     template = get_template(template_path)
#     html = template.render(context)

    # # create a pdf
    # pisa_status = pisa.CreatePDF(
    #    html, dest=response)
    # # if error then show some funy view
    # if pisa_status.err:
    #    return HttpResponse('We had some errors <pre>' + html + '</pre>')
    # return response


