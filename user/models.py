from django.contrib.auth.models import User
from django.db import models


class RegistrationCar(models.Model):
    WAITING_VISIT = 'Waiting for a visit'
    VISITED = 'Visited'
    ARCHIVED = 'Archived'
    status_types = [
        (WAITING_VISIT, 'Waiting for a visit'),
        (VISITED, 'Visited'),
        (ARCHIVED, 'Archived')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model_of_car = models.CharField(max_length=256)
    type_of_problem = models.TextField()
    visit_date = models.DateField()
    visit_time = models.TimeField()
    status = models.CharField(max_length=100, choices=status_types, default=WAITING_VISIT)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.model_of_car
