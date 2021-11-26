from django.shortcuts import render
from django.apps import apps
from django.shortcuts import get_object_or_404
from django.forms import modelform_factory,inlineformset_factory

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

def get_model(num):
    mods = apps.get_models()  # все модели
    model_names = []
    models = []
    for mod in mods:
        if mod._meta.verbose_name[0].isupper():
            model_names.append(mod._meta.verbose_name)
            models.append(mod)
    return models[num]

def get_values_of_object(objects, object_fields ):
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

    selected_model = get_model(pk) # выбранная пользователем модель(тип данных)

    selected_model_fields = selected_model._meta.fields  # поля принадлежащие модели

    selected_model_objects = selected_model.objects.order_by('id')# все объекты выбранного типа данных отсортированные по id

    values_of_fields = get_values_of_object(selected_model_objects, selected_model_fields) #значения объекта

    return render(request, 'admin_panel/admin_table.html', {'selected_model_name': selected_model._meta.verbose_name,
                                                            'selected_model_objects': selected_model_objects,
                                                            'fields': selected_model_fields,
                                                            'values_of_fields': values_of_fields,
                                                            'tabnum': int(pk)}, )


def edit_table(request, pk, idd):
    selected_model = get_model(pk)  # выбранная пользователем модель(тип данных)
    selected_model_fields = selected_model._meta.fields  # поля принадлежащие модели

    temp = get_object_or_404(selected_model, pk=idd) # получаем объект выбранной модели
    obj = []
    for field in selected_model_fields:
        obj.append(getattr(temp, field.name))


    values_of_fields = []

    field_names = []
    for field in selected_model_fields:
        if field.editable:
            field_names.append(field.name)
    form = modelform_factory(selected_model, fields = field_names)
    print(form)
    return render(request, 'admin_panel/edit_table.html', {'selected_model_name': selected_model._meta.verbose_name,
                                                           'fields': selected_model_fields,
                                                           'values_of_fields': values_of_fields,
                                                           'obj': obj,
                                                           'tabnum': int(pk),
                                                           'form': form}, )