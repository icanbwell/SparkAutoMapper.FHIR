from typing import Optional, Union

from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson


class GuarantorBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        party: Reference[Union[Patient, RelatedPerson, Organization]],
        onHold: Optional[FhirBoolean] = None,
        period: Optional[Period] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ):
        """
        GuarantorBackboneElement Resource in FHIR
        https://hl7.org/FHIR/account-definitions.html#guarantor

        :param party: Responsible entity
        :param onHold: Credit or other hold applied
        :param period: Guarantee account during
        """
        super().__init__(
            id_=id_, party=party, onHold=onHold, period=period, extension=extension
        )
