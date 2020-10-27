from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ${ClassName}(FhirValueSetBase):
    """
    $Documentation
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., '${ClassName}']) -> None:
            self.f: Callable[..., '${ClassName}'] = f

        def __get__(self, obj: Any, 
                    owner: Type['${ClassName}']
                    ) -> '${ClassName}':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> '${ClassName}':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ${ClassName}("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "$SystemUri"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "$OID"
