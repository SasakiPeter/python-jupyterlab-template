from pipeline.core.management.base import BaseCommand
from pipeline.run_pipeline import main as run_pipeline


class Command(BaseCommand):
    help = "Run."

    def add_arguments(self, parser):
        parser.add_argument("-n", "--name", help="sample")

    def execute(self, *args, **options):
        run_pipeline()
