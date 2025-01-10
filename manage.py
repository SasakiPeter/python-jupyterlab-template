import os
import sys


def main():
    template_commands = {}

    command = sys.argv[1]
    if command not in template_commands:
        file_name = sys.argv.pop()
        settings_module = f"config.settings.{file_name}"
        os.environ.setdefault("SETTINGS_MODULE", settings_module)

    try:
        from pipeline.core.management import execute_from_command_line
    except ImportError:
        raise ImportError("Couldn't import pipeline. Are you sure it's installed ?")
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
