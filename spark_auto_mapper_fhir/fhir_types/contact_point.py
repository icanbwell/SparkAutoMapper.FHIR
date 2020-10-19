from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.valuesets.contact_point_system import FhirContactPointSystemCode
from spark_auto_mapper_fhir.fhir_types.valuesets.contact_point_use import FhirContactPointUseCode


class FhirContactPoint(FhirResourceBase):
    @classmethod
    def map(
        cls,
        system: Optional[FhirContactPointSystemCode] = None,
        value: Optional[FhirString] = None,
        use: Optional[FhirContactPointUseCode] = None,
        rank: Optional[FhirPositiveInt] = None,
        period: Optional[FhirPeriod] = None
    ) -> 'FhirContactPoint':
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
        return FhirContactPoint(
            system=system, value=value, use=use, rank=rank, period=period
        )
