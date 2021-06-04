from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.valuesets.contact_point_system import ContactPointSystemCode
from spark_auto_mapper_fhir.valuesets.contact_point_use import ContactPointUseCode


class ContactPoint(FhirComplexTypeBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        system: Optional[ContactPointSystemCode] = None,
        value: Optional[FhirString] = None,
        use: Optional[ContactPointUseCode] = None,
        rank: Optional[FhirPositiveInt] = None,
        period: Optional[Period] = None,
    ):
        """
        ContactPoint Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ContactPoint
        Details of a Technology mediated contact point (phone, fax, email, etc.)
        + Rule: A system is required if a value is provided.

        :param system: phone | fax | email | pager | url | sms | other.
                        https://hl7.org/FHIR/valueset-contact-point-system.html
        :param value: The actual contact point details
        :param use: home | work | temp | old | mobile - purpose of this contact point.
                    https://hl7.org/FHIR/valueset-contact-point-use.html
        :param rank: Specify preferred order of use (1 = highest)
        :param period: Time period when the contact point was/is in use
        """
        super().__init__(
            id_=id_,
            extension=extension,
            system=system,
            value=value,
            use=use,
            rank=rank,
            period=period,
        )
