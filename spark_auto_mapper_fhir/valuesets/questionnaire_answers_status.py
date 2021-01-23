from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class QuestionnaireAnswersStatusCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR properties not just the ones you need
    https://www.hl7.org/fhir/valueset-questionnaire-answers-status.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'QuestionnaireAnswersStatusCode']
        ) -> None:
            self.f: Callable[..., 'QuestionnaireAnswersStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['QuestionnaireAnswersStatusCode']
        ) -> 'QuestionnaireAnswersStatusCode':
            return self.f(owner)

    @classproperty
    def InProgress(cls) -> 'QuestionnaireAnswersStatusCode':
        """
        This QuestionnaireResponse has been partially filled out with answers but changes or additions are still expected to be made to it.
        """
        # noinspection PyCallingNonCallable
        return QuestionnaireAnswersStatusCode("in-progress")

    @classproperty
    def Completed(cls) -> 'QuestionnaireAnswersStatusCode':
        """
        This QuestionnaireResponse has been filled out with answers and the current content is regarded as definitive.
        """
        # noinspection PyCallingNonCallable
        return QuestionnaireAnswersStatusCode("completed")

    @classproperty
    def Amended(cls) -> 'QuestionnaireAnswersStatusCode':
        """
        This QuestionnaireResponse has been filled out with answers, then marked as complete, yet changes or additions have been made to it afterwards.
        """
        # noinspection PyCallingNonCallable
        return QuestionnaireAnswersStatusCode("amended")

    @classproperty
    def EnteredInError(cls) -> 'QuestionnaireAnswersStatusCode':
        """
        This QuestionnaireResponse was entered in error and voided.
        """
        # noinspection PyCallingNonCallable
        return QuestionnaireAnswersStatusCode("entered-in-error")

    @classproperty
    def Stopped(cls) -> 'QuestionnaireAnswersStatusCode':
        """
        This QuestionnaireResponse has been partially filled out with answers but has been abandoned. It is unknown whether changes or additions are expected to be made to it.
        """
        # noinspection PyCallingNonCallable
        return QuestionnaireAnswersStatusCode("stopped")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/questionnaire-answers-status
        """
        return "http://hl7.org/fhir/questionnaire-answers-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        intentionally left blank
        """
        return ""
