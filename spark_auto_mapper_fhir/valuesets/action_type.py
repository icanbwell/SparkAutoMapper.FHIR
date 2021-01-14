from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ActionTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-action-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ActionTypeCode']) -> None:
            self.f: Callable[..., 'ActionTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ActionTypeCode']
        ) -> 'ActionTypeCode':
            return self.f(owner)

    @classproperty
    def Create(cls) -> 'ActionTypeCode':
        """
        The action is to create a new resource.
        """
        # noinspection PyCallingNonCallable
        return ActionTypeCode("create")

    @classproperty
    def Update(cls) -> 'ActionTypeCode':
        """
        The action is to update an existing resource.
        """
        # noinspection PyCallingNonCallable
        return ActionTypeCode("update")

    @classproperty
    def Remove(cls) -> 'ActionTypeCode':
        """
        The action is to remove an existing resource.
        """
        # noinspection PyCallingNonCallable
        return ActionTypeCode("remove")

    @classproperty
    def FireEvent(cls) -> 'ActionTypeCode':
        """
        The action is to fire a specific event.
        """
        # noinspection PyCallingNonCallable
        return ActionTypeCode("fire-event")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/action-type
        """
        return "http://hl7.org/fhir/ValueSet/action-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.809
        """
        return "2.16.840.1.113883.4.642.3.809"
