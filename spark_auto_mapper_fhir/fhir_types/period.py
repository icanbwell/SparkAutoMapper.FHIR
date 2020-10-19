from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

# noinspection SpellCheckingInspection
from spark_auto_mapper_fhir.fhir_types.date import FhirDate


class FhirPeriod(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        start: Optional[FhirDate] = None,
        end: Optional[FhirDate] = None
    ) -> 'FhirPeriod':
        """
        Period Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Period
        Time range defined by start and end date/time
        + Rule: If present, start SHALL have a lower value than end

        :param start: Starting time with inclusive boundary
        :param end: End time with inclusive boundary, if not ongoing
        """
        return FhirPeriod(start=start, end=end)
