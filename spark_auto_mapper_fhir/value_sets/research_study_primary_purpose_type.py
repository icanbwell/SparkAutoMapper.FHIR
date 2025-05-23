from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ResearchStudyPrimaryPurposeTypeCode(GenericTypeCode):
    """
    ResearchStudyPrimaryPurposeType
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
        Codes for the main intent of the study.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type
    """
    codeset: FhirUri = (
        "http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type"
    )


class ResearchStudyPrimaryPurposeTypeCodeValues:
    """
    One or more interventions are being evaluated for treating a disease,
    syndrome, or condition.
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
    """

    Treatment = ResearchStudyPrimaryPurposeTypeCode("treatment")
    """
    One or more interventions are being assessed for preventing the development of
    a specific disease or health condition.
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
    """
    Prevention = ResearchStudyPrimaryPurposeTypeCode("prevention")
    """
    One or more interventions are being evaluated for identifying a disease or
    health condition.
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
    """
    Diagnostic = ResearchStudyPrimaryPurposeTypeCode("diagnostic")
    """
    One or more interventions are evaluated for maximizing comfort, minimizing
    side effects, or mitigating against a decline in the participant's health or
    function.
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
    """
    SupportiveCare = ResearchStudyPrimaryPurposeTypeCode("supportive-care")
    """
    One or more interventions are assessed or examined for identifying a
    condition, or risk factors for a condition, in people who are not yet known to
    have the condition or risk factor.
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
    """
    Screening = ResearchStudyPrimaryPurposeTypeCode("screening")
    """
    One or more interventions for evaluating the delivery, processes, management,
    organization, or financing of healthcare.
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
    """
    HealthServicesResearch = ResearchStudyPrimaryPurposeTypeCode(
        "health-services-research"
    )
    """
    One or more interventions for examining the basic mechanism of action (for
    example, physiology or biomechanics of an intervention).
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
    """
    BasicScience = ResearchStudyPrimaryPurposeTypeCode("basic-science")
    """
    An intervention of a device product is being evaluated to determine the
    feasibility of the product or to test a prototype device and not health
    outcomes. Such studies are conducted to confirm the design and operating
    specifications of a device before beginning a full clinical trial.
    From: http://terminology.hl7.org/CodeSystem/research-study-prim-purp-type in valuesets.xml
    """
    DeviceFeasibility = ResearchStudyPrimaryPurposeTypeCode("device-feasibility")
