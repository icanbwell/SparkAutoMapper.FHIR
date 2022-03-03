from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
from spark_auto_mapper_fhir.extensions.custom.nested_extension_item import (
    NestedExtensionItem,
)
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.value_sets.custom.search_characteristic import (
    SearchCharacteristicCode,
)


class SearchCharacteristicExtensionItem(NestedExtensionItem):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        valueCodeableConcept: CodeableConcept[SearchCharacteristicCode]
    ):
        """

        :param valueCodeableConcept:
        """
        super().__init__(
            id_=id_,
            url=SearchCharacteristicExtensionItem.codeset,
            valueCodeableConcept=valueCodeableConcept,
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        searchCharacteristic
        :return:
        :rtype:
        """
        return "searchCharacteristic"
