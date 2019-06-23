import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Djanho commandf to pause executuoin until datbase is availane"""

    def handle(self, *args, **options):
        self.stdout.write('Waiting for datbase...')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database uanvailabel, waiint 1 second...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available!'))
