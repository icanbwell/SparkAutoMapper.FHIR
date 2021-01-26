from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class EmpiProcessingStatusExtension(ExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        processing_status: FhirString,
        date_processed: FhirDateTime,
        request_id: FhirString,
    ) -> None:
        """
        EmpiProcessingStatus Extension type in FHIR

        :param processing_status: The status of empi processing. Single value for now is 'processed'
        :param date_processed: Timestamp of when the record was processed
        :param request_id: A globally unique string of numbers to identify a specific request. Max length is 16.
        """
        definition_base_url = "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/"
        processing_status_extensions = [
            ExtensionBase(
                url=f"{definition_base_url}processing_status",
                valueString=processing_status,
            ),
            ExtensionBase(
                url=f"{definition_base_url}date_processed",
                valueDateTime=date_processed
            ),
            ExtensionBase(
                url=f"{definition_base_url}request_id",
                valueDateTime=request_id
            ),
        ]
        super().__init__(
            url=self.__class__.codeset,
            extension=FhirList(processing_status_extensions)
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/empi_processing_status
        :return:
        :rtype:
        """
        return "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/empi_processing_status"
