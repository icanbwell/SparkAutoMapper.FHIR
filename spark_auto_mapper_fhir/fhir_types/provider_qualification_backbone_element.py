from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.valuesets.provider_qualification import ProviderQualificationCode


class FhirProviderQualificationBackboneElement(FhirResourceBase):
    def __init__(
        self,
        code: FhirCodeableConcept[ProviderQualificationCode],
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        period: Optional[FhirPeriod] = None,
        issuer: Optional[FhirReference[FhirOrganization]] = None
    ):
        """
        ProviderQualificationBackboneElement Resource in FHIR
        http://hl7.org/fhir/practitioner-definitions.html#Practitioner.qualification
        Certification, licenses, or training pertaining to the provision of care

        :param code: Coded representation of the qualification. http://hl7.org/fhir/v2/0360/2.7/index.html
        :param identifier: An identifier for this qualification for the practitioner
        :param period: Period during which the qualification is valid
        :param issuer: Organization that regulates and issues the qualification
        """
        super().__init__(
            code=code, identifier=identifier, period=period, issuer=issuer
        )
