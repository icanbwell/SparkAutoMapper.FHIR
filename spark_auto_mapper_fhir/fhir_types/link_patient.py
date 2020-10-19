from typing import Union, Any

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.related_person import FhirRelatedPerson
from spark_auto_mapper_fhir.fhir_types.valuesets.link_type import FhirLinkTypeCode


class FhirLinkPatient(FhirResourceBase):
    @classmethod
    def map(
        cls,
        other: FhirReference[Union[Any, FhirRelatedPerson]],
        # "Any" should be "FhirPatient" but causes a circular import
        type_: FhirLinkTypeCode
    ) -> 'FhirLinkPatient':
        """
        LinkPatient Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#LinkPatient
        Link to another patient resource that concerns the same actual person


        :param other: The other patient or related person resource that the link refers to
        :param type_: replaced-by | replaces | refer | seealso. https://hl7.org/FHIR/valueset-link-type.html
        """
        return FhirLinkPatient(other=other, type_=type_)
