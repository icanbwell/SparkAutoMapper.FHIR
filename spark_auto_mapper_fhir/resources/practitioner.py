from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.attachment import Attachment
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.complex_types.human_name import HumanName
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.provider_qualification_backbone_element import \
    ProviderQualificationBackboneElement
from spark_auto_mapper_fhir.valuesets.administrative_gender import AdministrativeGenderCode
from spark_auto_mapper_fhir.valuesets.common_language import CommonLanguageCode


class Practitioner(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
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
                                ] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        Practitioner Resource in FHIR
        http://hl7.org/fhir/practitioner.html
        A person with a formal responsibility in the provisioning of healthcare or related services


        :param id_: id of resource
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
            resourceType="Practitioner",
            id_=id_,
            identifier=identifier,
            active=active,
            name=name,
            telecom=telecom,
            address=address,
            gender=gender,
            birthDate=birthDate,
            photo=photo,
            qualification=qualification,
            communication=communication,
            extension=extension
        )
