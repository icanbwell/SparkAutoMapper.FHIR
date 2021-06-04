from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class MeasureReportTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-measure-report-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "MeasureReportTypeCode"]) -> None:
            self.f: Callable[..., "MeasureReportTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["MeasureReportTypeCode"]
        ) -> "MeasureReportTypeCode":
            return self.f(owner)

    @classproperty
    def Individual(cls) -> "MeasureReportTypeCode":
        """
        An individual report that provides information on the performance for a given measure with respect to a single subject.
        """
        # noinspection PyCallingNonCallable
        return MeasureReportTypeCode("individual")

    @classproperty
    def SubjectList(cls) -> "MeasureReportTypeCode":
        """
        A subject list report that includes a listing of subjects that satisfied each population criteria in the measure.
        """
        # noinspection PyCallingNonCallable
        return MeasureReportTypeCode("subject-list")

    @classproperty
    def Summary(cls) -> "MeasureReportTypeCode":
        """
        A summary report that returns the number of members in each population criteria for the measure.
        """
        # noinspection PyCallingNonCallable
        return MeasureReportTypeCode("summary")

    @classproperty
    def DataCollection(cls) -> "MeasureReportTypeCode":
        """
        A data collection report that contains data-of-interest for the measure.
        """
        # noinspection PyCallingNonCallable
        return MeasureReportTypeCode("data-collection")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/measure-report-type
        """
        return "http://hl7.org/fhir/measure-report-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.778
        """
        return "2.16.840.1.113883.4.642.3.778"
