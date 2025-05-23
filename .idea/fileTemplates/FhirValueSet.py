from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ${ClassName}Code(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    $Documentation
    """
    def __init__(self, *, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., '${ClassName}Code']) -> None:
            self.f: Callable[..., '${ClassName}Code'] = f

        def __get__(self, obj: Any, 
                    owner: Type['${ClassName}Code']
                    ) -> '${ClassName}Code':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> '${ClassName}Code':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ${ClassName}Code(value="A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        $SystemUri
        """
        return "$SystemUri"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        $OID
        """
        return "$OID"
