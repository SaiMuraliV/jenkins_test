def div(x, y):
    try:
        return divmod(x, y)
    except ZeroDivisionError as e:
        raise Exception(f"{e}")
    except TypeError as e:
        raise Exception(f"{e}")

