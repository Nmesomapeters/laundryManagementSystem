from django.core.management.base import BaseCommand
from laundry.models import Service, ServiceCart

class Command(BaseCommand):
    help = 'Delete all services and related data'

    def handle(self, *args, **kwargs):
        ServiceCart.objects.all().delete()
        Service.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all services and related data'))