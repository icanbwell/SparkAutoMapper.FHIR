from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.observation_reference_range_backbone_element import \
    ObservationReferenceRangeBackboneElement
from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.fhir_types.time import FhirTime

from spark_auto_mapper_fhir.complex_types.range import Range
from spark_auto_mapper_fhir.complex_types.ratio import Ratio
from spark_auto_mapper_fhir.complex_types.sampled_data import SampledData
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase

from spark_auto_mapper_fhir.complex_types.quantity import Quantity

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.data_absent_reason import DataAbsentReasonCode
from spark_auto_mapper_fhir.valuesets.observation_code import LOINCCode
from spark_auto_mapper_fhir.valuesets.observation_interpretation import ObservationInterpretationCode


class ObservationComponentBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        code: CodeableConcept[LOINCCode],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        valueQuantity: Optional[Quantity] = None,
        valueCodeableConcept: Optional[CodeableConcept[FhirValueSetBase]
                                       ] = None,
        valueString: Optional[FhirString] = None,
        valueBoolean: Optional[FhirBoolean] = None,
        valueInteger: Optional[FhirInteger] = None,
        valueRange: Optional[Range] = None,
        valueRatio: Optional[Ratio] = None,
        valueSampledData: Optional[SampledData] = None,
        valueTime: Optional[FhirTime] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valuePeriod: Optional[Period] = None,
        dataAbsentReason: Optional[CodeableConcept[DataAbsentReasonCode]
                                   ] = None,
        interpretation: Optional[FhirList[ObservationInterpretationCode]
                                 ] = None,
        referenceRange: Optional[
            FhirList[ObservationReferenceRangeBackboneElement]] = None,
    ) -> None:
        """
        ObservationComponentBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/observation-definitions.html#Observation.component
        Component results


        :param code: Type of component observation (code / type)
        :param dataAbsentReason: Why the component result is missing
        :param interpretation: High, low, normal, etc.
        :param referenceRange: Provides guide for interpretation of component result
        """
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            valueQuantity=valueQuantity,
            valueCodeableConcept=valueCodeableConcept,
            valueString=valueString,
            valueBoolean=valueBoolean,
            valueInteger=valueInteger,
            valueRange=valueRange,
            valueRatio=valueRatio,
            valueSampledData=valueSampledData,
            valueTime=valueTime,
            valueDateTime=valueDateTime,
            valuePeriod=valuePeriod,
            dataAbsentReason=dataAbsentReason,
            interpretation=interpretation,
            referenceRange=referenceRange
        )
