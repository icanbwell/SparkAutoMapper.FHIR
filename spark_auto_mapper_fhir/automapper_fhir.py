from typing import List

from spark_auto_mapper.automappers.automapper import AutoMapper

from spark_auto_mapper_fhir.automapper_with_resource import AutoMapperWithResource
from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperFhir(AutoMapper):
    def __init__(self, view: str, source_view: str, keys: List[str]):
        super().__init__(view=view, source_view=source_view, keys=keys)

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def withResource(self,
                     resource: AutoMapperFhirDataTypeComplexBase
                     ) -> 'AutoMapperFhir':
        resource_mapper: AutoMapperWithResource = AutoMapperWithResource(resource=resource)
        for column_name, child_mapper in resource_mapper.mappers.items():
            self.register_child(dst_column=column_name, child=child_mapper)
        return self
