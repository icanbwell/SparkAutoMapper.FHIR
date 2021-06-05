from typing import Optional, Union

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.us_core.detailed_ethnicity import (
    DetailedEthnicity,
)
from spark_auto_mapper_fhir.valuesets.us_core.omb_ethnicity_category import (
    OMBEthnicityCategory,
)


class EthnicityItem(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: Optional[FhirUri] = None,
        valueCoding: Optional[Union[OMBEthnicityCategory, DetailedEthnicity]] = None,
        valueString: Optional[FhirString] = None,
    ) -> None:
        """
        Extension type in FHIR
        """
        assert url in ["ombCategory", "detailed", "text"]
        assert url not in ["ombCategory", "detailed"] or valueCoding
        assert url not in ["text"] or valueString
        super().__init__(url=url, valueCoding=valueCoding, valueString=valueString)

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "urn:oid:2.16.840.1.113883.6.238"
