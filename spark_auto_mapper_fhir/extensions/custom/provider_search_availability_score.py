from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class AvailabilityScoreExtensionItem(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(self, valueDecimal: FhirDecimal):
        """

        :param valueDecimal:
        """
        super().__init__(
            url=AvailabilityScoreExtensionItem.codeset,
            valueDecimal=valueDecimal,
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        avalabilityScore
        :return:
        :rtype:
        """
        return "availabilityScore"
