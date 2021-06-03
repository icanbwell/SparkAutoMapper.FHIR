from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ActionRelationshipTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-action-relationship-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ActionRelationshipTypeCode"]) -> None:
            self.f: Callable[..., "ActionRelationshipTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ActionRelationshipTypeCode"]
        ) -> "ActionRelationshipTypeCode":
            return self.f(owner)

    @classproperty
    def BeforeStart(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed before the start of the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("before-start")

    @classproperty
    def Before(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed before the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("before")

    @classproperty
    def BeforeEnd(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed before the end of the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("before-end")

    @classproperty
    def ConcurrentWithStart(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed concurrent with the start of the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("concurrent-with-start")

    @classproperty
    def Concurrent(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed concurrent with the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("concurrent")

    @classproperty
    def ConcurrentWithEnd(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed concurrent with the end of the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("concurrent-with-end")

    @classproperty
    def AfterStart(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed after the start of the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("after-start")

    @classproperty
    def After(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed after the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("after")

    @classproperty
    def AfterEnd(cls) -> "ActionRelationshipTypeCode":
        """
        The action must be performed after the end of the related action.
        """
        # noinspection PyCallingNonCallable
        return ActionRelationshipTypeCode("after-end")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/action-relationship-type
        """
        return "http://hl7.org/fhir/ValueSet/action-relationship-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.813
        """
        return "2.16.840.1.113883.4.642.3.813"
