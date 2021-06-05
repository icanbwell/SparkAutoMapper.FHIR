from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ClaimTypeCode"]) -> None:
            self.f: Callable[..., "ClaimTypeCode"] = f

        def __get__(self, obj: Any, owner: Type["ClaimTypeCode"]) -> "ClaimTypeCode":
            return self.f(owner)

    @classproperty
    def Institutional(cls) -> "ClaimTypeCode":
        """
        Hospital, clinic and typically inpatient claims.
        """
        # noinspection PyCallingNonCallable
        return ClaimTypeCode("institutional")

    def Oral(cls) -> "ClaimTypeCode":
        """
        Dental, Denture and Hygiene claims.
        """
        # noinspection PyCallingNonCallable
        return ClaimTypeCode("oral")

    def Pharmacy(cls) -> "ClaimTypeCode":
        """
        Pharmacy claims for goods and services.
        """
        # noinspection PyCallingNonCallable
        return ClaimTypeCode("pharmacy")

    def Professional(cls) -> "ClaimTypeCode":
        """
        Typically, outpatient claims from Physician, Psychological, Chiropractor, Physiotherapy, Speech Pathology, rehabilitative, consulting
        """
        # noinspection PyCallingNonCallable
        return ClaimTypeCode("professional")

    def Vision(cls) -> "ClaimTypeCode":
        """
        Vision claims for professional services and products such as glasses and contact lenses.
        """
        # noinspection PyCallingNonCallable
        return ClaimTypeCode("vision")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "https://hl7.org/FHIR/codesystem-claim-type.html"
