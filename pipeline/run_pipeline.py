import json

from pipeline.conf import settings
from pipeline.submodules.submodule import do_something
from pipeline.utils.logger import setup_logger


def main():
    logger = setup_logger(__name__)
    try:
        logger.info("Start pipeline.")
        logger.info(f"settings: {json.dumps(settings.to_dict(), indent=4)}")
        do_something()
        logger.info("End pipeline.")

    except Exception as e:
        logger.error(e)
        raise e


if __name__ == "__main__":
    main()
