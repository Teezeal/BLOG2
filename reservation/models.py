from django.db import models

# Create your models here.
DESTINATION =[
    ('Dubai', 'Dubai'),
    ('Paris', 'Paris'),
    ('Nigeria', 'Nigeria')
]

CHECK_IN =[
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Night', 'Night')
]

ROOMS =[
    ('Barcelona', 'Barcelona'),
    ('Bayern', 'Bayern'),
    ('Chelsea', 'Chelsea'),
    ('Man U', 'Man U'),
    ('Man City', 'Man City'),
    ('Wolves', 'Wolves'),
    ('Psg', 'Psg'),
    ('Psv', 'Psv'),
    ('Ajax', 'Ajax')
]

ADULTS=[
    ('21-30', '21-30'),
    ('31-40', '31-40'),
    ('41-50', '41-50'),
    ('51-60', '51-60'),
    ('61-70', '61-70'),
    ('71-80', '71-80')
    
]

CHILDREN=[
    ('0-5', '0-5'),
    ('6-11', '6-11'),
    ('12-20', '12-20')
    
]


class Reservation(models.Model):
    
    destination= models.CharField(max_length=20, choices=DESTINATION)
    check_in=models.CharField(max_length=20, choices=CHECK_IN)
    check_out=models.CharField(max_length=20, choices=CHECK_IN)
    rooms=models.CharField(max_length=20, choices=ROOMS)
    adults=models.CharField(max_length=20, choices=ADULTS)
    children=models.CharField(max_length=20, choices=CHILDREN)



    def __str__(self):
        return f'{self.user.username} Profile'