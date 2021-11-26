from django import forms
from bootstrap_modal_forms.generic import BSModalCreateView
import models

class objectForm(forms.ModelForm, selected_model):
    class Meta:
        model = selected_model

    template_name = 'templates/admin_table.html'
    form_class = models.User
    success_message = 'Success: Book was created.'
    success_url = reverse_lazy('index')