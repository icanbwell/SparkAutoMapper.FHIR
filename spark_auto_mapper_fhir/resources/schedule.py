from typing import Optional, Union

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.schedule import ScheduleSchema

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.device import Device
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson


class Schedule(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        actor: FhirList[Reference[Union[Patient, Practitioner,
                                        PractitionerRole, RelatedPerson,
                                        Device, HealthcareService, Location]]],
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        active: Optional[FhirBoolean] = None,
    ):
        """
        Schedule Resource in FHIR
        http://hl7.org/fhir/schedule.html
        A container for slots of time that may be available for booking appointments


        :param id_: id of resource
        :param actor: Resource(s) that availability information is being provided for
        :param identifier: An identifier for the schedule
        :param active: Whether this schedule is in active use
        """
        super().__init__(
            resourceType="Schedule",
            id_=id_,
            meta=meta,
            identifier=identifier,
            extension=extension,
            active=active,
            actor=actor,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return ScheduleSchema.get_schema(include_extension=include_extension)
