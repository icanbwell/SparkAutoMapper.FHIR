from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimCareTeamRoleCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-careteamrole.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ClaimCareTeamRoleCode']) -> None:
            self.f: Callable[..., 'ClaimCareTeamRoleCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ClaimCareTeamRoleCode']
        ) -> 'ClaimCareTeamRoleCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'ClaimCareTeamRoleCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ClaimCareTeamRoleCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/claimcareteamrole"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.586"
