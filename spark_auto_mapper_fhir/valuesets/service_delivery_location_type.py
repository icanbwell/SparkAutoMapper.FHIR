from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ServiceDeliveryLocationTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/v3/ServiceDeliveryLocationRoleType/vs.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'ServiceDeliveryLocationTypeCode']
        ) -> None:
            self.f: Callable[..., 'ServiceDeliveryLocationTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ServiceDeliveryLocationTypeCode']
        ) -> 'ServiceDeliveryLocationTypeCode':
            return self.f(owner)

    @classproperty
    def Hospital(cls) -> 'ServiceDeliveryLocationTypeCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ServiceDeliveryLocationTypeCode("HOSP")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/v3-RoleCode
        """
        return "http://terminology.hl7.org/CodeSystem/v3-RoleCode"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.1.11.17660
        """
        return "2.16.840.1.113883.1.11.17660"
