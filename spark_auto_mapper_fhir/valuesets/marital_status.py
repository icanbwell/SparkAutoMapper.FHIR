from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class MaritalStatusCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-marital-status.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'MaritalStatusCode']) -> None:
            self.f: Callable[..., 'MaritalStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['MaritalStatusCode']
        ) -> 'MaritalStatusCode':
            return self.f(owner)

    @classproperty
    def Annulled(cls) -> 'MaritalStatusCode':
        """
        Marriage contract has been declared null and to not have existed
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("A")

    @classproperty
    def Divorced(cls) -> 'MaritalStatusCode':
        """
        Marriage contract has been declared dissolved and inactive
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("D")

    @classproperty
    def Interlocutory(cls) -> 'MaritalStatusCode':
        """
        Subject to an Interlocutory Decree.
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("I")

    @classproperty
    def Legally_Separated(cls) -> 'MaritalStatusCode':
        """
        Legally Separated
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("L")

    @classproperty
    def Married(self) -> 'MaritalStatusCode':
        """
        A current marriage contract is active
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("M")

    @classproperty
    def Polygamous(self) -> 'MaritalStatusCode':
        """
        More than 1 current spouse
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("P")

    @classproperty
    def Never_Married(cls) -> 'MaritalStatusCode':
        """
        No marriage contract has ever been entered
        :return:
        :rtype:
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("S")

    @classproperty
    def Domestic_partner(self) -> 'MaritalStatusCode':
        """
        Person declares that a domestic partner relationship exists.
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("T")

    @classproperty
    def unmarried(self) -> 'MaritalStatusCode':
        """
        Currently not in a marriage contract.
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("U")

    @classproperty
    def Widowed(self) -> 'MaritalStatusCode':
        """
        The spouse has died
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("W")

    @classproperty
    def unknown(self) -> 'MaritalStatusCode':
        """
        Description:A proper value is applicable, but not known. Usage Notes: This means the actual value is not known.
        If the only thing that is unknown is how to properly express the value in the necessary
        constraints (value set, datatype, etc.), then the OTH or UNC flavor should be used
        """
        # noinspection PyCallingNonCallable
        return MaritalStatusCode("UNK")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v3-MaritalStatus"
