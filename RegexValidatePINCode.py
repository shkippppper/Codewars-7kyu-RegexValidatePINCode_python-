


def validate_pin(pin):

    if pin.isnumeric():
        if len(pin)==4 or len(pin) == 6:
            return True
        else:
            return False
    else:
        return False


