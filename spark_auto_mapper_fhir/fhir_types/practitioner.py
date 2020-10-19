from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.attachment import FhirAttachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.contact_point import FhirContactPoint
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.provider_qualification_backbone_element import \
    FhirProviderQualificationBackboneElement
from spark_auto_mapper_fhir.fhir_types.valuesets.administrative_gender import FhirAdministrativeGenderCode
from spark_auto_mapper_fhir.fhir_types.valuesets.common_language import FhirCommonLanguageCode


class FhirPractitioner(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        active: Optional[FhirBoolean] = None,
        name: Optional[FhirList[FhirHumanName]] = None,
        telecom: Optional[FhirList[FhirContactPoint]] = None,
        address: Optional[FhirList[FhirAddress]] = None,
        gender: Optional[FhirAdministrativeGenderCode] = None,
        birthDate: Optional[FhirDate] = None,
        photo: Optional[FhirList[FhirAttachment]] = None,
        qualification: Optional[
            FhirList[FhirProviderQualificationBackboneElement]] = None,
        communication: Optional[FhirList[
            FhirCodeableConcept[FhirCommonLanguageCode]]] = None
    ) -> 'FhirPractitioner':
        """
        Practitioner Resource in FHIR
        http://hl7.org/fhir/practitioner.html
        A person with a formal responsibility in the provisioning of healthcare or related services


        :param identifier: An identifier for the person as this agent
        :param active: Whether this practitioner's record is in active use
        :param name: The name(s) associated with the practitioner
        :param telecom: A contact detail for the practitioner (that apply to all roles)
        :param address: Address(es) of the practitioner that are not role specific (typically home address)
        :param gender: male | female | other | unknown. http://hl7.org/fhir/valueset-administrative-gender.html
        :param birthDate: The date on which the practitioner was born
        :param photo: Image of the person
        :param qualification: Certification, licenses, or training pertaining to the provision of care
        :param communication: A language the practitioner can use in patient communication.
                            http://hl7.org/fhir/valueset-languages.html
        """
        return FhirPractitioner(
            identifier=identifier,
            active=active,
            name=name,
            telecom=telecom,
            address=address,
            gender=gender,
            birthDate=birthDate,
            photo=photo,
            qualification=qualification,
            communication=communication
        )
