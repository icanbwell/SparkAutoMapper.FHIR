from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirMaritalStatusCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-marital-status.html
    """
    @classmethod
    def map(cls, value: AutoMapperNativeSimpleType) -> 'FhirMaritalStatusCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirMaritalStatusCode']) -> None:
            self.f: Callable[..., 'FhirMaritalStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirMaritalStatusCode']
        ) -> 'FhirMaritalStatusCode':
            return self.f(owner)

    @classproperty
    def Annulled(cls) -> 'FhirMaritalStatusCode':
        """
        Marriage contract has been declared null and to not have existed
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("A")

    @classproperty
    def Divorced(cls) -> 'FhirMaritalStatusCode':
        """
        Marriage contract has been declared dissolved and inactive
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("D")

    @classproperty
    def Interlocutory(cls) -> 'FhirMaritalStatusCode':
        """
        Subject to an Interlocutory Decree.
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("I")

    @classproperty
    def Legally_Separated(cls) -> 'FhirMaritalStatusCode':
        """
        Legally Separated
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("L")

    @classproperty
    def Married(self) -> 'FhirMaritalStatusCode':
        """
        A current marriage contract is active
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("M")

    @classproperty
    def Polygamous(self) -> 'FhirMaritalStatusCode':
        """
        More than 1 current spouse
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("P")

    @classproperty
    def Never_Married(cls) -> 'FhirMaritalStatusCode':
        """
        No marriage contract has ever been entered
        :return:
        :rtype:
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("S")

    @classproperty
    def Domestic_partner(self) -> 'FhirMaritalStatusCode':
        """
        Person declares that a domestic partner relationship exists.
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("T")

    @classproperty
    def unmarried(self) -> 'FhirMaritalStatusCode':
        """
        Currently not in a marriage contract.
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("U")

    @classproperty
    def Widowed(self) -> 'FhirMaritalStatusCode':
        """
        The spouse has died
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("W")

    @classproperty
    def unknown(self) -> 'FhirMaritalStatusCode':
        """
        Description:A proper value is applicable, but not known. Usage Notes: This means the actual value is not known.
        If the only thing that is unknown is how to properly express the value in the necessary
        constraints (value set, datatype, etc.), then the OTH or UNC flavor should be used
        """
        # noinspection PyCallingNonCallable
        return FhirMaritalStatusCode("UNK")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
