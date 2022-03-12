from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class PositionExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        longitude: FhirDecimal,
        latitude: FhirDecimal,
        altitude: Optional[FhirDecimal] = None,
    ) -> None:
        """
        Position Extension type in FHIR


        :param longitude:
        :param latitude:
        :param altitude: (Optional)
        """
        definition_base_url = "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/"
        position_extensions = [
            ExtensionBase(
                url=f"{definition_base_url}longitude", valueDecimal=longitude
            ),
            ExtensionBase(url=f"{definition_base_url}latitude", valueDecimal=latitude),
        ]
        if altitude:
            position_extensions.append(
                ExtensionBase(
                    url=f"{definition_base_url}altitude", valueDecimal=altitude
                )
            )
        super().__init__(
            id_=id_, extension=FhirList(position_extensions), url=self.__class__.codeset
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/position
        :return:
        :rtype:
        """
        return "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/position"
