from typing import Optional

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.range import Range

from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.referencerange_appliesto import ObservationReferenceRangeAppliesToCode
from spark_auto_mapper_fhir.valuesets.referencerange_meaning import ObservationReferenceRangeMeaningCode


class ObservationReferenceRangeBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        low: Optional[SimpleQuantity] = None,
        high: Optional[SimpleQuantity] = None,
        type_: Optional[CodeableConcept[ObservationReferenceRangeMeaningCode]
                        ] = None,
        appliesTo: Optional[FhirList[
            CodeableConcept[ObservationReferenceRangeAppliesToCode]]] = None,
        age: Optional[Range] = None,
        text: Optional[FhirString] = None
    ) -> None:
        """
        ObservationReferenceRangeBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/observation-definitions.html#Observation.referenceRange
        Provides guide for interpretation
        + Rule: Must have at least a low or a high or text


        :param low: Low Range, if relevant
        :param high: High Range, if relevant
        :param type_: Reference range qualifier
        :param appliesTo: Reference range population
        :param age: Applicable age range, if relevant
        :param text: 	Text based reference range in an observation
        """
        super().__init__(
            id_=id_,
            extension=extension,
            low=low,
            high=high,
            type_=type_,
            appliesTo=appliesTo,
            age=age,
            text=text
        )
