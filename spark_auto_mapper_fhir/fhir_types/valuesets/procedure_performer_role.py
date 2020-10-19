from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirProcedurePerformerRoleCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-performer-role.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirProcedurePerformerRoleCode']
        ) -> None:
            self.f: Callable[..., 'FhirProcedurePerformerRoleCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirProcedurePerformerRoleCode']
        ) -> 'FhirProcedurePerformerRoleCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirProcedurePerformerRoleCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirProcedurePerformerRoleCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://snomed.info/sct"
