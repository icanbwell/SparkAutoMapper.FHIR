from typing import Optional

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
        preferred: Optional[FhirBoolean] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
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
            language=language,
            preferred=preferred,
            extension=extension
        )
