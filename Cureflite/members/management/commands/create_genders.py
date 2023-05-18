from django.core.management.base import BaseCommand
from members.models import Gender


class Command(BaseCommand):
    help = 'Create initial genders if they do not exist'

    def handle(self, *args, **options):
        male_gender = Gender.objects.filter(code='M').first()
        female_gender = Gender.objects.filter(code='F').first()

        if not male_gender:
            # Create the male gender object if it doesn't exist
            male_gender = Gender.objects.create(code='M', name_en='Male', name_zh='男', is_male=True)
            self.stdout.write(self.style.SUCCESS('Created male gender'))

        if not female_gender:
            # Create the female gender object if it doesn't exist
            female_gender = Gender.objects.create(code='F', name_en='Female', name_zh='女', is_male=False)
            self.stdout.write(self.style.SUCCESS('Created female gender'))
