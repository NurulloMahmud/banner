from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'statuses'
        verbose_name_plural = 'statuses'


class Company(models.Model):
    title = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    address = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'companies'
        verbose_name_plural = 'companies'
    
    def __str__(self) -> str:
        return self.title


class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    class Meta:
        db_table = 'agents'
    
    def __str__(self) -> str:
        return self.user.get_username()


class Location(models.Model):
    name = models.CharField(max_length=55)
    description = models.TextField()
    lattitude = models.FloatField()
    longtitude = models.FloatField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'locations'


class LocationImage(models.Model):
    image = models.TextField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.location.name + "'s picture"
    
    class Meta:
        db_table = 'location_images'


class Advertisement(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)