from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        # 1. Create the necessary reference data
        self.create_colleges()
        self.create_programs()
        # 2. Now create the main data
        self.create_organization(10)
        self.create_students(50)
        self.create_membership(10)

    def create_colleges(self):
        colleges = [
            "College of Engineering",
            "College of Arts and Sciences",
            "College of Business Administration",
            "College of Education",
            "College of Information Technology",
            "College of Nursing",
            "College of Law",
        ]
        for name in colleges:
            College.objects.get_or_create(college_name=name)
        self.stdout.write(self.style.SUCCESS('Colleges created successfully.'))

    def create_programs(self):
        program_data = {
            "College of Engineering": ["BS Civil Engineering", "BS Mechanical Engineering", "BS Electrical Engineering", "BS Computer Engineering"],
            "College of Arts and Sciences": ["BS Biology", "BA English", "BA Psychology", "BS Mathematics"],
            "College of Business Administration": ["BS Accountancy", "BS Business Administration", "BS Marketing"],
            "College of Education": ["BS Elementary Education", "BS Secondary Education"],
            "College of Information Technology": ["BS Information Technology", "BS Computer Science", "BS Information Systems"],
            "College of Nursing": ["BS Nursing"],
            "College of Law": ["Juris Doctor"],
        }
        for college_name, programs in program_data.items():
            college = College.objects.get(college_name=college_name)
            for prog_name in programs:
                Program.objects.get_or_create(prog_name=prog_name, college=college)
        self.stdout.write(self.style.SUCCESS('Programs created successfully.'))

    def create_organization(self, count):
        fake = Faker()
        for _ in range(count):
            words = [fake.word() for _ in range(2)]
            organization_name = ''.join(words)
            Organization.objects.create(
                name=organization_name.title(),
                college=College.objects.order_by('?').first(),
                description=fake.sentence()
            )
        self.stdout.write(self.style.SUCCESS('Organizations created successfully.'))

    def create_students(self, count):
        fake = Faker('en_PH')
        for _ in range(count):
            Student.objects.create(
                student_id=f'{fake.random_int(2020,2025)}-{fake.random_int(1,8)}-{fake.random_number(digits=4)}',
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=Program.objects.order_by('?').first()   # now this will always return a Program
            )
        self.stdout.write(self.style.SUCCESS('Students created successfully.'))

    def create_membership(self, count):
        fake = Faker()
        for _ in range(count):
            OrgMember.objects.create(
                student=Student.objects.order_by('?').first(),
                organization=Organization.objects.order_by('?').first(),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )
        self.stdout.write(self.style.SUCCESS('Memberships created successfully.'))