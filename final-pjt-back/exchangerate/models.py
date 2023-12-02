from django.db import models

class ExchangeRate(models.Model):
    search_date = models.DateField()
    cur_unit = models.CharField(max_length=150)
    cur_nm = models.TextField()
    ttb = models.TextField()
    tts = models.TextField()
    deal_bas_r = models.TextField()