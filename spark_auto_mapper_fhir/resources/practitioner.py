from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.address import Address
from spark_auto_mapper_fhir.resources.attachment import Attachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.resources.contact_point import ContactPoint
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.resources.human_name import HumanName
from spark_auto_mapper_fhir.resources.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.provider_qualification_backbone_element import \
    ProviderQualificationBackboneElement
from spark_auto_mapper_fhir.valuesets.administrative_gender import AdministrativeGenderCode
from spark_auto_mapper_fhir.valuesets.common_language import CommonLanguageCode


class Practitioner(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        identifier: Optional[FhirList[Identifier]] = None,
        active: Optional[FhirBoolean] = None,
        name: Optional[FhirList[HumanName]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[FhirList[Address]] = None,
        gender: Optional[AdministrativeGenderCode] = None,
        birthDate: Optional[FhirDate] = None,
        photo: Optional[FhirList[Attachment]] = None,
        qualification: Optional[FhirList[ProviderQualificationBackboneElement]
                                ] = None,
        communication: Optional[FhirList[CodeableConcept[CommonLanguageCode]]
                                ] = None
    ):
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
        super().__init__(
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
