from django.shortcuts import render, redirect

def gestionnaire_parc_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Gestionnaire Parc').exists():
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'page_erreur/401.html')
    return wrapped_view

def employe_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Employe').exists():
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'page_erreur/401.html')
    return wrapped_view

def gestionnaire_intervention_required(view_func):
    def wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Gestionnaire Intervention').exists():
            return view_func(request, *args, **kwargs)
        else:
            return render(request, 'page_erreur/401.html')
    return wrapped_view
