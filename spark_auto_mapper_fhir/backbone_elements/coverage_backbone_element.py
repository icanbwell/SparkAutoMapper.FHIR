from typing import Optional

from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

from spark_auto_mapper_fhir.resources.coverage import Coverage


class CoverageBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        coverage: Reference[Coverage],
        priority: Optional[FhirPositiveInt] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ):
        """
        CoverageBackboneElement Resource in FHIR
        https://hl7.org/FHIR/account-definitions.html#coverage

        :param coverage: The party(s) that are responsible for covering the payment of this account, and what order should they be applied to the account
        :param priority: The priority of the coverage in the context of this account
        """
        super().__init__(
            id_=id_, coverage=coverage, priority=priority, extension=extension
        )
