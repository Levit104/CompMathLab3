def valid_value(value, min_value, max_value, is_strict):
    if value == 'exit':
        raise KeyboardInterrupt
    try:
        return (min_value < float(value) < max_value) if is_strict else (min_value <= float(value) <= max_value)
    except ValueError:
        return False
