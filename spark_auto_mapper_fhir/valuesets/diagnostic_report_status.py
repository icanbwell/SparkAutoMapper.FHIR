from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DiagnosticReportStatusCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-diagnostic-report-status.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'DiagnosticReportStatusCode']
        ) -> None:
            self.f: Callable[..., 'DiagnosticReportStatusCode'] = f

        def __get__(
            self, obj: Any, owner: Type['DiagnosticReportStatusCode']
        ) -> 'DiagnosticReportStatusCode':
            return self.f(owner)

    @classproperty
    def Registered(cls) -> 'DiagnosticReportStatusCode':
        """
        The existence of the report is registered, but there is nothing yet available.
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("registered")

    @classproperty
    def Partial(cls) -> 'DiagnosticReportStatusCode':
        """
        This is a partial (e.g. initial, interim or preliminary) report: data in the report may be
        incomplete or unverified.
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("partial")

    @classproperty
    def Preliminary(cls) -> 'DiagnosticReportStatusCode':
        """
        Verified early results are available, but not all results are final.
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("preliminary")

    @classproperty
    def Final(cls) -> 'DiagnosticReportStatusCode':
        """
        The report is complete and verified by an authorized person.
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("final")

    @classproperty
    def Amended(cls) -> 'DiagnosticReportStatusCode':
        """
        Subsequent to being final, the report has been modified. This includes any change in the results, diagnosis,
         narrative text, or other content of a report that has been issued.
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("amended")

    @classproperty
    def Corrected(cls) -> 'DiagnosticReportStatusCode':
        """
        Subsequent to being final, the report has been modified to correct an error in the report or referenced results.
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("corrected")

    @classproperty
    def Appended(cls) -> 'DiagnosticReportStatusCode':
        """
        Subsequent to being final, the report has been modified by adding new content. The existing content is unchanged.
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("appended")

    @classproperty
    def Cancelled(cls) -> 'DiagnosticReportStatusCode':
        """
        The report is unavailable because the measurement was not started or not completed (also sometimes called "aborted").
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("cancelled")

    @classproperty
    def EnteredInError(cls) -> 'DiagnosticReportStatusCode':
        """
        The report has been withdrawn following a previous final release. This electronic record should never have
         existed, though it is possible that real-world decisions were based on it. (If real-world activity has
          occurred, the status should be "cancelled" rather than "entered-in-error".).
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("entered-in-error")

    @classproperty
    def Unknown(cls) -> 'DiagnosticReportStatusCode':
        """
        The authoring/source system does not know which of the status values currently applies for this observation.
        Note: This concept is not to be used for "other" - one of the listed statuses is presumed to apply, but
        the authoring/source system does not know which.
        """
        # noinspection PyCallingNonCallable
        return DiagnosticReportStatusCode("unknown")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/diagnostic-report-status
        """
        return "http://hl7.org/fhir/diagnostic-report-status"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.235
        """
        return "2.16.840.1.113883.4.642.3.235"
