from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class ProviderSearchSystemExtensionItem(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(self, *, id_: Optional[FhirId] = None, valueUri: FhirUri):
        """

        :param valueUri:
        """
        super().__init__(
            id_=id_,
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
