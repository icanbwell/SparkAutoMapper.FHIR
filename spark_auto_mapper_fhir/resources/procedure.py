from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.procedure import ProcedureSchema

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.group import Group
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.valuesets.event_status import EventStatusCode
from spark_auto_mapper_fhir.valuesets.snomed import SnoMedCode


class Procedure(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: EventStatusCode,
        statusReason: Optional[CodeableConcept[SnoMedCode]] = None,
        subject: Reference[Union[Patient, Group]]
    ) -> None:
        """
        Procedure Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Procedure
        An action that is being or was performed on a patient


        :param id_: id of resource
        :param status: preparation | in-progress | not-done | on-hold | stopped | completed | entered-in-error | unknown
        :param statusReason: Reason for current status
        """
        super().__init__(
            resourceType="Procedure",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            statusReason=statusReason
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ProcedureSchema.get_schema(include_extension=include_extension)
