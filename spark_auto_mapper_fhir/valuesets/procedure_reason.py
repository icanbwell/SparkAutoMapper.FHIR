from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ProcedureReasonCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-procedure-reason.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ProcedureReasonCode"]) -> None:
            self.f: Callable[..., "ProcedureReasonCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ProcedureReasonCode"]
        ) -> "ProcedureReasonCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ProcedureReasonCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ProcedureReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/procedure-reason
        """
        return "http://hl7.org/fhir/ValueSet/procedure-reason"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.432
        """
        return "2.16.840.1.113883.4.642.3.432"
