from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ConditionClinicalStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-condition-clinical.html
    Preferred value set for Condition Clinical Status.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "ConditionClinicalStatusCode"]) -> None:
            self.f: Callable[..., "ConditionClinicalStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["ConditionClinicalStatusCode"]
        ) -> "ConditionClinicalStatusCode":
            return self.f(owner)

    @classproperty
    def Active(cls) -> "ConditionClinicalStatusCode":
        """
        The subject is currently experiencing the symptoms of the condition or there is evidence of the condition.
        """
        # noinspection PyCallingNonCallable
        return ConditionClinicalStatusCode("active")

    @classproperty
    def Recurrence(cls) -> "ConditionClinicalStatusCode":
        """
        The subject is experiencing a re-occurence or repeating of a previously resolved condition,
        e.g. urinary tract infection, pancreatitis, cholangitis, conjunctivitis.
        """
        # noinspection PyCallingNonCallable
        return ConditionClinicalStatusCode("recurrence")

    @classproperty
    def Relapse(cls) -> "ConditionClinicalStatusCode":
        """
        The subject is experiencing a return of a condition, or signs and symptoms after a period of improvement
        or remission, e.g. relapse of cancer, multiple sclerosis, rheumatoid arthritis, systemic lupus erythematosus,
        bipolar disorder, [psychotic relapse of] schizophrenia, etc.
        """
        # noinspection PyCallingNonCallable
        return ConditionClinicalStatusCode("relapse")

    @classproperty
    def Inactive(cls) -> "ConditionClinicalStatusCode":
        """
        The subject is no longer experiencing the symptoms of the condition or there is no longer evidence
        of the condition.
        """
        # noinspection PyCallingNonCallable
        return ConditionClinicalStatusCode("inactive")

    @classproperty
    def Remission(cls) -> "ConditionClinicalStatusCode":
        """
        The subject is no longer experiencing the symptoms of the condition, but there is a risk of the
        symptoms returning.
        """
        # noinspection PyCallingNonCallable
        return ConditionClinicalStatusCode("remission")

    @classproperty
    def Resolved(cls) -> "ConditionClinicalStatusCode":
        """
        The subject is no longer experiencing the symptoms of the condition and there is a negligible
        perceived risk of the symptoms returning.
        """
        # noinspection PyCallingNonCallable
        return ConditionClinicalStatusCode("resolved")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/condition-clinical
        """
        return "http://terminology.hl7.org/CodeSystem/condition-clinical"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.164
        """
        return "2.16.840.1.113883.4.642.3.164"
