from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class VisionEyesCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://hl7.org/FHIR/valueset-vision-eye-codes.html
    """

    def __init__(self, *, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "VisionEyesCode"]) -> None:
            self.f: Callable[..., "VisionEyesCode"] = f

        def __get__(self, obj: Any, owner: Type["VisionEyesCode"]) -> "VisionEyesCode":
            return self.f(owner)

    @classproperty
    def RightEye(cls) -> "VisionEyesCode":
        """
        Right Eye.
        """
        # noinspection PyCallingNonCallable
        return VisionEyesCode(value="right")

    def LeftEye(cls) -> "VisionEyesCode":
        """
        Left Eye.
        """
        # noinspection PyCallingNonCallable
        return VisionEyesCode(value="left")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/vision-eye-codes
        """
        return "http://hl7.org/fhir/ValueSet/vision-eye-codes"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.660
        """
        return "2.16.840.1.113883.4.642.3.660"
