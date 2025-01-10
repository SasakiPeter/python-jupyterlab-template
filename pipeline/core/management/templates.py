from pipeline.core.management.base import BaseCommand


class TemplateCommand(BaseCommand):
    help = "This is a template command"

    def add_arguments(self, parser):
        parser.add_argument("module_name", type=str, help="name of module to be created")
