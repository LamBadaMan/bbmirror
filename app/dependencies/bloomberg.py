from blp import blp


def bbconnect():
    query = blp.BlpQuery().start()
    try:
        yield query
    finally:
        query.stop()
