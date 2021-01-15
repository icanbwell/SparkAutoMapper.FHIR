from typing import Optional

from spark_auto_mapper_fhir.resources.group import Group

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.backbone_elements.participant_backbone_element import ParticipantBackboneElement
from spark_auto_mapper_fhir.backbone_elements.plan_definition_dynamicValue_backbone_element import \
    PlanDefinitionDynamicValueBackboneElement
from spark_auto_mapper_fhir.backbone_elements.timing_backbone_element import Timing
from spark_auto_mapper_fhir.complex_types.duration import Duration

from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.range import Range
from spark_auto_mapper_fhir.fhir_types.age import FhirAge

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.backbone_elements.related_action_backbone_element import RelatedActionBackboneElement
from spark_auto_mapper_fhir.complex_types.data_requirement import DataRequirement
from spark_auto_mapper_fhir.fhir_types.uri import FhirCanonical, FhirUri
from spark_auto_mapper_fhir.resources.related_artifact import RelatedArtifact
from spark_auto_mapper_fhir.valuesets.action_cardinality_behavior import ActionCardinalityBehaviorCode
from spark_auto_mapper_fhir.valuesets.action_grouping_behavior import ActionGroupingBehaviorCode
from spark_auto_mapper_fhir.valuesets.action_precheck_behavior import ActionPrecheckBehaviorCode
from spark_auto_mapper_fhir.valuesets.action_required_behavior import ActionRequiredBehaviorCode
from spark_auto_mapper_fhir.valuesets.action_selection_behavior import ActionSelectionBehaviorCode
from spark_auto_mapper_fhir.valuesets.action_type import ActionTypeCode
from spark_auto_mapper_fhir.valuesets.request_priority import RequestPriorityCode

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.backbone_elements.condition_backbone_element import ConditionBackboneElement
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.trigger_definition import TriggerDefinition
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper_fhir.valuesets.subject_type import SubjectTypeCode


class ActionBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        prefix: Optional[FhirString] = None,
        title: Optional[FhirString] = None,
        description: Optional[FhirString] = None,
        textEquivalent: Optional[FhirString] = None,
        priority: Optional[RequestPriorityCode] = None,
        code: Optional[FhirList[CodeableConcept[FhirValueSetBase]]] = None,
        reason: Optional[FhirList[CodeableConcept[FhirValueSetBase]]] = None,
        documentation: Optional[FhirList[RelatedArtifact]] = None,
        goalId: Optional[FhirList[FhirId]] = None,
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]
                                         ] = None,
        subjectReference: Optional[Reference[Group]] = None,
        trigger: Optional[FhirList[TriggerDefinition]] = None,
        condition: Optional[FhirList[ConditionBackboneElement]] = None,
        input_: Optional[FhirList[DataRequirement]] = None,
        output: Optional[FhirList[DataRequirement]] = None,
        relatedAction: Optional[FhirList[RelatedActionBackboneElement]] = None,
        timingDateTime: Optional[FhirDateTime] = None,
        timingAge: Optional[FhirAge] = None,
        timingPeriod: Optional[Period] = None,
        timingDuration: Optional[Duration] = None,
        timingRange: Optional[Range] = None,
        timingTiming: Optional[Timing] = None,
        participant: Optional[FhirList[ParticipantBackboneElement]] = None,
        type_: Optional[CodeableConcept[ActionTypeCode]] = None,
        groupingBehavior: Optional[ActionGroupingBehaviorCode] = None,
        selectionBehavior: Optional[ActionSelectionBehaviorCode] = None,
        requiredBehavior: Optional[ActionRequiredBehaviorCode] = None,
        precheckBehavior: Optional[ActionPrecheckBehaviorCode] = None,
        cardinalityBehavior: Optional[ActionCardinalityBehaviorCode] = None,
        definitionCanonical: Optional[FhirCanonical] = None,
        definitionUri: Optional[FhirUri] = None,
        transform: Optional[FhirCanonical] = None,
        dynamicValue: Optional[
            FhirList[PlanDefinitionDynamicValueBackboneElement]] = None,
        action: Optional[FhirList['ActionBackboneElement']] = None
    ) -> None:
        """
        ActionBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/plandefinition-definitions.html#PlanDefinition.action
        Action defined by the plan

        :param prefix: User-visible prefix for the action (e.g. 1. or A.)
        :param title: User-visible title
        :param description: Brief description of the action
        :param textEquivalent: Static text equivalent of the action, used if the dynamic aspects cannot be interpreted
                                by the receiving system
        :param priority: routine | urgent | asap | stat
        :param code: Code representing the meaning of the action or sub-actions
        :param reason: Why the action should be performed
        :param documentation: Supporting documentation for the intended performer of the action
        :param goalId: What goals this action supports
        :param subjectCodeableConcept: Type of individual the action is focused on
        :param subjectReference: Type of individual the action is focused on
        :param trigger: When the action should be triggered
        :param condition: Whether or not the action is applicable
        :param input_: Input data requirements
        :param output: Output data definition
        :param relatedAction: Relationship to another action
        :param timingDateTime: When the action should take place
        :param timingAge: When the action should take place
        :param timingPeriod: When the action should take place
        :param timingDuration: When the action should take place
        :param timingRange: When the action should take place
        :param timingTiming: When the action should take place
        :param participant: Who should participate in the action
        :param type_: create | update | remove | fire-event
        :param groupingBehavior: visual-group | logical-group | sentence-group
        :param selectionBehavior: any | all | all-or-none | exactly-one | at-most-one | one-or-more
        :param requiredBehavior: must | could | must-unless-documented
        :param precheckBehavior: yes | no
        :param cardinalityBehavior: single | multiple
        :param definitionCanonical: Description of the activity to be performed
        :param definitionUri: Description of the activity to be performed
        :param transform: Transform to apply the template
        :param dynamicValue: Dynamic aspects of the definition
        """
        super().__init__(
            id_=id_,
            extension=extension,
            prefix=prefix,
            title=title,
            description=description,
            textEquivalent=textEquivalent,
            priority=priority,
            code=code,
            reason=reason,
            documentation=documentation,
            goalId=goalId,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            trigger=trigger,
            condition=condition,
            input_=input_,
            output=output,
            relatedAction=relatedAction,
            timingDateTime=timingDateTime,
            timingAge=timingAge,
            timingPeriod=timingPeriod,
            timingDuration=timingDuration,
            timingRange=timingRange,
            timingTiming=timingTiming,
            participant=participant,
            type_=type_,
            groupingBehavior=groupingBehavior,
            selectionBehavior=selectionBehavior,
            requiredBehavior=requiredBehavior,
            precheckBehavior=precheckBehavior,
            cardinalityBehavior=cardinalityBehavior,
            definitionCanonical=definitionCanonical,
            definitionUri=definitionUri,
            transform=transform,
            dynamicValue=dynamicValue,
            action=action
        )
