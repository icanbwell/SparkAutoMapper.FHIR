from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.common_language import CommonLanguageCode


class Expression(FhirComplexTypeBase):
    def __init__(
        self,
        language: CommonLanguageCode,
        id_: Optional[FhirId] = None,
        description: Optional[FhirString] = None,
        name: Optional[FhirId] = None,
        expression: Optional[FhirString] = None,
        reference: Optional[FhirUri] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        Expression Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes.html#Expression
        """
        super().__init__(
            id_=id_,
            description=description,
            name=name,
            language=language,
            expression=expression,
            reference=reference,
            extension=extension
        )
