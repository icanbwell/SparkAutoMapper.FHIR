from typing import Optional

from spark_auto_mapper_fhir.extensions.custom.provider_search_availability_score import (
    AvailabilityScoreExtensionItem,
)
from spark_auto_mapper_fhir.extensions.custom.provider_search_characteristic import (
    SearchCharacteristicExtensionItem,
)
from spark_auto_mapper_fhir.extensions.custom.provider_search_system import (
    ProviderSearchSystemExtensionItem,
)

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class ProviderSearchExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        forSystem: ProviderSearchSystemExtensionItem,
        searchCharacteristic: Optional[
            FhirList[SearchCharacteristicExtensionItem]
        ] = None,
        availabilityScore: Optional[AvailabilityScoreExtensionItem] = None,
        id_: Optional[FhirId] = None,
    ) -> None:
        """


        :param forSystem: system for which the flags apply
        :param searchCharacteristic: codeable concept
        :param availabilityScore: Asymmetrik-provided score
        """

        super().__init__(
            url=ProviderSearchExtension.codeset,
            id_=id_,
            extension=[availabilityScore, searchCharacteristic, forSystem],
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/provider_search
        :return:
        :rtype:
        """
        return "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/provider_search"
