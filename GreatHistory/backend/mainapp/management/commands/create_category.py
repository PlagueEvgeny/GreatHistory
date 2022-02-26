from django.core.management.base import BaseCommand

from mainapp.models import Category


class Command(BaseCommand):
    help = 'Create Category'

    def handle(self, *args, **options):
        i = 0
        while i <= 4:
            Category.objects.get_or_create(
                name=f'Категория #{i + 1}',
            )
            i += 1
        print('Категория успешно создана!')
