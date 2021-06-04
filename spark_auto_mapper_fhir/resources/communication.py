from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.communication import CommunicationSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.common_language import CommonLanguageCode


class Communication(FhirResourceBase):
    def __init__(
        self,
        language: CodeableConcept[CommonLanguageCode],
        id_: FhirId,
        meta: Optional[Meta] = None,
        preferred: Optional[FhirBoolean] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ):
        """
        Communication Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Communication
        A language which may be used to communicate with the patient about his or her health


        :param language: The language which can be used to communicate with the patient about his or her health.
                        https://hl7.org/FHIR/valueset-languages.html
        :param id_: id of resource
        :param preferred: Language preference indicator
        """
        super().__init__(
            resourceType="Communication",
            id_=id_,
            meta=meta,
            extension=extension,
            language=language,
            preferred=preferred,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return CommunicationSchema.get_schema(include_extension=include_extension)
