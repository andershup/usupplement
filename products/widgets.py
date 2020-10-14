from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy as _ #we can now call it as _()

# copied from CI which inherits the built in one
class CustomClearableFileInput(ClearableFileInput): #we overide first with our own values in brackets
    clear_checkbox_label = _('Remove')
    initial_text = _('Current Image')
    input_text = _('')
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'