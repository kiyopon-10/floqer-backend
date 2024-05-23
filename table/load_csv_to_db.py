import os
import django
import pandas as pd

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'table.settings')  # Replace 'myproject' with your project's name
django.setup()

from myapp.models import JobData  # Ensure 'myapp' is your app's name

# Load the CSV file
csv_file_path = os.path.join(os.path.dirname(__file__), 'salaries.csv')
df = pd.read_csv(csv_file_path)

# Iterate through the DataFrame and create JobData instances
for index, row in df.iterrows():
    JobData.objects.create(
        work_year=row['work_year'],
        experience_level=row['experience_level'],
        employment_type=row['employment_type'],
        job_title=row['job_title'],
        salary=row['salary'],
        salary_currency=row['salary_currency'],
        salary_in_usd=row['salary_in_usd'],
        employee_residence=row['employee_residence'],
        remote_ratio=row['remote_ratio'],
        company_location=row['company_location'],
        company_size=row['company_size'],
    )
