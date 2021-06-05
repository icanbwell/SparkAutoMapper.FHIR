from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimSubTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-subtype.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ClaimSubTypeCode"]) -> None:
            self.f: Callable[..., "ClaimSubTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ClaimSubTypeCode"]
        ) -> "ClaimSubTypeCode":
            return self.f(owner)

    @classproperty
    def OrthodonticClaim(cls) -> "ClaimSubTypeCode":
        """
        A claim for Orthodontic Services.
        """
        # noinspection PyCallingNonCallable
        return ClaimSubTypeCode("ortho")

    def EmergencyClaim(cls) -> "ClaimSubTypeCode":
        """
        A claim for emergency services.
        """
        # noinspection PyCallingNonCallable
        return ClaimSubTypeCode("emergency")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-claimsubtype"
