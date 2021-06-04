from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.administrative_gender import (
    AdministrativeGenderCode,
)
from spark_auto_mapper_fhir.valuesets.patient_contact_relationship import (
    PatientContactRelationshipCode,
)
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference


class Contact(FhirComplexTypeBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        relationship: Optional[
            FhirList[CodeableConcept[PatientContactRelationshipCode]]
        ] = None,
        name: Optional[HumanName] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[Address] = None,
        gender: Optional[AdministrativeGenderCode] = None,
        organization: Optional[Reference[Organization]] = None,
        period: Optional[Period] = None,
    ):
        """
        Contact Resource in FHIR
        https://hl7.org/FHIR/patient-definitions.html#Patient.contact
        A contact party (e.g. guardian, partner, friend) for the patient
        + Rule: SHALL at least contain a contact's details or a reference to an organization


        :param relationship: The kind of relationship. https://hl7.org/FHIR/valueset-patient-contactrelationship.html
        :param name: A name associated with the contact person
        :param telecom: A contact detail for the person
        :param address: Address for the contact person
        :param gender: male | female | other | unknown. https://hl7.org/FHIR/valueset-administrative-gender.html
        :param organization: Organization that is associated with the contact
        :param period: The period during which this contact person or organization is valid to be contacted relating to this patient
        """
        super().__init__(
            id_=id_,
            extension=extension,
            relationship=relationship,
            name=name,
            telecom=telecom,
            address=address,
            gender=gender,
            organization=organization,
            period=period,
        )
