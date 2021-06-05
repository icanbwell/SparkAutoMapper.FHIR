from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.resources.device import Device

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.resources.procedure import Procedure
from spark_auto_mapper_fhir.valuesets.ex_procedure_type import ExProcedureTypeCode
from spark_auto_mapper_fhir.valuesets.icd10_procedure import Icd10ProcedureCode


class ProcedureBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        sequence: FhirPositiveInt,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type_: Optional[FhirList[CodeableConcept[ExProcedureTypeCode]]] = None,
        date: Optional[FhirDate] = None,
        procedureCodeableConcept: Optional[CodeableConcept[Icd10ProcedureCode]] = None,
        procedureReference: Optional[Reference["Procedure"]] = None,
        udi: Optional[FhirList[Device]] = None,
    ):
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
        super().__init__(
            id_=id_,
            extension=extension,
            sequence=sequence,
            type_=type_,
            date=date,
            procedureCodeableConcept=procedureCodeableConcept,
            procedureReference=procedureReference,
            udi=udi,
        )
