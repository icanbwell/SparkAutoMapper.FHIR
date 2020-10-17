from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.procedure import FhirProcedure
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference


class FhirProcedureBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    @classmethod
    def map(cls,
            sequence: FhirPositiveInt,
            procedureCodeableConcept: FhirCodeableConcept,
            type_: Optional[FhirList[FhirCodeableConcept]] = None,
            date: Optional[FhirDate] = None,
            procedureReference: Optional[FhirReference[FhirProcedure]] = None
            ) -> 'FhirProcedureBackboneElement':
        """
        ProcedureBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ProcedureBackboneElement
        Clinical procedures performed

        :param sequence: Procedure instance identifier
        :param procedureCodeableConcept: Specific clinical procedure.
                                        https://hl7.org/FHIR/valueset-icd-10-procedures.html
        :param type_: Category of Procedure. https://hl7.org/FHIR/valueset-ex-procedure-type.html
        :param date: When the procedure was performed
        :param procedureReference:
        """
        return FhirProcedureBackboneElement(
            sequence=sequence,
            procedureCodeableConcept=procedureCodeableConcept,
            type_=type_,
            date=date,
            procedureReference=procedureReference
        )
