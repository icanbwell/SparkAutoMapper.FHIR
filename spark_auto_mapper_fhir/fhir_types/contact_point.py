from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.code import FhirCode
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirContactPoint(AutoMapperDataTypeComplexBase):
    @classmethod
    def map(cls,
            system: Optional[FhirCode] = None,
            value: Optional[FhirString] = None,
            use: Optional[FhirCode] = None,
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
            system=system,
            value=value,
            use=use,
            rank=rank,
            period=period
        )
