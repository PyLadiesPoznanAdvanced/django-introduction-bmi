from django.db import models

sex = (
    ("men", "mężczyzna"),
    ("women", "kobieta")
    )


class Person (models.Model):
    """Person model with sex, weight and height for bmi counting."""

    sex = models.CharField(max_length=20, choices=sex)
    weight = models.FloatField()
    height = models.FloatField()

    def get_bmi(self):

        # count bmi
        bmi_result = round(self.weight / self.height ** 2, 2)

        # check weight category
        if sex == "women":
            if bmi_result <= 17.5:
                weight_type = "niedowaga"
            elif 17.5 < bmi_result <= 22.5:
                weight_type = "normalna waga"
            elif 22.5 < bmi_result <= 27.5:
                weight_type = "nadwaga"
            else:
                weight_type = "otyłość"
        else:
            if bmi_result <= 20:
                weight_type = "niedowaga"
            elif 20 < bmi_result <= 25:
                weight_type = "normalna waga"
            elif 25 < bmi_result <= 30:
                weight_type = "nadwaga"
            else:
                weight_type = "otyłość"

        return bmi_result, weight_type
