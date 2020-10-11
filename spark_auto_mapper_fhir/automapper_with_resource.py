from spark_auto_mapper.automappers.automapper_container import AutoMapperContainer

from spark_auto_mapper_fhir.fhir_types.automapper_fhir_data_type_complex_base import AutoMapperFhirDataTypeComplexBase


class AutoMapperWithResource(AutoMapperContainer):
    def __init__(self,
                 resource: AutoMapperFhirDataTypeComplexBase
                 ) -> None:
        super().__init__()

        self.resource: AutoMapperFhirDataTypeComplexBase = resource

        self.generate_mappers(mappers_dict={key: value for key, value in self.resource.value.items()})
