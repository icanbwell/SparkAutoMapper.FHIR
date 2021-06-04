from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.resources.insurance_plan import InsurancePlan


class InsurancePlanItemExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
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
            url=url or InsurancePlanItemExtension.codeset, valueReference=valueReference
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
