from django.db import models

# Create your models here.
from django.db import models


class LGA(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    lga_id = models.IntegerField()
    lga_name = models.CharField(max_length=50)
    state_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "lga"


class Ward(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    ward_id = models.IntegerField()
    ward_name = models.CharField(max_length=50)
    lga_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "ward"


class Party(models.Model):
    id = models.IntegerField(primary_key=True)
    partyid = models.CharField(max_length=11)
    partyname = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = "party"


class PollingUnit(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField(null=True)
    polling_unit_number = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    polling_unit_name = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    polling_unit_description = models.TextField(
        null=True,
        blank=True
    )
    lat = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    long = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    class Meta:
        managed = False
        db_table = "polling_unit"


class AnnouncedPUResult(models.Model):
    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.CharField(max_length=50)
    party_abbreviation = models.CharField(max_length=4)
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=50)
    date_entered = models.DateTimeField()
    user_ip_address = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = "announced_pu_results"
