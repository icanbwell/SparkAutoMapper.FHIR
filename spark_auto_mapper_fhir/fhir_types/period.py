from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperDateInputType


# noinspection SpellCheckingInspection
class AutoMapperFhirDataTypePeriod(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            start: Optional[AutoMapperDateInputType] = None,
            end: Optional[AutoMapperDateInputType] = None
            ) -> 'AutoMapperFhirDataTypePeriod':
        """
        Period Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Period
        Time range defined by start and end date/time
        + Rule: If present, start SHALL have a lower value than end

        :param start: Starting time with inclusive boundary
        :param end: End time with inclusive boundary, if not ongoing
        """
        return AutoMapperFhirDataTypePeriod(
            start=start,
            end=end
        )
