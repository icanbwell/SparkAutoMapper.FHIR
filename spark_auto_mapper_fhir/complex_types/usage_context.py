from typing import Optional, Union

from spark_auto_mapper_fhir.resources.insurance_plan import InsurancePlan

from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService

from spark_auto_mapper_fhir.resources.group import Group

from spark_auto_mapper_fhir.resources.location import Location

from spark_auto_mapper_fhir.resources.organization import Organization

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.complex_types.quantity import Quantity

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.complex_types.range import Range

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.plan_definition import PlanDefinition
from spark_auto_mapper_fhir.resources.research_study import ResearchStudy
from spark_auto_mapper_fhir.valuesets.usage_context_type import UsageContextTypeCode
from spark_auto_mapper_fhir.valuesets.use_context import ConformanceUseContextCode


class UsageContext(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[Coding[UsageContextTypeCode]] = None,
        valueCodeableConcept: Optional[
            CodeableConcept[ConformanceUseContextCode]] = None,
        valueQuantity: Optional[Quantity] = None,
        valueRange: Optional[Range] = None,
        valueReference: Optional[Reference[Union['PlanDefinition',
                                                 ResearchStudy, InsurancePlan,
                                                 HealthcareService, Group,
                                                 Location,
                                                 Organization]]] = None
    ) -> None:
        """
        UsageContext Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes-definitions.html#UsageContext
        """
        super().__init__(
            id_=id_,
            extension=extension,
            code=code,
            valueCodeableConcept=valueCodeableConcept,
            valueQuantity=valueQuantity,
            valueRange=valueRange,
            valueReference=valueReference
        )
