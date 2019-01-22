from ..app import App
from .model import {{ cookiecutter.type_name }}Model, {{ cookiecutter.type_name }}Collection
from .modelui import {{ cookiecutter.type_name }}ModelUI, {{ cookiecutter.type_name }}CollectionUI
from .storage import {{ cookiecutter.type_name }}Storage


def get_collection(request):
    storage = {{ cookiecutter.type_name }}Storage(request)
    return {{ cookiecutter.type_name }}Collection(request, storage)


def get_model(request, identifier):
    col = get_collection(request)
    return col.get(identifier)


@App.path(model={{ cookiecutter.type_name }}Collection, 
          path='{{ cookiecutter.api_mount_path }}')
def _get_collection(request):
    return get_collection(request)


@App.path(model={{ cookiecutter.type_name }}Model, 
        path='{{ cookiecutter.api_mount_path }}/{identifier}')
def _get_model(request, identifier):
    return get_model(request, identifier)


@App.path(model={{ cookiecutter.type_name }}CollectionUI, 
        path='{{ cookiecutter.ui_mount_path }}')
def get_collection_ui(request):
    col = get_collection(request)
    return {{ cookiecutter.type_name }}CollectionUI(request, col)


@App.path(model={{ cookiecutter.type_name }}ModelUI, 
        path='{{ cookiecutter.ui_mount_path }}/{identifier}')
def get_model_ui(request, identifier):
    col = get_collection(request)
    model = get_model(request, identifier)
    return {{ cookiecutter.type_name }}ModelUI(request, model, {{ cookiecutter.type_name }}CollectionUI(request, col))
