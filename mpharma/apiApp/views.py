from __future__ import unicode_literals

import csv, urllib

from django.shortcuts import render,HttpResponse


from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from celery.decorators import task
from celery import shared_task
from celery.task.schedules import crontab
from celery.decorators import periodic_task


from apiApp.models import IcdCode
from .serializers import IcdcodeSerializer





class LargeResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
  


class IcdcodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed,update,delete.
    """
    queryset = IcdCode.objects.all().order_by('-full_code')
    serializer_class = IcdcodeSerializer
    pagination_class = LargeResultsSetPagination



# """
# Function that reads the csv file from github and update the database every 15 minutes.
# """
@shared_task
@periodic_task(run_every=(crontab(minute='*/15')))
def CsvView():
	try:
		data = "https://raw.githubusercontent.com/kamillamagna/ICD-10-CSV/master/codes.csv"
		webpage = urllib.urlopen(data)
		datareader = csv.reader(webpage)
		for row in datareader:
			check=icdCode.objects.filter(category_code=row[0],diagnosis_code=row[1],full_code=row[2],abbreviated_description=row[3],full_description=row[4],category_title=row[5]).count()
			if check<1:
				icd=IcdCode()
				icd.category_code=row[0]
				icd.diagnosis_code=row[1]
				icd.full_code=row[2]
				icd.abbreviated_description=row[3]
				icd.full_description=row[4]
				icd.category_title=row[5]
				icd.save()
	except Exception as e:
		pass
		print "an error occured when updating database"

	
	return HttpResponse("updates done ")