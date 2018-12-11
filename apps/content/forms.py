# -*- coding: utf-8 -*-
from django import forms
from diseases.models import Disease
from .models import Content
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class ContentModelForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    image_url = forms.CharField(widget=forms.URLInput)
    
    def __init__(self, *args, **kwargs):
        super(ContentModelForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'save'))

    class Meta:
        model = Content
        fields = ['title','description','image_url','content_type','diseases','complications','gender','race','age_level','reading_level','smoking_status','alcohol_status','activity_level','share_period']
# class ContentForm(forms.Form):
#     title = forms.CharField()

#     description = forms.CharField(
#         widget = forms.Textarea(),
#     )

#     image_url = forms.CharField()

#     content_type = forms.ChoiceField(
#         choices = (
#             ('Text', "Some users are better suited to text content"), 
#             ('Graphic', "Some users like graphics most"),
#             ('Video', "Other users like video content")
#         ),
#         widget = forms.RadioSelect,
#         initial = 'Text',
#     )

#     radio_buttons = forms.ChoiceField(
#         choices = (
#             ('option_one', "Option one is this and that be sure to include why it's great"), 
#             ('option_two', "Option two can is something else and selecting it will deselect option one")
#         ),
#         widget = forms.RadioSelect,
#         initial = 'option_two',
#     )

#     diseases = forms.MultipleChoiceField(
#         choices = (
#             ('CVD', "Select this if the option is relevant all users with the above disease"), 
#             ('Diabetes', 'Select this if the option is relevant to all users with the above disease'),
#         ),
#         initial = 'option_one',
#         widget = forms.CheckboxSelectMultiple,
#         # help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#     )
#     complications = forms.MultipleChoiceField(
#         choices = (
#             ('Smoking', "Select this if the option is relevant all users with the selected diseases and the listed complications"), 
#             ('Diabetes', 'Select this if the option is relevant to all users with the selected diseases and the listed complications'),
#         ),
#         initial = 'Diabetes',
#         widget = forms.CheckboxSelectMultiple,
#         # help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#     )

#     gender = forms.MultipleChoiceField(
#         choices = (
#             ('Male', "Content relevant to males"), 
#             ('Female', 'Content relevant to females'),
#         ),
#         initial = 'Male',
#         widget = forms.CheckboxSelectMultiple,
#         # help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#     )
#     race = forms.MultipleChoiceField(
#         choices = (
#             ('American Indian or Alaska Native', "Select this if the option is relevant all users with the selected diseases and the listed complications"), 
#             ('Asian', 'Select this if the option is relevant to all users with the selected diseases and the listed complications'),
#             ('Black or African American', 'Select this if the option is relevant to all users with the selected diseases and the listed complications'),
#             ('Asian', 'Select this if the option is relevant to all users with the selected diseases and the listed complications'),
#             ('Asian', 'Select this if the option is relevant to all users with the selected diseases and the listed complications'),
#             ('Asian', 'Select this if the option is relevant to all users with the selected diseases and the listed complications'),
#         ),
#         initial = 'Diabetes',
#         widget = forms.CheckboxSelectMultiple,
#         # help_text = "<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",
#     )

#     appended_text = forms.CharField(
#         help_text = "Here's more help text"
#     )

#     prepended_text = forms.CharField()

#     prepended_text_two = forms.CharField()

#     multicolon_select = forms.MultipleChoiceField(
#         choices = (('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')),
#     )

#     # Uni-form
#     helper = FormHelper()
#     helper.form_class = 'form-horizontal'
#     helper.layout = Layout(
#         Field('text_input', css_class='input-xlarge'),
#         Field('textarea', rows="3", css_class='input-xlarge'),
#         'radio_buttons',
#         Field('checkboxes', style="background: #FAFAFA; padding: 10px;"),
#         AppendedText('appended_text', '.00'),
#         PrependedText('prepended_text', '<input type="checkbox" checked="checked" value="" id="" name="">', active=True),
#         PrependedText('prepended_text_two', '@'),
#         'multicolon_select',
#         FormActions(
#             Submit('save_changes', 'Save changes', css_class="btn-primary"),
#             Submit('cancel', 'Cancel'),
#         )
#     )
