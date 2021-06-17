from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class VisionBaseCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-vision-base-codes.html
    """

    def __init__(self, *, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "VisionBaseCode"]) -> None:
            self.f: Callable[..., "VisionBaseCode"] = f

        def __get__(self, obj: Any, owner: Type["VisionBaseCode"]) -> "VisionBaseCode":
            return self.f(owner)

    @classproperty
    def Up(cls) -> "VisionBaseCode":
        """
        top.
        """
        # noinspection PyCallingNonCallable
        return VisionBaseCode(value="up")

    def Down(cls) -> "VisionBaseCode":
        """
        bottom.
        """
        # noinspection PyCallingNonCallable
        return VisionBaseCode(value="down")

    def In(cls) -> "VisionBaseCode":
        """
        inner edge.
        """
        # noinspection PyCallingNonCallable
        return VisionBaseCode(value="in")

    def Out(cls) -> "VisionBaseCode":
        """
        outer edge.
        """
        # noinspection PyCallingNonCallable
        return VisionBaseCode(value="out")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/vision-base-codes
        """
        return "http://hl7.org/fhir/ValueSet/vision-base-codes"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.662
        """
        return "2.16.840.1.113883.4.642.3.662"
