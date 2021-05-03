from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class FromNetworkExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(self, valueReference: Reference[Organization]) -> None:
        """
        From Network
        http://hl7.org/fhir/us/davinci-pdex-plan-net/StructureDefinition/newpatients

        :param url:
        :param valueReference:
        """
        super().__init__(
            url=FromNetworkExtension.codeset, valueReference=valueReference
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        fromNetwork
        :return:
        :rtype:
        """
        return "fromNetwork"
