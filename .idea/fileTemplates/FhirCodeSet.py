from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase

# noinspection PyMethodParameters
# noinspection PyPep8Naming
class Fhir${ClassName}Code(FhirValueSetBase):
    """
    $Documentation
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'Fhir${ClassName}Code']) -> None:
            self.f: Callable[..., 'Fhir${ClassName}Code'] = f

        def __get__(self, obj: Any, 
                    owner: Type['Fhir${ClassName}Code']
                    ) -> 'Fhir${ClassName}Code':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'Fhir${ClassName}Code':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return Fhir${ClassName}Code("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "$SystemUri"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "$OID"
