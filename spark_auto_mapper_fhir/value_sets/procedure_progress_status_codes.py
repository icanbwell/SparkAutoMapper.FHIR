from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ProcedureProgressStatusCodesCode(GenericTypeCode):
    """
    ProcedureProgressStatusCodes
    From: http://hl7.org/fhir/procedure-progress-status-code in valuesets.xml
        This value set is provided as an example. The value set to instantiate this
    attribute should be drawn from a robust terminology code system that consists
    of or contains concepts to support the procedure performance process.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/procedure-progress-status-code
    """
    codeset: FhirUri = "http://hl7.org/fhir/procedure-progress-status-code"


class ProcedureProgressStatusCodesCodeValues:
    """
    A patient is in the Operating Room.
    From: http://hl7.org/fhir/procedure-progress-status-code in valuesets.xml
    """

    InOperatingRoom = ProcedureProgressStatusCodesCode("in-operating-room")
    """
    The patient is prepared for a procedure.
    From: http://hl7.org/fhir/procedure-progress-status-code in valuesets.xml
    """
    Prepared = ProcedureProgressStatusCodesCode("prepared")
    """
    The patient is under anesthesia.
    From: http://hl7.org/fhir/procedure-progress-status-code in valuesets.xml
    """
    AnesthesiaInduced = ProcedureProgressStatusCodesCode("anesthesia-induced")
    """
    The patient has open incision(s).
    From: http://hl7.org/fhir/procedure-progress-status-code in valuesets.xml
    """
    OpenIncision = ProcedureProgressStatusCodesCode("open-incision")
    """
    The patient has incision(s) closed.
    From: http://hl7.org/fhir/procedure-progress-status-code in valuesets.xml
    """
    ClosedIncision = ProcedureProgressStatusCodesCode("closed-incision")
    """
    The patient is in the recovery room.
    From: http://hl7.org/fhir/procedure-progress-status-code in valuesets.xml
    """
    InRecoveryRoom = ProcedureProgressStatusCodesCode("in-recovery-room")
