from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.common_language import FhirCommonLanguageCode


class FhirCommunication(FhirResourceBase):
    @classmethod
    def map(
        cls,
        language: FhirCodeableConcept[FhirCommonLanguageCode],
        preferred: Optional[FhirBoolean] = None
    ) -> 'FhirCommunication':
        """
        Communication Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Communication
        A language which may be used to communicate with the patient about his or her health


        :param language: The language which can be used to communicate with the patient about his or her health.
                        https://hl7.org/FHIR/valueset-languages.html
        :param preferred: Language preference indicator
        """
        return FhirCommunication(language=language, preferred=preferred)
