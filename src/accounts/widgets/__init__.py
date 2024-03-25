from django.forms.widgets import TextInput

class InputFieldWidget(TextInput):
    # default_template = 'widgets/input-form-tabs.html'

    def custom_name(self, name):
        return name.split('_')[0].strip()

    def render(self, name, value, attrs=None, renderer=None):
        return super().render(
            name, value,
            attrs={'class': 'form-control mt mt-field-field-en mt-default'}, renderer=renderer
            )


'''
from django.forms.widgets import TextInput
from django.template.loader import render_to_string

class InputFieldWidget(TextInput):
    default_template = 'widgets/input-form.html'

    def preprocess_label(self, label):
        # Remove brackets and their contents
        return label.split('[')[0].strip()

    def render(self, name, value, attrs=None, renderer=None):
        label = self.preprocess_label(self.label)
        label_html = render_to_string(self.default_template, {'name': name, 'label': label})
        input_html = super().render(name, value, attrs={'class': 'form-control'}, renderer=renderer)
        return f'{label_html}{input_html}'
'''