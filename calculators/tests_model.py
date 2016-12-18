

from django.test import TestCase
from .models import Person


class PersonTests(TestCase):

    def setUp(self):
        """Metoda setUP jest wykonywana przed każdym testem.
        Tworzy dwa obiekty Person wyłącznie w celach testowych"""
        Person.objects.create(sex="women", weight=55, height=1.60)
        Person.objects.create(sex="men", weight=70, height=1.70)

    def test_bmi_1(self):
        """Test obliczeń bmi Person, sex='women'"""
        women = Person.objects.get(sex="women")
        bmi, weight_cat = women.get_bmi()
        self.assertEqual(bmi, 21.48, msg="Błąd w test_bmi_1")

    def test_bmi_2(self):
        """Test obliczeń bmi Person, sex='men'"""
        men = Person.objects.get(sex="men")
        bmi, weight_cat = men.get_bmi()
        self.assertEqual(bmi, 24.22)

    # TODO a lot of tests

