from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.money import Money
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class GeneralCostBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: Optional[CodeableConcept[FhirValueSetBase]] = None,
        groupSize: Optional[FhirPositiveInt] = None,
        cost: Optional[Money] = None,
        comment: Optional[FhirString] = None
    ) -> None:
        """
        GeneralCostBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/insuranceplan-definitions.html#InsurancePlan.plan.generalCost
        Overall costs


        :param type_: Type of cost
        :param groupSize: Number of enrollees
        :param cost: Cost value
        :param comment: Additional cost information
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            groupSize=groupSize,
            cost=cost,
            comment=comment
        )
