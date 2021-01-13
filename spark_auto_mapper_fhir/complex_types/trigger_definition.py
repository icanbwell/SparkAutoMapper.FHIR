from typing import Optional

from spark_auto_mapper_fhir.complex_types.data_requirement import DataRequirement
from spark_auto_mapper_fhir.complex_types.expression import Expression
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.valuesets.trigger_type import TriggerTypeCode


class TriggerDefinition(FhirComplexTypeBase):
    def __init__(
        self,
        type_: TriggerTypeCode,
        id_: Optional[FhirId] = None,
        name: Optional[FhirString] = None,
        data: Optional[FhirList[DataRequirement]] = None,
        condition: Optional[Expression] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        TriggerDefinition Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes.html#TriggerDefinition
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            name=name,
            data=data,
            condition=condition,
        )
