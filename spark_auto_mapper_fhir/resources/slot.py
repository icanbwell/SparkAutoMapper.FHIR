from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.slot import SlotSchema

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.schedule import Schedule
from spark_auto_mapper_fhir.valuesets.service_type import ServiceTypeCode
from spark_auto_mapper_fhir.valuesets.slot_status import SlotStatusCode


class Slot(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        schedule: Reference[Schedule],
        status: SlotStatusCode,
        start: FhirInstant,
        end: FhirInstant,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        serviceType: Optional[FhirList[CodeableConcept[ServiceTypeCode]]
                              ] = None,
    ):
        """
        Slot Resource in FHIR
        http://hl7.org/fhir/slot.html
        A slot of time on a schedule that may be available for booking appointments


        :param id_: id of resource
        :param schedule: The schedule resource that this slot defines an interval of status information
        :param status: busy | free | busy-unavailable | busy-tentative | entered-in-error
        :param start: Date/Time that the slot is to begin
        :param end: Date/Time that the slot is to conclude
        :param identifier: An identifier for the slot
        :param serviceType: The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource
        """
        super().__init__(
            resourceType="Schedule",
            id_=id_,
            schedule=schedule,
            status=status,
            start=start,
            end=end,
            meta=meta,
            identifier=identifier,
            extension=extension,
            serviceType=serviceType,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return SlotSchema.get_schema(include_extension=include_extension)
