from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.provider_qualification import ProviderQualificationCode


class PractitionerQualificationBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        code: CodeableConcept[ProviderQualificationCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        period: Optional[Period] = None,
        issuer: Optional[Reference[Organization]] = None
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
            id_=id_,
            extension=extension,
            identifier=identifier,
            code=code,
            period=period,
            issuer=issuer
        )
