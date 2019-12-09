from django.db import models

# Create your models here.

class SearchList(models.Model):
    no = models.AutoField(db_column='NO', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    price = models.CharField(db_column='PRICE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(db_column='PLACE', max_length=45, blank=True, null=True)  # Field name made lowercase.
    del_price = models.CharField(db_column='DEL_PRICE', max_length=15, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    site = models.CharField(db_column='SITE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    img = models.CharField(db_column='IMG', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'search_list'
