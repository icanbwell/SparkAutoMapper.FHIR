from typing import Optional, Union

from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.resources.organization import Organization

from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

from spark_auto_mapper_fhir.resources.patient import Patient

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.resources.practitioner import Practitioner

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)


class Annotation(FhirComplexTypeBase):
    def __init__(
        self,
        text: FhirMarkdown,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        authorReference: Optional[
            Reference[Union[Practitioner, Patient, RelatedPerson, Organization]]
        ] = None,
        authorString: Optional[FhirString] = None,
        time: Optional[FhirDateTime] = None,
    ) -> None:
        """
        Annotation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Annotation
        A text note which also contains information about who made the statement and when.

        :param text: The text of the annotation in markdown format.
        :param authorReference: The individual responsible for making the annotation.
        :param authorString: The individual responsible for making the annotation.
        :param time: Indicates when this particular annotation was made.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            authorReference=authorReference,
            authorString=authorString,
            time=time,
            text=text,
        )
