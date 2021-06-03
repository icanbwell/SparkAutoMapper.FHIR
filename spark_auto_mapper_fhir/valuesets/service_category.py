from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ServiceCategoryCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-service-category.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ServiceCategoryCode"]) -> None:
            self.f: Callable[..., "ServiceCategoryCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ServiceCategoryCode"]
        ) -> "ServiceCategoryCode":
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> "ServiceCategoryCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ServiceCategoryCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/service-category
        """
        return "http://terminology.hl7.org/CodeSystem/service-category"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.516
        """
        return "2.16.840.1.113883.4.642.3.516"
