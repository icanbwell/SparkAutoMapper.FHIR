from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperDateInputType

from spark_auto_mapper_fhir.fhir_types.period import AutoMapperFhirDataTypePeriod


class AutoMapperFhirDataTypeServiceDateOrPeriod(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            servicedDate: Optional[AutoMapperDateInputType] = None,
            servicedPeriod: Optional[AutoMapperFhirDataTypePeriod] = None
            ) -> 'AutoMapperFhirDataTypeServiceDateOrPeriod':
        """
        ServiceDateOrPeriod Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit.html
        Date or dates of service or product delivery

        :param servicedDate: date
        :param servicedPeriod: period
        """
        return AutoMapperFhirDataTypeServiceDateOrPeriod(
            servicedDate=servicedDate,
            servicedPeriod=servicedPeriod
        )
