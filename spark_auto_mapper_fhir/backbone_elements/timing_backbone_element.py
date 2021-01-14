from typing import Optional

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.complex_types.timing_repeat import TimingRepeat
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.timing_abbreviation import TimingAbbreviationCode


class Timing(FhirBackboneElementBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        event: Optional[FhirList[FhirDateTime]] = None,
        repeat: Optional[TimingRepeat] = None,
        code: Optional[CodeableConcept[TimingAbbreviationCode]] = None
    ) -> None:
        """
        Timing Backbone Element in FHIR
        https://www.hl7.org/fhir/datatypes.html#Timing
        A timing schedule that specifies an event that may occur multiple times


        :param event: When the event occurs
        :param repeat: When the event is to occur
        :param code: BID | TID | QID | AM | PM | QD | QOD | +
        """
        super().__init__(
            id_=id_,
            extension=extension,
            event=event,
            repeat=repeat,
            code=code
        )
