# Generated by Django 5.0.6 on 2024-05-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_year', models.IntegerField()),
                ('experience_level', models.CharField(max_length=2)),
                ('employment_type', models.CharField(max_length=2)),
                ('job_title', models.CharField(max_length=255)),
                ('salary', models.IntegerField()),
                ('salary_currency', models.CharField(max_length=3)),
                ('salary_in_usd', models.IntegerField()),
                ('employee_residence', models.CharField(max_length=2)),
                ('remote_ratio', models.IntegerField()),
                ('company_location', models.CharField(max_length=2)),
                ('company_size', models.CharField(max_length=1)),
            ],
        ),
    ]
