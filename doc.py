from sys import builtin_module_names

def doc_from_str(objstr):
    ns = objstr.split('.')
    try:
        obj = __builtins__[ns[0]]
    except KeyError:
        if ns[0] in builtin_module_names:
            obj = __import__(ns[0])
        else:
            return None
    for scope in ns[1:]:
        try:
            obj = getattr(obj, scope)
        except AttributeError:
            return None
    return getattr(obj, '__doc__')
