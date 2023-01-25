def is_floatstring(value):
    if value[0] == '0':
        return False
    try:
        float(value)
        return True

    except ValueError:
        try:
            str(value)
            return False
        except Exception:
            return
