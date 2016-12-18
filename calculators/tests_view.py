from django.test import Client, TestCase
from django.core.urlresolvers import reverse


class ViewTests(TestCase):

    def setUp(self):
        self.client = Client()

    def test_bmi_calculator_main_page_1(self):
        response = self.client.get(reverse('calculators:main_bmi'))
        self.assertEqual(response.status_code, 200)

    def test_bmi_calculator_main_page_2(self):
        response = self.client.get(reverse('calculators:main_bmi'))
        self.assertEqual(response.context["sex"], ("kobieta", "mężczyzna"))

    def test_bmi_calculator_main_page_3(self):

        """A list of Template instances used to render the final content,
        in the order they were rendered. For each template in the list,
        use template.name to get the template’s file name, if the template was loaded from a file. """

        response = self.client.get(reverse('calculators:main_bmi'))
        self.assertEqual(response.templates[0].name, "calculators/bmi.html")


    # SimpleTestCase.assertContains(response, text, count=None, status_code=200, msg_prefix='', html=False)
    # TODO a lot of tests
