from django.shortcuts import render
from django.apps import apps


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

def main_admin_panel(request):
    mods = apps.get_models() #все модели
    model_names = []
    for mod in mods:
        if mod._meta.verbose_name[0].isupper():
            model_names.append(mod._meta.verbose_name)

    counter = Counter()

    return render(request, 'admin_panel/main_admin_list_page.html', {'table_names':model_names, 'counter':counter})

def admin_current_table(request, pk):
    mods = apps.get_models()  # все модели
    model_names = []
    models = []
    for mod in mods:
        if mod._meta.verbose_name[0].isupper():
            model_names.append(mod._meta.verbose_name)
            models.append(mod)

    selected_model = models[pk]# выбранная пользователем модель(тип данных)
    selected_model_objects = selected_model.objects.all()#все объекты выбранного типа данных
    selected_model_fields = selected_model._meta.fields#поля принадлежащие модели

    values_of_fields = []
    for obj in selected_model_objects:
        print(obj)
        temp = []
        for field in selected_model_fields:
            temp.append(getattr(obj, field.name))
        values_of_fields.append(temp)

    return render(request, 'admin_panel/admin_table.html', {'selected_model_name':selected_model._meta.verbose_name,
                                                            'selected_model_objects':selected_model_objects,
                                                            'fields':selected_model_fields,
                                                            'values_of_fields':values_of_fields,}, )
