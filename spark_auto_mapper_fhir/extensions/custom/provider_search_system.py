from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class ProviderSearchSystemExtensionItem(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(self, valueUri: FhirUri):
        """

        :param valueUri:
        """
        super().__init__(
            url=ProviderSearchSystemExtensionItem.codeset,
            valueUri=valueUri,
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        forSystem
        :return:
        :rtype:
        """
        return "forSystem"
