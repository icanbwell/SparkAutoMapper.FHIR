from typing import Optional, Union
from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.questionnaire import QuestionnaireSchema

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta


class Questionnaire(FhirResourceBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None,
    ) -> None:
        """
        Questionnaire Resource in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR properties not just the ones you need
        https://www.hl7.org/fhir/questionnaire.html


        :param id_: id of resource
        """
        # TODO fill in all the properties
        super().__init__(
            resourceType="Questionnaire", id_=id_, meta=meta, extension=extension
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return QuestionnaireSchema.get_schema(include_extension=include_extension)
