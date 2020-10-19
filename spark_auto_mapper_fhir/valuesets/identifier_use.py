from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class IdentifierUseCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-identifier-use.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'IdentifierUseCode']) -> None:
            self.f: Callable[..., 'IdentifierUseCode'] = f

        def __get__(
            self, obj: Any, owner: Type['IdentifierUseCode']
        ) -> 'IdentifierUseCode':
            return self.f(owner)

    @classproperty
    def Usual(cls) -> 'IdentifierUseCode':
        """
        The identifier recommended for display and use in real-world interactions.
        """
        # noinspection PyCallingNonCallable
        return IdentifierUseCode("usual")

    @classproperty
    def Official(cls) -> 'IdentifierUseCode':
        """
        The identifier considered to be most trusted for the identification of this item.
        Sometimes also known as "primary" and "main". The determination of "official" is subjective
        and implementation guides often provide additional guidelines for use.
        """
        # noinspection PyCallingNonCallable
        return IdentifierUseCode("official")

    @classproperty
    def Temp(cls) -> 'IdentifierUseCode':
        """
        A temporary identifier.
        """
        # noinspection PyCallingNonCallable
        return IdentifierUseCode("temp")

    @classproperty
    def Secondary(cls) -> 'IdentifierUseCode':
        """
        An identifier that was assigned in secondary use - it serves to identify the object in a relative context,
        but cannot be consistently assigned to the same object again in a different context.
        """
        # noinspection PyCallingNonCallable
        return IdentifierUseCode("secondary")

    @classproperty
    def Old(cls) -> 'IdentifierUseCode':
        """
        The identifier id no longer considered valid, but may be relevant for search purposes.
        E.g. Changes to identifier schemes, account merges, etc.
        """
        # noinspection PyCallingNonCallable
        return IdentifierUseCode("old")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/identifier-use"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.4.58"
