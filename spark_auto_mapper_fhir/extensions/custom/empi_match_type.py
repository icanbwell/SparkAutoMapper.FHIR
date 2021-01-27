from spark_auto_mapper_fhir.classproperty import genericclassproperty

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class EmpiMatchType(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(self, match_type: FhirString) -> None:
        """
        EmpiMatchType Extension type in FHIR

        :param match_type: The type of empi match for a patient
        """
        url: str = "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/empi_match_type"
        extensions = [ExtensionBase(url=url, valueString=match_type)]

        super().__init__(url=url, extension=FhirList(extensions))

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/empi_match_type
        :return:
        :rtype:
        """
        return "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/empi_match_type"
