from django.shortcuts import render
from django.apps import apps
from django.shortcuts import get_object_or_404
from django.forms import modelform_factory,inlineformset_factory
from django.forms.models import fields_for_model
class Counter:
    count = 0

    def increment(self):
        self.count += 1
        return ''

    def decrement(self):
        self.count -= 1
        return ''

    def double(self):
        self.count *= 2
        return ''
from django.forms import ModelForm
from django.forms.models import model_to_dict
from django.template.loader import render_to_string
from django.http import JsonResponse



def get_model(num):
    mods = apps.get_models()  # все модели
    model_names = []
    models = []
    for mod in mods:
        if mod._meta.verbose_name[0].isupper():
            model_names.append(mod._meta.verbose_name)
            models.append(mod)
    return models[num]

def get_values_of_objects(objects, object_fields ):
    values = []
    for obj in objects:
        print(obj)
        temp = []
        for field in object_fields:
            temp.append(getattr(obj, field.name))
        values.append(temp)
    return values



def main_admin_panel(request):
    mods = apps.get_models()  # все модели
    model_names = []
    for mod in mods:
        if mod._meta.verbose_name[0].isupper():
            model_names.append(mod._meta.verbose_name)

    counter = Counter()

    return render(request, 'admin_panel/main_admin_list_page.html', {'table_names': model_names, 'counter': counter})

def admin_current_table(request, pk):
    context = {}
    selected_model = get_model(pk) # выбранная пользователем модель(тип данных)

    selected_model_fields = selected_model._meta.fields  # поля принадлежащие модели

    selected_model_objects = selected_model.objects.order_by('id')# все объекты выбранного типа данных отсортированные по id

    values_of_fields = get_values_of_objects(selected_model_objects, selected_model_fields) #значения объекта

    field_names = []  # имена полей(столбцов таблицы)

    if request.method == "POST":
        obj_id = request.POST.get('object_id')

        for field in selected_model_fields:  # получаем список имён полей для генерации формы
            if field.editable:
                field_names.append(field.name)

        temp_form = modelform_factory(selected_model,
                                      fields=field_names)  # Форма для выбранного объекта, может используется для создания новой формы, поэтому temp
        obj = get_object_or_404(selected_model, pk=obj_id)  # получаем объект выбранной модели
        form = temp_form(instance=obj)
        modal_context = {
            'form': form,
            'user': request.user,
            'obj' : obj,
        }
        result = render_to_string('includes/modal_change_object.html', modal_context)
        return JsonResponse({'result': result})

    context['selected_model_name'] = selected_model._meta.verbose_name
    context['selected_model_objects'] = selected_model_objects
    context['fields'] = selected_model_fields
    context['values_of_fields'] = values_of_fields
    context['tabnum'] = int(pk)

    return render(request, 'admin_panel/admin_table.html', context, )


def edit_table(request, pk, idd):
    print("я вызвался")
    selected_model = get_model(pk)  # выбранная пользователем модель(тип данных)
    selected_model_fields = selected_model._meta.fields  # поля принадлежащие модели

    obj = get_object_or_404(selected_model, pk=idd) # получаем объект выбранной модели
    for field in selected_model_fields: # получаем список имён полей для генерации формы
        if field.editable:
            field_names.append(field.name)

    temp_form = modelform_factory(selected_model, fields=field_names)#Форма для выбранного объекта, может используется для создания новой формы, поэтому temp
    form = temp_form(instance=obj)
    if request.method == "POST":
        print("edefewfwefweg AUE")
        form = temp_form(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()

    return render(request, 'admin_panel/edit_table.html', {'selected_model_name': selected_model._meta.verbose_name,
                                                           'fields': selected_model_fields,
                                                           'tabnum': int(pk),
                                                           'form': form,
                                                           'obj': obj}, )