from django import forms
from ERP.models import Project, TipoProyectoDetalle, DocumentoFuente, Estimate, ProgressEstimateLog, LogFile
from datetime import datetime
from django.utils.safestring import mark_safe
from Logs.controller import Logs
import os
from django.conf import settings

class TipoProyectoDetalleAddForm(forms.ModelForm):
    class Meta:
        model = TipoProyectoDetalle
        fields = '__all__'

    def save(self, commit=True):
        instance = super(TipoProyectoDetalleAddForm, self).save(commit=False)
        if instance.id is not None:  # Revisa si existe ese objeto
            a = TipoProyectoDetalle.objects.filter(id=instance.id).first()
            Logs.log(a.documento.name, "Mensaje")
            if a.documento.name != "":  # revisa si tiene una foto asignada

                if instance.documento.name != a.documento.name:  # revisa si cambio la foto asignada

                    route = settings.MEDIA_ROOT + "/" + a.documento.name  # borra la anterior y pon la nueva
                    try:
                        os.remove(route)
                    except Exception as e:
                        print e
        return super(TipoProyectoDetalleAddForm, self).save(commit)

class AddProyectoForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = '__all__'


    def save(self, commit=True):
        instance = super(AddProyectoForm, self).save(commit=False)

        return super(AddProyectoForm, self).save(commit=commit)

class DocumentoFuenteForm(forms.ModelForm):
    class Meta:
        model = DocumentoFuente
        fields = "__all__"

    def save(self, commit=True):
        print "OVERAID"
        instance = super(DocumentoFuenteForm, self).save(commit=False)

        if instance.id is not None:  # Revisa si existe ese objeto
            a = DocumentoFuente.objects.filter(id=instance.id).first()

            if a.documento.name != "":  # revisa si tiene una foto asignada

                if instance.documento.name != a.documento.name:  # revisa si cambio la foto asignada
                    route = settings.MEDIA_ROOT + "/" + a.documento.name  # borra la anterior y pon la nueva
                    print route
                    try:
                        os.remove(route)
                    except Exception as e:
                        print e

        return super(DocumentoFuenteForm, self).save(commit)




'''
    Forms for the progress estimate.
'''
class EstimateForm(forms.ModelForm):

    line_item_filter = forms.IntegerField(label="Partida")

    def save(self, commit=True):
        line_item_filter = self.cleaned_data.get('line_item_filter', None)
        # ...do something with extra_field here...
        return super(EstimateForm, self).save(commit=commit)

    class Meta:
        model = Estimate
        fields = "__all__"



'''
    Forms for the progress estimate log.
'''
class ProgressEstimateLogForm(forms.ModelForm):
    class Meta:
        model = ProgressEstimateLog
        fields = "__all__"




'''
    Forms for the log file form.
'''
class LogFileForm(forms.ModelForm):
    class Meta:
        model = LogFile
        fields = "__all__"