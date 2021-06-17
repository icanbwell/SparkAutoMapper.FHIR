from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.visionprescription import VisionPrescriptionSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.encounter import Encounter
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.valuesets.financial_resource_status import (
    FinancialResourceStatusCode,
)
from spark_auto_mapper_fhir.backbone_elements.vision_prescription_lens_specification_backbone_element import (
    VisionPrescriptionLensSpecificationBackboneElement,
)


class VisionPrescription(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        status: FinancialResourceStatusCode,
        created: FhirDateTime,
        patient: Reference[Patient],
        dateWritten: FhirDateTime,
        prescriber: Reference[Union[Practitioner, PractitionerRole]],
        lensSpecification: FhirList[VisionPrescriptionLensSpecificationBackboneElement],
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        encounter: Optional[Reference[Encounter]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        VisionPrescription Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#VisionPrescription


        :param id_: id of resource
        :param identifier: Business Identifier for vision prescription
        :param status: active | cancelled | draft | entered-in-error
        :param created: Response creation date
        :param patient: Who prescription is for
        :param encounter: Created during encounter / admission / stay
        :param dateWritten: When prescription was authorized
        :param prescriber: Who authorized the vision prescription
        :param lensSpecification: Vision lens authorization
        """
        super().__init__(
            resourceType="VisionPrescription",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            created=created,
            patient=patient,
            encounter=encounter,
            dateWritten=dateWritten,
            prescriber=prescriber,
            lensSpecification=lensSpecification,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return VisionPrescriptionSchema.get_schema(include_extension=include_extension)
