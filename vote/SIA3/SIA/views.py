from django.shortcuts import render
from .forms import *
import csv,io
from django.http import HttpResponse
from dal import autocomplete

# Create your views here.
def create(request):
	if request.method=='POST':
		activityform=ActivityForm(request.POST)
		if activityform.is_valid():
			activityform.save()
			activity=Activity.objects.last()
		AIformset=Activity_interventionFormSet(request.POST)
		if AIformset.is_valid():
			AIformset.save(commit=False)
			for activityinterventionform in AIformset:
				activityinterventionform.activity=activity
				activityinterventionform.save()
		# PhaseFormset=PhaseFormset(request.POST)
		# if PhaseFormset.is_valid():
		# 	PhaseFormset.save(commit=False)
		# 	for phaseform in PhaseFormset:
		# 		phaseform.activity=activity
		# 		phaseform.save()
		return redirect("/")
	else:
		activityform=ActivityForm()
		AIformset=Activity_interventionFormSet(request.GET or None)
		# PhaseFormset=PhaseFormset(request.GET or None)
		return render(request,'SIA/create.html',{'activityform':activityform,'AIformset':AIformset})
		
def upload(request):

	if request.method=="GET":
		return render(request,"SIA/upload.html")
	csv_file=request.FILES['country']
	if not csv_file.name.endswith('.csv'):
		message.error(request,'This is not a csv file')
	data_set=csv_file.read().decode('UTF-8')
	io_string=io.StringIO(data_set)
	i=0
	next(io_string)
	for column in csv.reader(io_string,delimiter=',',quotechar='|'):
		_,created=Country.objects.update_or_create(
			iso3=column[0],
			country_name=column[1],
			WHO_region=column[2],
			UNICEF_region=column[3],
			)
	return HttpResponse("Success")


class CountryAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        if not self.request.user.is_authenticated:
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs