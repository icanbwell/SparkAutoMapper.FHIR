from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperDateInputType

from spark_auto_mapper_fhir.fhir_types.period import AutoMapperFhirDataTypePeriod


class AutoMapperFhirDataTypeTimingDateOrPeriod(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            timingDate: Optional[AutoMapperDateInputType] = None,
            timingPeriod: Optional[AutoMapperFhirDataTypePeriod] = None
            ) -> 'AutoMapperFhirDataTypeTimingDateOrPeriod':
        """
        TimingDateOrPeriod Resource in FHIR
        When it occurred

        :param timingDate: date
        :param timingPeriod: period
        """
        return AutoMapperFhirDataTypeTimingDateOrPeriod(
            timingDate=timingDate,
            timingPeriod=timingPeriod
        )
