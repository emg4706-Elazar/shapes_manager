import logging


def get_logger():
    l = logging.getLogger('shapes')
    l.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("shape_manager.log", encoding="utf-8")
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    file_handler.setFormatter(formatter)
    l.addHandler(file_handler)

    return l

logger = get_logger()