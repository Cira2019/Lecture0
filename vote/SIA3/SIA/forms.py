from django import forms
from django.forms import ModelForm,formset_factory
from .models import *

class ActivityForm(ModelForm):
	class Meta:
		model=Activity
		fields=['country','year','phased_yesno','phase_total','comment','survey_done','survey_report_received','activity_name']
		widgets={'phased_yesno': forms.Select(attrs={'id': u'phased_yesno'}),}
class PhaseForm(ModelForm):
	class Meta:
		model=Phase
		fields=['activity','start_date','end_date','date_text','phase_no','phase_status','tr_received']

class Sub_activityForm(ModelForm):
	class Meta:
		model=Sub_activity
		fields=['phase','intervention','intervention_other','admin2','target_age','target_age_other',
		'target_population','target_population_source','population_reached','admin_coverage','survey_coverage','start_date','end_date']

class Activity_interventionForm(ModelForm):
	class Meta:
		model=Activity_intervention
		fields=['intervention','activity_type','extent','activity_status']
		labels={
		'intervention':'','activity_type':'','extent':'','activity_status':''
		}

Activity_interventionFormSet=formset_factory(Activity_interventionForm,extra=1)
PhaseFormSet=formset_factory(PhaseForm,extra=0)
