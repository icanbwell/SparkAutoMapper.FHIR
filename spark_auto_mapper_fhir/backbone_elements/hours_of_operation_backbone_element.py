from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.time import FhirTime
from spark_auto_mapper_fhir.valuesets.days_of_week import DaysOfWeekCode


class HoursOfOperationBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        daysOfWeek: Optional[FhirList[DaysOfWeekCode]] = None,
        allDay: Optional[FhirBoolean] = None,
        openingTime: Optional[FhirTime] = None,
        closingTime: Optional[FhirTime] = None,
    ) -> None:
        """
        HoursOfOperationBackboneElement Backbone Element in FHIR
        https://hl7.org/FHIR/location-definitions.html#Location.hoursOfOperation
        What days/times during a week is this location usually open


        :param daysOfWeek: mon | tue | wed | thu | fri | sat | sun
        :param allDay: 	The Location is open all day
        :param openingTime: Time that the Location opens
        :param closingTime: Time that the Location closes
        """
        super().__init__(
            id_=id_,
            extension=extension,
            daysOfWeek=daysOfWeek,
            allDay=allDay,
            openingTime=openingTime,
            closingTime=closingTime,
        )
