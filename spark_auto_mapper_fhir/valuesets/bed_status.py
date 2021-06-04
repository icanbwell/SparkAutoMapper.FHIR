from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class BedStatusCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/v2/0116/index.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "BedStatusCode"]) -> None:
            self.f: Callable[..., "BedStatusCode"] = f

        def __get__(self, obj: Any, owner: Type["BedStatusCode"]) -> "BedStatusCode":
            return self.f(owner)

    @classproperty
    def Closed(cls) -> "BedStatusCode":
        # noinspection PyCallingNonCallable
        return BedStatusCode("C")

    @classproperty
    def Housekeeping(cls) -> "BedStatusCode":
        # noinspection PyCallingNonCallable
        return BedStatusCode("H")

    @classproperty
    def Isolated(cls) -> "BedStatusCode":
        # noinspection PyCallingNonCallable
        return BedStatusCode("I")

    @classproperty
    def Contaminated(cls) -> "BedStatusCode":
        # noinspection PyCallingNonCallable
        return BedStatusCode("K")

    @classproperty
    def Occupied(cls) -> "BedStatusCode":
        # noinspection PyCallingNonCallable
        return BedStatusCode("O")

    @classproperty
    def Unoccupied(cls) -> "BedStatusCode":
        # noinspection PyCallingNonCallable
        return BedStatusCode("U")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/v2-0116
        """
        return "http://terminology.hl7.org/CodeSystem/v2-0116"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """ """
        return ""
