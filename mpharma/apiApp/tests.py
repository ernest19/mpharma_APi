
from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework import status

from apiApp.models import icdCode 
from .serializers import CdicodeSerializer




class ModelTestCase(TestCase):
	"""This class defines the test suite for the dxcodelist model."""

	def setup(self):
		"""Define the test client and other test variables."""
		self.category_code='ZS220'
		self.diagnosis_code=3
		self.full_code='ZY2100'
		self.abbreviated_description='Salmonella pyelonephritis'
		self.full_description='Shigellosis due to Shigella sonnei'
		self.category_title='Shigellosis due to Shigella sonnei'
		self.dxcodelist = icdCode(category_code=self.category_code,diagnosis_code=self.diagnosis_code,full_code=self.full_code,abbreviated_description=self.abbreviated_description,full_description=self.full_description,category_title=self.category_title)

	def test_model_create_a_dxcode(self):
		"""Test the dxcodelist model can create a dxcodelist."""
		old_count = icdCode.objects.count()
		self.dxcodelist.save()
		new_count = icdCode.objects.count()
		self.assertNotEqual(old_count, new_count)








def test_api_get_a_dxcode(self):
		"""Test the api can get a given dxcodelist."""
		dxcodelist = icdCode.objects.get()
		response = self.client.get(
			reverse('details',
			kwargs={'pk': dxcodelist.full_code}), format="json")

		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, dxcodelist)

def test_api_update_dxcode(self):
	"""Test the api can update a given dxcodelist."""
	change_dxcodelist = {'category_code': 'ZS220'}
	res = self.client.put(
		reverse('details', kwargs={'pk': dxcodelist.full_code}),
		change_dxcodelist, format='json'
	)
	self.assertEqual(res.status_code, status.HTTP_200_OK)

def test_api_delete_dxcode(self):
	"""Test the api can delete a dxcodelist."""
	dxcodelist = icdCode.objects.get()
	response = self.client.delete(
		reverse('details', kwargs={'pk': dxcodelist.full_code}),
		format='json',
		follow=True)
	self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
