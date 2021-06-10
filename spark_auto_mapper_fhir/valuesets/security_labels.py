from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class SecurityLabelsCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-security-labels.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "SecurityLabelsCode"]) -> None:
            self.f: Callable[..., "SecurityLabelsCode"] = f

        def __get__(
            self, obj: Any, owner: Type["SecurityLabelsCode"]
        ) -> "SecurityLabelsCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "SecurityLabelsCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return SecurityLabelsCode("A")

    @genericclassproperty
    def owner_codeset(cls) -> FhirUri:
        return "https://www.icanbwell.com/owner"

    @genericclassproperty
    def access_codeset(cls) -> FhirUri:
        return "https://www.icanbwell.com/access"

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/v3-Confidentiality
        """
        return "http://terminology.hl7.org/CodeSystem/v3-Confidentiality"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.47
        """
        return "2.16.840.1.113883.4.642.3.47"
