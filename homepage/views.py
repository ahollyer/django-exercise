from django.template.response import TemplateResponse
import datetime

def homepage (request):
    context = {
        # 'page_title': 'HOME Page',
        'name': 'Aspen',
        'now': datetime.datetime.now(),
        'numbers': [1, 2, 3, 4]

    }
    return TemplateResponse(request, 'homepage.html', context)

def contact (request):
    context = {}
    return TemplateResponse(request, 'contact.html', context)
