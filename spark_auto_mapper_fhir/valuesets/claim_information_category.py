from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimInformationCategoryCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-informationcategory.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ClaimInformationCategoryCode"]) -> None:
            self.f: Callable[..., "ClaimInformationCategoryCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ClaimInformationCategoryCode"]
        ) -> "ClaimInformationCategoryCode":
            return self.f(owner)

    @classproperty
    def Information(cls) -> "ClaimInformationCategoryCode":
        """
        Codes conveying additional situation and condition information.
        """
        # noinspection PyCallingNonCallable
        return ClaimInformationCategoryCode("info")

    def Discharge(cls) -> "ClaimInformationCategoryCode":
        """
        Discharge status and discharge to locations.
        """
        # noinspection PyCallingNonCallable
        return ClaimInformationCategoryCode("discharge")

    def RelatedServices(cls) -> "ClaimInformationCategoryCode":
        """
        Nature and date of the related event e.g. Last exam, service, X-ray etc.
        """
        # noinspection PyCallingNonCallable
        return ClaimInformationCategoryCode("related")

    def Exception(cls) -> "ClaimInformationCategoryCode":
        """
        Insurance policy exceptions.
        """
        # noinspection PyCallingNonCallable
        return ClaimInformationCategoryCode("exception")

    def Other(cls) -> "ClaimInformationCategoryCode":
        """
        Other information identified by the type.system.
        """
        # noinspection PyCallingNonCallable
        return ClaimInformationCategoryCode("other")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/claiminformationcategory"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.582"
