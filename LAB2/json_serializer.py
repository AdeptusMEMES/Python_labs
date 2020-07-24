def to_json(obj):
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        if obj is True:
            return "true"
        else:
            return "false"
    elif isinstance(obj, (int, float)):
        return str(obj)
    elif isinstance(obj, str):
        return '"' + obj + '"'
    elif isinstance(obj, (tuple, set, list)):
        res = ", ".join(to_json(element) for element in obj)
        return "[" + res + "]"
    elif isinstance(obj, dict):
        keys_and_values = []
        for key, value in obj.items():
            if isinstance(key, (int, float, bool)) or key is None:
                keys_and_values.append('"' + to_json(key) + '":' + to_json(value))
            else:
                keys_and_values.append(to_json(key) + ": " + to_json(value))
        res = ", ".join(key_and_value for key_and_value in keys_and_values)
        return "{" + res + "}"
    elif isinstance(obj, object):
        class_dict = obj.__dict__
        return to_json(class_dict)
    else:
        raise TypeError("Impossible to serialize object of type " + str(type(obj)) + " to JSON" )