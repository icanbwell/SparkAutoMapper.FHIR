from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class HL7ContextConductionStyle(GenericTypeCode):
    """
    v3.HL7ContextConductionStyle
    From: http://terminology.hl7.org/ValueSet/v3-HL7ContextConductionStyle in v3-codesystems.xml
        The styles of context conduction usable by relationships within a static model
    derived from tyhe HL7 Reference Information Model.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-HL7ContextConductionStyle
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/v3-HL7ContextConductionStyle"
    )


class HL7ContextConductionStyleValues:
    """
    Definition: Context conduction is defined using the contextConductionCode and
    contextConductionInd attributes on ActRelationship and Participation.


                               UsageNotes: This approach is deprecated as of
    March, 2010.
    From: http://terminology.hl7.org/CodeSystem/v3-HL7ContextConductionStyle in v3-codesystems.xml
    """

    Conduction_indicator_based = HL7ContextConductionStyle("C")
    """
    Definition: Context conduction is not explicitly defined.  The recipient of an
    instance must infer conduction based on the semantics of the model and what is
    deemed "reasonable".
    
    
                               UsageNotes: Because this approach can lead to
    variation in instance interpretation, its use is discouraged.
    From: http://terminology.hl7.org/CodeSystem/v3-HL7ContextConductionStyle in v3-codesystems.xml
    """
    Inferred = HL7ContextConductionStyle("I")
    """
    Definition: Context conduction is defined using the
    ActRelationship.blockedContextActRelationshipType and
    blockedContextParticipationType attributes and the "conductible" property on
    the ActRelationshipType and ParticipationType code systems.
    From: http://terminology.hl7.org/CodeSystem/v3-HL7ContextConductionStyle in v3-codesystems.xml
    """
    Vocabulary_based = HL7ContextConductionStyle("V")
