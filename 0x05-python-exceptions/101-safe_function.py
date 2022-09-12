#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        div = fct(*args)
        return div
    except Exception as e:
        import sys
        print("Exception: {}".format(e), file=sys.stderr)
        return None
