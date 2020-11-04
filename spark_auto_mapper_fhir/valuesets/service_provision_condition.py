from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ServiceProvisionConditionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-service-provision-conditions.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'ServiceProvisionConditionCode']
        ) -> None:
            self.f: Callable[..., 'ServiceProvisionConditionCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ServiceProvisionConditionCode']
        ) -> 'ServiceProvisionConditionCode':
            return self.f(owner)

    @classproperty
    def Free(cls) -> 'ServiceProvisionConditionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ServiceProvisionConditionCode("free")

    @classproperty
    def DiscountsAvailable(cls) -> 'ServiceProvisionConditionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ServiceProvisionConditionCode("disc")

    @classproperty
    def FeesApply(cls) -> 'ServiceProvisionConditionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ServiceProvisionConditionCode("cost")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/service-provision-conditions
        """
        return "http://terminology.hl7.org/CodeSystem/service-provision-conditions"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.514
        """
        return "2.16.840.1.113883.4.642.3.514"
