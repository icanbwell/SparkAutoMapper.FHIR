from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.slot import SlotSchema

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.schedule import Schedule
from spark_auto_mapper_fhir.valuesets.practice_setting_code import PracticeSettingCode
from spark_auto_mapper_fhir.valuesets.service_category import ServiceCategoryCode
from spark_auto_mapper_fhir.valuesets.service_type import ServiceTypeCode
from spark_auto_mapper_fhir.valuesets.slot_status import SlotStatusCode
from spark_auto_mapper_fhir.valuesets.v2_appointment_reason import (
    V2AppointmentReasonCode,
)


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
        serviceCategory: Optional[
            FhirList[CodeableConcept[ServiceCategoryCode]]
        ] = None,
        serviceType: Optional[FhirList[CodeableConcept[ServiceTypeCode]]] = None,
        specialty: Optional[FhirList[CodeableConcept[PracticeSettingCode]]] = None,
        appointmentType: Optional[CodeableConcept[V2AppointmentReasonCode]] = None,
        overbooked: Optional[FhirBoolean] = None,
        comment: Optional[FhirString] = None,
    ):
        """
        Slot Resource in FHIR
        http://hl7.org/fhir/slot.html
        A slot of time on a schedule that may be available for booking appointments


        :param id_: id of resource
        :param identifier: An identifier for the slot
        :param serviceCategory: A broad categorization of the service that is to be performed during this appointment
        :param serviceType: The type of appointments that can be booked into this slot (ideally this would be an identifiable service - which is at a location, rather than the location itself). If provided then this overrides the value provided on the availability resource
        :param specialty: The specialty of a practitioner that would be required to perform the service requested in this appointment
        :param appointmentType: The style of appointment or patient that may be booked in the slot (not service type)
        :param schedule: The schedule resource that this slot defines an interval of status information
        :param status: busy | free | busy-unavailable | busy-tentative | entered-in-error
        :param start: Date/Time that the slot is to begin
        :param end: Date/Time that the slot is to conclude
        :param overbooked: This slot has already been overbooked, appointments are unlikely to be accepted for this time
        :param comment: Comments on the slot to describe any extended information. Such as custom constraints on the slot
        """
        super().__init__(
            resourceType="Schedule",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            serviceCategory=serviceCategory,
            serviceType=serviceType,
            specialty=specialty,
            appointmentType=appointmentType,
            schedule=schedule,
            status=status,
            start=start,
            end=end,
            overbooked=overbooked,
            comment=comment,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return SlotSchema.get_schema(include_extension=include_extension)
