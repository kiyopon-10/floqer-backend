from django.db import models

class JobData(models.Model):
    work_year = models.IntegerField()
    experience_level = models.CharField(max_length=2)
    employment_type = models.CharField(max_length=2)
    job_title = models.CharField(max_length=255)
    salary = models.IntegerField()
    salary_currency = models.CharField(max_length=3)
    salary_in_usd = models.IntegerField()
    employee_residence = models.CharField(max_length=2)
    remote_ratio = models.IntegerField()
    company_location = models.CharField(max_length=2)
    company_size = models.CharField(max_length=1)
