from django.db import models
#from partial_date import PartialDateField #has a problem with a package called six


class Country(models.Model):
	iso3=models.CharField(max_length=3)
	country_name=models.CharField(max_length=50)
	WHO_region=models.CharField(max_length=20,null=True)
	UNICEF_region=models.CharField(max_length=20,null=True)
	def __str__(self):
		return f"{self.country_name}"
	class Meta:
		verbose_name_plural='Countries'

class Status(models.Model):
	status=models.CharField(max_length=20)
	def __str__(self):
		return f"{self.status}"

class Intervention(models.Model):
	intervention=models.CharField(max_length=50)
	def __str__(self): 
		return f"{self.intervention}"

class Activity_type(models.Model):
	activity_type=models.CharField(max_length=30)
	#intervention=models.ForeignKey(Intervention,null=True,blank=True,on_delete=models.SET_NULL,related_name="activity_types")
	standard_age_group=models.CharField(max_length=50,null=True,blank=True)
	definition=models.CharField(max_length=1500,null=True)
	intervention=models.ManyToManyField(Intervention,blank=True,related_name="activity_types")
	def __str__(self):
		return f"{self.activity_type}"

##to be decided
class Age(models.Model):
	age_group=models.CharField(max_length=30)
	intervention=models.ManyToManyField(Intervention,blank=True,related_name="age")
	def __str__(self):
		return f"{self.age_group}"

class Extent(models.Model):
	extent=models.CharField(max_length=30)
	def __str__(self):
		return f"{self.extent}"

class Target_population_source(models.Model):
	source=models.CharField(max_length=30)
	def __str__(self):
		return f"{self.source}"


class Area(models.Model):
	PLACE_ID=models.CharField(max_length=50)
	EFF_STARTDATE=models.DateTimeField()
	EFF_ENDDATE=models.DateTimeField()
	LEVEL=models.IntegerField()
	TITLE=models.CharField(max_length=60)
	ISO_2_CODE=models.CharField(max_length=2)
	ISO_3_CODE=models.CharField(max_length=3)
	ADM0_NAME=models.CharField(max_length=100)
	ADM1_NAME=models.CharField(max_length=100)
	ADM2_NAME=models.CharField(max_length=100)
	ADM0_TITLE=models.CharField(max_length=100)
	ADM1_TITLE=models.CharField(max_length=100)
	ADM2_TITLE=models.CharField(max_length=100)
	WHO_REGION=models.CharField(max_length=30)
	UNICEF_REG=models.CharField(max_length=30)
	SHAPE_WHO_GUID=models.CharField(max_length=50)
	CENTER_LON=models.CharField(max_length=30)
	CENTER_LAT=models.CharField(max_length=30)
	IS_CURRENT=models.CharField(max_length=6,null=True)
	def __str__(self):
		return f"{self.TITLE}"

class YesNo(models.Model):
	yesno=models.CharField(max_length=10)
	def __str__(self):
		return f"{self.yesno}"

class Activity(models.Model):
	activity_name=models.CharField(max_length=64)
	country=models.ForeignKey(Country,null=True,blank=True,on_delete=models.SET_NULL,related_name="activities")
	phased_yesno=models.ForeignKey(YesNo,null=True,blank=True,on_delete=models.SET_NULL,related_name="activities")
	phase_total=models.IntegerField()
	comment=models.CharField(max_length=500,blank=True)
	survey_done=models.BooleanField()
	survey_report_received=models.BooleanField()
	year=models.IntegerField(blank=True,null=True)

	def __str__(self):
		return f"{self.activity_name}"

class Phase(models.Model):
	activity=models.ForeignKey(Activity,on_delete=models.CASCADE,related_name="phases")
	start_date=models.DateField()
	end_date=models.DateField()
	date_text=models.CharField(max_length=150,blank=True)
	phase_no=models.IntegerField()
	phase_status=models.ForeignKey(Status,null=True,blank=True,on_delete=models.SET_NULL,related_name="phases")
	tr_received=models.BooleanField()
	def __str__(self):
		return f"{self.activity.activity_name} Phase {self.phase_no}"

class Sub_activity(models.Model):
	phase=models.ForeignKey(Phase,on_delete=models.CASCADE,related_name="sub_activities")
	intervention=models.ForeignKey(Intervention,null=True,blank=True,on_delete=models.SET_NULL,related_name="sub_activities")
	intervention_other=models.CharField(max_length=255)
	admin2=models.ManyToManyField(Area,blank=True,related_name="sub_activities")
	target_age=models.ForeignKey(Age,null=True,blank=True,on_delete=models.SET_NULL,related_name="sub_activities")
	target_age_other=models.CharField(max_length=50)
	target_population=models.IntegerField()
	target_population_source=models.ForeignKey(Target_population_source,null=True,blank=True,on_delete=models.SET_NULL,related_name="sub_activities")
	population_reached=models.IntegerField()
	admin_coverage=models.DecimalField(max_digits=6, decimal_places=2)
	survey_coverage=models.DecimalField(max_digits=6, decimal_places=2)
	start_date=models.DateField()
	end_date=models.DateField()
	def __str__(self):
		return f"Phase {self.phase.phase_no} {self.intervention}"

class Activity_intervention(models.Model):
	intervention=models.ForeignKey(Intervention,null=True,blank=True,on_delete=models.SET_NULL,related_name="activity_interventions")
	activity_type=models.ForeignKey(Activity_type,null=True,blank=True,on_delete=models.SET_NULL,related_name="activity_interventions")
	extent=models.ForeignKey(Extent,null=True,blank=True,on_delete=models.SET_NULL,related_name="activity_interventions")
	#activity_status=models.ForeignKey(Status,null=True,blank=True,on_delete=models.SET_NULL,related_name="activity_interventions")
	activity=models.ForeignKey(Activity,null=True,blank=True,on_delete=models.SET_NULL,related_name="activity_interventions")
	# def __str__(self):
	# 	return f"{self.activity.activity_name} {self.intervention} {self.extent}"
