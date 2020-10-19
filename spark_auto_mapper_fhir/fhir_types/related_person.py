from typing import Optional

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.attachment import FhirAttachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.communication import FhirCommunication
from spark_auto_mapper_fhir.fhir_types.contact_point import FhirContactPoint
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.valuesets.administrative_gender import FhirAdministrativeGenderCode
from spark_auto_mapper_fhir.fhir_types.valuesets.relatedperson_relationshiptype import \
    FhirRelatedPersonRelationshipTypeCode


class FhirRelatedPerson(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        patient: FhirReference[
            FhirResourceBase
        ],  # should be FhirPatient but causes circular imports
        id_: Optional[FhirId] = None,
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        active: Optional[FhirBoolean] = None,
        relationship: Optional[FhirList[
            FhirCodeableConcept[FhirRelatedPersonRelationshipTypeCode]]
                               ] = None,
        name: Optional[FhirList[FhirHumanName]] = None,
        telecom: Optional[FhirList[FhirContactPoint]] = None,
        gender: Optional[FhirAdministrativeGenderCode] = None,
        birthDate: Optional[FhirDate] = None,
        address: Optional[FhirList[FhirAddress]] = None,
        photo: Optional[FhirList[FhirAttachment]] = None,
        period: Optional[FhirPeriod] = None,
        communication: Optional[FhirList[FhirCommunication]] = None
    ) -> 'FhirRelatedPerson':
        """
        RelatedPerson Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#RelatedPerson
        A person that is related to a patient, but who is not a direct target of care


        :param patient: The patient this person is related to

        :param id_: id
        :param identifier: 	A human identifier for this person
        :param active: Whether this related person's record is in active use
        :param relationship: The nature of the relationship.
                                http://hl7.org/fhir/valueset-relatedperson-relationshiptype.html
        :param name: A name associated with the person
        :param telecom: A contact detail for the person
        :param gender: 	male | female | other | unknown. http://hl7.org/fhir/valueset-administrative-gender.html
        :param birthDate: The date on which the related person was born
        :param address: Address where the related person can be contacted or visited
        :param photo: Image of the person
        :param period: Period of time that this relationship is considered valid
        :param communication: A language which may be used to communicate with about the patient's health
        """
        return FhirRelatedPerson(
            patient=patient,
            id_=id_,
            identifier=identifier,
            active=active,
            relationship=relationship,
            name=name,
            telecom=telecom,
            gender=gender,
            birthDate=birthDate,
            address=address,
            photo=photo,
            period=period,
            communication=communication
        )
