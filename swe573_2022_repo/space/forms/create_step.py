from django import forms
from space.models import StepModel, SpaceModel
from django.shortcuts import redirect, render, get_object_or_404


class CreateStepModelForm(forms.ModelForm):
    def __init__(self, stepspace, **kwargs):
            super(CreateStepModelForm, self).__init__(**kwargs)
            if stepspace:
                self.fields['relatedresource'].queryset = StepModel.objects.filter(stepspace=stepspace)
    class Meta:
        model=StepModel
        fields= ('steptitle', 'stepcontent', 'relatedresource')