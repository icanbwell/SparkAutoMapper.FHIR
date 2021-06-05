from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class QualityAdjustedLifeYears(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self, url: Optional[FhirUri] = None, valueDecimal: Optional[FhirDecimal] = None
    ) -> None:
        """
        Extension type in FHIR
        """
        super().__init__(
            url=url or QualityAdjustedLifeYears.codeset, valueDecimal=valueDecimal
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://synthetichealth.github.io/synthea/quality-adjusted-life-years"
