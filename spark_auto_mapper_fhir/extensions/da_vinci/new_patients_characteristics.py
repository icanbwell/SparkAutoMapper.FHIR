from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class CharacteristicExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(self, valueString: "FhirString") -> None:
        """
        Characteristics of accepted patients
        http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients

        :param url:
        :param valueString:
        """
        super().__init__(url=CharacteristicExtension.codeset, valueString=valueString)

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        characteristic
        :return:
        :rtype:
        """
        return "characteristic"
