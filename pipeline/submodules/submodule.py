from pipeline.utils.logger import setup_logger


def do_something():
    logger = setup_logger(__name__)
    logger.info("do something")


if __name__ == "__main__":
    do_something()
