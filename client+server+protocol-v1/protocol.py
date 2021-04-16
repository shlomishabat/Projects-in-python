#   Ex. 2.7 template - protocol


LENGTH_FIELD_SIZE = 4
PORT = 8820


def check_cmd(data):
    if len(data) < 10000:
        return True
    else:
        return False


def create_msg(data):
    length = str(len(data))
    zfill_length = length.zfill(4)
    return zfill_length+data


def get_msg(lenmas):
    if lenmas.isdigit():
        return True
    else:
        return False









