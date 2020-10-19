from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.common_language import CommonLanguageCode


class Communication(FhirResourceBase):
    def __init__(
        self,
        language: CodeableConcept[CommonLanguageCode],
        preferred: Optional[FhirBoolean] = None
    ):
        """
        Communication Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Communication
        A language which may be used to communicate with the patient about his or her health


        :param language: The language which can be used to communicate with the patient about his or her health.
                        https://hl7.org/FHIR/valueset-languages.html
        :param preferred: Language preference indicator
        """
        super().__init__(language=language, preferred=preferred)
