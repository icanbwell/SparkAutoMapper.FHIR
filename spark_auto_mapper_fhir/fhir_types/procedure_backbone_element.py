from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.data_types.list import AutoMapperDataTypeList
from spark_auto_mapper.type_definitions.defined_types import AutoMapperNumberInputType, AutoMapperDateInputType

from spark_auto_mapper_fhir.fhir_types.codeableConcept import AutoMapperFhirDataTypeCodeableConcept
from spark_auto_mapper_fhir.fhir_types.procedure import AutoMapperFhirDataTypeProcedure
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference


class AutoMapperFhirDataTypeProcedureBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(cls,
            sequence: AutoMapperNumberInputType,
            procedureCodeableConcept: AutoMapperFhirDataTypeCodeableConcept,
            type_: Optional[AutoMapperDataTypeList[AutoMapperFhirDataTypeCodeableConcept]] = None,
            date: Optional[AutoMapperDateInputType] = None,
            procedureReference: Optional[AutoMapperFhirDataTypeReference[AutoMapperFhirDataTypeProcedure]] = None
            ) -> 'AutoMapperFhirDataTypeProcedureBackboneElement':
        """
        ProcedureBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ProcedureBackboneElement
        Clinical procedures performed

        :param sequence: Procedure instance identifier
        :param procedureCodeableConcept: Specific clinical procedure. https://hl7.org/FHIR/valueset-icd-10-procedures.html
        :param type_: Category of Procedure. https://hl7.org/FHIR/valueset-ex-procedure-type.html
        :param date: When the procedure was performed
        :param procedureReference:
        """
        return AutoMapperFhirDataTypeProcedureBackboneElement(
            sequence=sequence,
            procedureCodeableConcept=procedureCodeableConcept,
            type_=type_,
            date=date,
            procedureReference=procedureReference
        )
