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
        extension: Optional[FhirList[ExtensionBase]] = None,
        description: Optional[FhirString] = None,
        name: Optional[FhirId] = None,
        expression: Optional[FhirString] = None,
        reference: Optional[FhirUri] = None,
    ) -> None:
        """
        Expression Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes.html#Expression
        An expression that can be used to generate a value
        + Rule: An expression or a reference must be provided


        :param description: Natural language description of the condition
        :param name: Short name assigned to expression for reuse
        :param language: text/cql | text/fhirpath | application/x-fhir-query | etc.
        :param expression: Expression in specified language
        :param reference: Where the expression is found
        """
        super().__init__(
            id_=id_,
            extension=extension,
            description=description,
            name=name,
            language=language,
            expression=expression,
            reference=reference,
        )
