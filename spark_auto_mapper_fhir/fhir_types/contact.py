from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.administrative_gender import FhirAdministrativeGenderCode
from spark_auto_mapper_fhir.fhir_types.valuesets.patient_contact_relationship import FhirPatientContactRelationshipCode
from spark_auto_mapper_fhir.fhir_types.contact_point import FhirContactPoint
from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference


class FhirContact(FhirResourceBase):
    @classmethod
    def map(
        cls,
        relationship: Optional[FhirList[
            FhirCodeableConcept[FhirPatientContactRelationshipCode]]] = None,
        name: Optional[FhirHumanName] = None,
        telecom: Optional[FhirList[FhirContactPoint]] = None,
        address: Optional[FhirAddress] = None,
        gender: Optional[FhirAdministrativeGenderCode] = None,
        organization: Optional[FhirReference[FhirOrganization]] = None,
        period: Optional[FhirPeriod] = None
    ) -> 'FhirContact':
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
        return FhirContact(
            relationship=relationship,
            name=name,
            telecom=telecom,
            address=address,
            gender=gender,
            organization=organization,
            period=period
        )
