from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class MeasureReportStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-measure-report-status.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "MeasureReportStatusCode"]) -> None:
            self.f: Callable[..., "MeasureReportStatusCode"] = f

        def __get__(
            self, obj: Any, owner: Type["MeasureReportStatusCode"]
        ) -> "MeasureReportStatusCode":
            return self.f(owner)

    @classproperty
    def Complete(cls) -> "MeasureReportStatusCode":
        """
        The report is complete and ready for use.
        """
        # noinspection PyCallingNonCallable
        return MeasureReportStatusCode("complete")

    @classproperty
    def Pending(cls) -> "MeasureReportStatusCode":
        """
        The report is currently being generated.
        """
        # noinspection PyCallingNonCallable
        return MeasureReportStatusCode("pending")

    @classproperty
    def Error(cls) -> "MeasureReportStatusCode":
        """
        An error occurred attempting to generate the report.
        """
        # noinspection PyCallingNonCallable
        return MeasureReportStatusCode("error")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/measure-report-status
        """
        return "http://hl7.org/fhir/ValueSet/measure-report-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.776
        """
        return "2.16.840.1.113883.4.642.3.776"
