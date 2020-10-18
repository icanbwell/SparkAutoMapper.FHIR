# noinspection PyPep8Naming,SpellCheckingInspection
class genericclassproperty(object):
    """
    Attribute to have a method treated as class property
    """

    def __init__(self, f) -> None:
        self.f = f

    def __get__(self, obj, owner):
        return self.f(owner)

# _T = TypeVar("_T")
#
#
# # noinspection PyPep8Naming,SpellCheckingInspection
# class genericclassproperty(Generic[_T]):
#     """
#     Attribute to have a method treated as class property
#     """
#
#     def __init__(self, f: Callable[..., _T]) -> None:
#         self.f: Callable[..., _T] = f
#
#     def __get__(self, obj, owner: Type[_T]) -> _T:
#         return self.f(owner)
