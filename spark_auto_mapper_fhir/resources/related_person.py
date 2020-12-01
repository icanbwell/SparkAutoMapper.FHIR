from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.relatedperson import RelatedPersonSchema

from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.attachment import Attachment
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.resources.communication import Communication
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.valuesets.administrative_gender import AdministrativeGenderCode
from spark_auto_mapper_fhir.valuesets.relatedperson_relationshiptype import \
    RelatedPersonRelationshipTypeCode


class RelatedPerson(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        patient: Reference[
            FhirResourceBase
        ],  # should be FhirPatient but causes circular imports
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        relationship: Optional[FhirList[
            CodeableConcept[RelatedPersonRelationshipTypeCode]]] = None,
        name: Optional[FhirList[HumanName]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        gender: Optional[AdministrativeGenderCode] = None,
        birthDate: Optional[FhirDate] = None,
        address: Optional[FhirList[Address]] = None,
        photo: Optional[FhirList[Attachment]] = None,
        period: Optional[Period] = None,
        communication: Optional[FhirList[Communication]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        RelatedPerson Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#RelatedPerson
        A person that is related to a patient, but who is not a direct target of care


        :param patient: The patient this person is related to

        :param id_: id of resource
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
        super().__init__(
            patient=patient,
            resourceType="RelatedPerson",
            id_=id_,
            meta=meta,
            extension=extension,
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

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return RelatedPersonSchema.get_schema(
            include_extension=include_extension
        )
