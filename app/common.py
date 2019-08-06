def trueReturn(data, msg):
    return {
        "status": True,
        "data": data,
        "msg": msg
    }


def falseReturn(data=None, msg):
    return {
        "status": False,
        "data": data,
        "msg": msg
    }

