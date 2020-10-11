from typing import List

from spark_auto_mapper.automappers.automapper import AutoMapper

from spark_auto_mapper_fhir.automapper_with_resource import AutoMapperWithResource
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperFhir(AutoMapper):
    def __init__(self, view: str, source_view: str, keys: List[str]):
        super().__init__(view=view, source_view=source_view, keys=keys)

    # noinspection PyPep8Naming
    def withResource(self,
                     resource: AutoMapperFhirDataTypeComplexBase
                     ) -> AutoMapperWithResource:
        return AutoMapperWithResource(parent=self, resource=resource)
