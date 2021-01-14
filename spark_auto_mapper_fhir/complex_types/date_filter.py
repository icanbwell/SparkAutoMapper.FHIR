from typing import Optional

from spark_auto_mapper_fhir.complex_types.duration import Duration

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase


class DateFilter(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        path: Optional[FhirString] = None,
        searchParam: Optional[FhirString] = None,
        valueDateTime: Optional[FhirDateTime] = None,
        valuePeriod: Optional[Period] = None,
        valueDuration: Optional[Duration] = None,
    ) -> None:
        """
        DateFilter Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes-definitions.html#DataRequirement.dateFilter
        What dates/date ranges are expected
        + Rule: Either a path or a searchParam must be provided, but not both


        :param path: A date-valued attribute to filter on
        :param searchParam: A date valued parameter to search on
        :param valueDateTime: The value of the filter, as a Period, DateTime, or Duration value
        :param valuePeriod: The value of the filter, as a Period, DateTime, or Duration value
        :param valueDuration: The value of the filter, as a Period, DateTime, or Duration value
        """
        super().__init__(
            id_=id_,
            extension=extension,
            path=path,
            searchParam=searchParam,
            valueDateTime=valueDateTime,
            valuePeriod=valuePeriod,
            valueDuration=valueDuration
        )
