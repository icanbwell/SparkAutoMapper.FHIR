from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ProgramCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-program.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ProgramCode']) -> None:
            self.f: Callable[..., 'ProgramCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ProgramCode']
        ) -> 'ProgramCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'ProgramCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ProgramCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/program
        """
        return "http://terminology.hl7.org/CodeSystem/program"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.1383
        """
        return "2.16.840.1.113883.4.642.3.1383"
