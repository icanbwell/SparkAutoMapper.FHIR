from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RestfulSecurityServiceCode(GenericTypeCode):
    """
    RestfulSecurityService
    From: http://terminology.hl7.org/CodeSystem/restful-security-service in valuesets.xml
        Types of security services used with FHIR.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/restful-security-service
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/restful-security-service"


class RestfulSecurityServiceCodeValues:
    """
    OAuth (unspecified version see oauth.net).
    From: http://terminology.hl7.org/CodeSystem/restful-security-service in valuesets.xml
    """

    OAuth = RestfulSecurityServiceCode("OAuth")
    """
    OAuth2 using SMART-on-FHIR profile (see http://docs.smarthealthit.org/).
    From: http://terminology.hl7.org/CodeSystem/restful-security-service in valuesets.xml
    """
    SMART_on_FHIR = RestfulSecurityServiceCode("SMART-on-FHIR")
    """
    Microsoft NTLM Authentication.
    From: http://terminology.hl7.org/CodeSystem/restful-security-service in valuesets.xml
    """
    NTLM = RestfulSecurityServiceCode("NTLM")
    """
    Basic authentication defined in HTTP specification.
    From: http://terminology.hl7.org/CodeSystem/restful-security-service in valuesets.xml
    """
    Basic = RestfulSecurityServiceCode("Basic")
    """
    see http://www.ietf.org/rfc/rfc4120.txt.
    From: http://terminology.hl7.org/CodeSystem/restful-security-service in valuesets.xml
    """
    Kerberos = RestfulSecurityServiceCode("Kerberos")
    """
    SSL where client must have a certificate registered with the server.
    From: http://terminology.hl7.org/CodeSystem/restful-security-service in valuesets.xml
    """
    Certificates = RestfulSecurityServiceCode("Certificates")
