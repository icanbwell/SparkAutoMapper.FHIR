# noinspection PyPep8Naming,SpellCheckingInspection
class classproperty(object):
    """
    Attribute to have a method treated as class property
    """
    def __init__(self, f):
        self.f = f

    def __get__(self, obj, owner):
        return self.f(owner)
