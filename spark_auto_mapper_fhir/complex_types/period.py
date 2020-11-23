from typing import Optional

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase

# noinspection SpellCheckingInspection
from spark_auto_mapper_fhir.fhir_types.date import FhirDate


class Period(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        start: Optional[FhirDate] = None,
        end: Optional[FhirDate] = None
    ):
        """
        Period Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Period
        Time range defined by start and end date/time
        + Rule: If present, start SHALL have a lower value than end

        :param start: Starting time with inclusive boundary
        :param end: End time with inclusive boundary, if not ongoing
        """
        super().__init__(id_=id_, start=start, end=end)
