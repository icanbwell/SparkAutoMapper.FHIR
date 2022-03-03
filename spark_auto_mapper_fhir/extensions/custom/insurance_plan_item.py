from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.custom.nested_extension_item import (
    NestedExtensionItem,
)
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.resources.insurance_plan import InsurancePlan


class InsurancePlanItemExtension(NestedExtensionItem):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        url: Optional[FhirUri] = None,
        valueReference: Optional[Reference[InsurancePlan]] = None,
    ) -> None:
        """
        InsurancePlanItemExtension Extension type in FHIR
        Used to define relationship between practitioner and insurance plan


        :param url: Set to "plan" if not passed in
        :param valueReference:
        """
        super().__init__(
            id_=id_,
            url=url or InsurancePlanItemExtension.codeset,
            valueReference=valueReference,
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        plan
        :return:
        :rtype:
        """
        return "plan"
