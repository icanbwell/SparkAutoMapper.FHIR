from typing import Optional

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.fhir_types.date import FhirDate

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.backbone_elements.timing_backbone_element import Timing
from spark_auto_mapper_fhir.complex_types.data_requirement import DataRequirement
from spark_auto_mapper_fhir.complex_types.expression import Expression
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.schedule import Schedule
from spark_auto_mapper_fhir.valuesets.trigger_type import TriggerTypeCode


class TriggerDefinition(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        type_: TriggerTypeCode,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        name: Optional[FhirString] = None,
        timingTiming: Optional[Timing] = None,
        timingReference: Optional[Reference[Schedule]] = None,
        timingDate: Optional[FhirDate] = None,
        timingDateTime: Optional[FhirDateTime] = None,
        data: Optional[FhirList[DataRequirement]] = None,
        condition: Optional[Expression] = None,
    ) -> None:
        """
        TriggerDefinition Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes.html#TriggerDefinition
        Defines an expected trigger for a module
        + Rule: Either timing, or a data requirement, but not both
        + Rule: A condition only if there is a data requirement
        + Rule: A named event requires a name, a periodic event requires timing, and a data event requires data


        :param type_: named-event | periodic | data-changed | data-added | data-modified | data-removed
                        | data-accessed | data-access-ended
        :param name: 	Name or URI that identifies the event
        :param timingTiming: Timing of the event
        :param timingReference: Timing of the event
        :param timingDate: Timing of the event
        :param timingDateTime: Timing of the event
        :param data: Triggering data of the event (multiple = 'and')
        :param condition: Whether the event triggers (boolean expression)
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            name=name,
            timingTiming=timingTiming,
            timingReference=timingReference,
            timingDate=timingDate,
            timingDateTime=timingDateTime,
            data=data,
            condition=condition,
        )
