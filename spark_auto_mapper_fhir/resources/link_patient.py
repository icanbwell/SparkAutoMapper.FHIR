from typing import Union, Any

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.reference import Reference
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.valuesets.link_type import LinkTypeCode


class LinkPatient(FhirResourceBase):
    def __init__(
        self,
        other: Reference[Union[Any, RelatedPerson]],
        # "Any" should be "FhirPatient" but causes a circular import
        type_: LinkTypeCode
    ):
        """
        LinkPatient Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#LinkPatient
        Link to another patient resource that concerns the same actual person


        :param other: The other patient or related person resource that the link refers to
        :param type_: replaced-by | replaces | refer | seealso. https://hl7.org/FHIR/valueset-link-type.html
        """
        super().__init__(other=other, type_=type_)
