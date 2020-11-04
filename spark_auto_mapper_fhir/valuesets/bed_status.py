from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class BedStatus(FhirValueSetBase):
    """
    https://hl7.org/FHIR/v2/0116/index.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'BedStatus']) -> None:
            self.f: Callable[..., 'BedStatus'] = f

        def __get__(self, obj: Any, owner: Type['BedStatus']) -> 'BedStatus':
            return self.f(owner)

    @classproperty
    def Closed(cls) -> 'BedStatus':
        # noinspection PyCallingNonCallable
        return BedStatus("C")

    @classproperty
    def Housekeeping(cls) -> 'BedStatus':
        # noinspection PyCallingNonCallable
        return BedStatus("H")

    @classproperty
    def Isolated(cls) -> 'BedStatus':
        # noinspection PyCallingNonCallable
        return BedStatus("I")

    @classproperty
    def Contaminated(cls) -> 'BedStatus':
        # noinspection PyCallingNonCallable
        return BedStatus("K")

    @classproperty
    def Occupied(cls) -> 'BedStatus':
        # noinspection PyCallingNonCallable
        return BedStatus("O")

    @classproperty
    def Unoccupied(cls) -> 'BedStatus':
        # noinspection PyCallingNonCallable
        return BedStatus("U")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/v2-0116
        """
        return "http://terminology.hl7.org/CodeSystem/v2-0116"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        """
        return ""
