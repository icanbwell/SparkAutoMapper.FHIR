from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.custom.insurance_plan_item import (
    InsurancePlanItemExtension,
)
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class InsurancePlanExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: Optional[FhirUri] = None,
        extension: Optional[FhirList[InsurancePlanItemExtension]] = None,
    ) -> None:
        """
        InsurancePlanExtension Extension type in FHIR


        :param url: Automatically set to codeset property if not passed in
        :param extension:
        """
        super().__init__(url=url or InsurancePlanExtension.codeset, extension=extension)

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/insurance_plan
        :return:
        :rtype:
        """
        return "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/insurance_plan"
