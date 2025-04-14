from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class DeviceControlTest(TestCase):
    def test_device_control(self):
        response = self.client.get(reverse('device_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Device List')
        self.assertTemplateUsed(response, 'device_list.html')