from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirIdentifierUseCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-identifier-use.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirIdentifierUseCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirIdentifierUseCode']) -> None:
            self.f: Callable[..., 'FhirIdentifierUseCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirIdentifierUseCode']
        ) -> 'FhirIdentifierUseCode':
            return self.f(owner)

    @classproperty
    def Usual(cls) -> 'FhirIdentifierUseCode':
        """
        The identifier recommended for display and use in real-world interactions.
        """
        # noinspection PyCallingNonCallable
        return FhirIdentifierUseCode("usual")

    @classproperty
    def Official(cls) -> 'FhirIdentifierUseCode':
        """
        The identifier considered to be most trusted for the identification of this item.
        Sometimes also known as "primary" and "main". The determination of "official" is subjective
        and implementation guides often provide additional guidelines for use.
        """
        # noinspection PyCallingNonCallable
        return FhirIdentifierUseCode("official")

    @classproperty
    def Temp(cls) -> 'FhirIdentifierUseCode':
        """
        A temporary identifier.
        """
        # noinspection PyCallingNonCallable
        return FhirIdentifierUseCode("temp")

    @classproperty
    def Secondary(cls) -> 'FhirIdentifierUseCode':
        """
        An identifier that was assigned in secondary use - it serves to identify the object in a relative context,
        but cannot be consistently assigned to the same object again in a different context.
        """
        # noinspection PyCallingNonCallable
        return FhirIdentifierUseCode("secondary")

    @classproperty
    def Old(cls) -> 'FhirIdentifierUseCode':
        """
        The identifier id no longer considered valid, but may be relevant for search purposes.
        E.g. Changes to identifier schemes, account merges, etc.
        """
        # noinspection PyCallingNonCallable
        return FhirIdentifierUseCode("old")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/identifier-use"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.4.58"
