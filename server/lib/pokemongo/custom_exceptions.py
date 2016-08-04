class GeneralPogoException(Exception):
    """Throw an exception that moves up to the start, and reboots"""

class OutOfUsableBallsException(GeneralPogoException):
    """Throw an out of usable balls exception"""