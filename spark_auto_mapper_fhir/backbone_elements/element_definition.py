from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.resource import Resource
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # path (string)
    # representation (PropertyRepresentation)
    from spark_auto_mapper_fhir.value_sets.property_representation import (
        PropertyRepresentationCode,
    )

    # sliceName (string)
    # sliceIsConstraining (boolean)
    # label (string)
    # code (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

    # End Import for References for code
    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.loinc_codes import LOINCCodesCode

    # End Import for CodeableConcept for code
    # slicing (ElementDefinition.Slicing)
    from spark_auto_mapper_fhir.backbone_elements.element_definition_slicing import (
        ElementDefinitionSlicing,
    )

    # short (string)
    # definition (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # comment (markdown)
    # requirements (markdown)
    # alias (string)
    # min (unsignedInt)
    from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt

    # max (string)
    # base (ElementDefinition.Base)
    from spark_auto_mapper_fhir.backbone_elements.element_definition_base import (
        ElementDefinitionBase,
    )

    # contentReference (uri)
    # type_ (ElementDefinition.Type)
    from spark_auto_mapper_fhir.backbone_elements.element_definition_type import (
        ElementDefinitionType,
    )

    # defaultValueBase64Binary (base64Binary)
    from spark_auto_mapper_fhir.fhir_types.base64_binary import FhirBase64Binary

    # defaultValueBoolean (boolean)
    # defaultValueCanonical (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # defaultValueCode (generic_type)
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # defaultValueDate (date)
    # defaultValueDateTime (dateTime)
    # defaultValueDecimal (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # defaultValueId (id)
    # defaultValueInstant (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # defaultValueInteger (integer)
    # defaultValueMarkdown (markdown)
    # defaultValueOid (oid)
    from spark_auto_mapper_fhir.fhir_types.oid import FhirOid

    # defaultValuePositiveInt (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # defaultValueString (string)
    # defaultValueTime (time)
    from spark_auto_mapper_fhir.fhir_types.time import FhirTime

    # defaultValueUnsignedInt (unsignedInt)
    # defaultValueUri (uri)
    # defaultValueUrl (url)
    from spark_auto_mapper_fhir.fhir_types.url import FhirUrl

    # defaultValueUuid (uuid)
    from spark_auto_mapper_fhir.fhir_types.uuid import FhirUuid

    # defaultValueAddress (Address)
    from spark_auto_mapper_fhir.complex_types.address import Address

    # defaultValueAge (Age)
    from spark_auto_mapper_fhir.complex_types.age import Age

    # defaultValueAnnotation (Annotation)
    from spark_auto_mapper_fhir.complex_types.annotation import Annotation

    # defaultValueAttachment (Attachment)
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment

    # defaultValueCodeableConcept (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for defaultValueCodeableConcept
    # Import for CodeableConcept for defaultValueCodeableConcept
    # End Import for CodeableConcept for defaultValueCodeableConcept
    # defaultValueCoding (Coding)
    # End Import for References for defaultValueCoding
    # Import for CodeableConcept for defaultValueCoding
    # End Import for CodeableConcept for defaultValueCoding
    # defaultValueContactPoint (ContactPoint)
    from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint

    # defaultValueCount (Count)
    from spark_auto_mapper_fhir.complex_types.count import Count

    # defaultValueDistance (Distance)
    from spark_auto_mapper_fhir.complex_types.distance import Distance

    # defaultValueDuration (Duration)
    from spark_auto_mapper_fhir.complex_types.duration import Duration

    # defaultValueHumanName (HumanName)
    from spark_auto_mapper_fhir.complex_types.human_name import HumanName

    # defaultValueIdentifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # defaultValueMoney (Money)
    from spark_auto_mapper_fhir.complex_types.money import Money

    # defaultValuePeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # defaultValueQuantity (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # defaultValueRange (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # defaultValueRatio (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio

    # defaultValueReference (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for defaultValueReference
    # defaultValueSampledData (SampledData)
    from spark_auto_mapper_fhir.complex_types.sampled_data import SampledData

    # defaultValueSignature (Signature)
    from spark_auto_mapper_fhir.complex_types.signature import Signature

    # defaultValueTiming (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # defaultValueContactDetail (ContactDetail)
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail

    # defaultValueContributor (Contributor)
    from spark_auto_mapper_fhir.complex_types.contributor import Contributor

    # defaultValueDataRequirement (DataRequirement)
    from spark_auto_mapper_fhir.complex_types.data_requirement import DataRequirement

    # defaultValueExpression (Expression)
    from spark_auto_mapper_fhir.complex_types.expression import Expression

    # defaultValueParameterDefinition (ParameterDefinition)
    from spark_auto_mapper_fhir.complex_types.parameter_definition import (
        ParameterDefinition,
    )

    # defaultValueRelatedArtifact (RelatedArtifact)
    from spark_auto_mapper_fhir.complex_types.related_artifact import RelatedArtifact

    # defaultValueTriggerDefinition (TriggerDefinition)
    from spark_auto_mapper_fhir.complex_types.trigger_definition import (
        TriggerDefinition,
    )

    # defaultValueUsageContext (UsageContext)
    from spark_auto_mapper_fhir.complex_types.usage_context import UsageContext

    # defaultValueDosage (Dosage)
    from spark_auto_mapper_fhir.backbone_elements.dosage import Dosage

    # defaultValueMeta (Meta)
    from spark_auto_mapper_fhir.complex_types.meta import Meta

    # meaningWhenMissing (markdown)
    # orderMeaning (string)
    # fixedBase64Binary (base64Binary)
    # fixedBoolean (boolean)
    # fixedCanonical (canonical)
    # fixedCode (generic_type)
    # fixedDate (date)
    # fixedDateTime (dateTime)
    # fixedDecimal (decimal)
    # fixedId (id)
    # fixedInstant (instant)
    # fixedInteger (integer)
    # fixedMarkdown (markdown)
    # fixedOid (oid)
    # fixedPositiveInt (positiveInt)
    # fixedString (string)
    # fixedTime (time)
    # fixedUnsignedInt (unsignedInt)
    # fixedUri (uri)
    # fixedUrl (url)
    # fixedUuid (uuid)
    # fixedAddress (Address)
    # fixedAge (Age)
    # fixedAnnotation (Annotation)
    # fixedAttachment (Attachment)
    # fixedCodeableConcept (CodeableConcept)
    # End Import for References for fixedCodeableConcept
    # Import for CodeableConcept for fixedCodeableConcept
    # End Import for CodeableConcept for fixedCodeableConcept
    # fixedCoding (Coding)
    # End Import for References for fixedCoding
    # Import for CodeableConcept for fixedCoding
    # End Import for CodeableConcept for fixedCoding
    # fixedContactPoint (ContactPoint)
    # fixedCount (Count)
    # fixedDistance (Distance)
    # fixedDuration (Duration)
    # fixedHumanName (HumanName)
    # fixedIdentifier (Identifier)
    # fixedMoney (Money)
    # fixedPeriod (Period)
    # fixedQuantity (Quantity)
    # fixedRange (Range)
    # fixedRatio (Ratio)
    # fixedReference (Reference)
    # Imports for References for fixedReference
    # fixedSampledData (SampledData)
    # fixedSignature (Signature)
    # fixedTiming (Timing)
    # fixedContactDetail (ContactDetail)
    # fixedContributor (Contributor)
    # fixedDataRequirement (DataRequirement)
    # fixedExpression (Expression)
    # fixedParameterDefinition (ParameterDefinition)
    # fixedRelatedArtifact (RelatedArtifact)
    # fixedTriggerDefinition (TriggerDefinition)
    # fixedUsageContext (UsageContext)
    # fixedDosage (Dosage)
    # fixedMeta (Meta)
    # patternBase64Binary (base64Binary)
    # patternBoolean (boolean)
    # patternCanonical (canonical)
    # patternCode (generic_type)
    # patternDate (date)
    # patternDateTime (dateTime)
    # patternDecimal (decimal)
    # patternId (id)
    # patternInstant (instant)
    # patternInteger (integer)
    # patternMarkdown (markdown)
    # patternOid (oid)
    # patternPositiveInt (positiveInt)
    # patternString (string)
    # patternTime (time)
    # patternUnsignedInt (unsignedInt)
    # patternUri (uri)
    # patternUrl (url)
    # patternUuid (uuid)
    # patternAddress (Address)
    # patternAge (Age)
    # patternAnnotation (Annotation)
    # patternAttachment (Attachment)
    # patternCodeableConcept (CodeableConcept)
    # End Import for References for patternCodeableConcept
    # Import for CodeableConcept for patternCodeableConcept
    # End Import for CodeableConcept for patternCodeableConcept
    # patternCoding (Coding)
    # End Import for References for patternCoding
    # Import for CodeableConcept for patternCoding
    # End Import for CodeableConcept for patternCoding
    # patternContactPoint (ContactPoint)
    # patternCount (Count)
    # patternDistance (Distance)
    # patternDuration (Duration)
    # patternHumanName (HumanName)
    # patternIdentifier (Identifier)
    # patternMoney (Money)
    # patternPeriod (Period)
    # patternQuantity (Quantity)
    # patternRange (Range)
    # patternRatio (Ratio)
    # patternReference (Reference)
    # Imports for References for patternReference
    # patternSampledData (SampledData)
    # patternSignature (Signature)
    # patternTiming (Timing)
    # patternContactDetail (ContactDetail)
    # patternContributor (Contributor)
    # patternDataRequirement (DataRequirement)
    # patternExpression (Expression)
    # patternParameterDefinition (ParameterDefinition)
    # patternRelatedArtifact (RelatedArtifact)
    # patternTriggerDefinition (TriggerDefinition)
    # patternUsageContext (UsageContext)
    # patternDosage (Dosage)
    # patternMeta (Meta)
    # example (ElementDefinition.Example)
    from spark_auto_mapper_fhir.backbone_elements.element_definition_example import (
        ElementDefinitionExample,
    )

    # minValueDate (date)
    # minValueDateTime (dateTime)
    # minValueInstant (instant)
    # minValueTime (time)
    # minValueDecimal (decimal)
    # minValueInteger (integer)
    # minValuePositiveInt (positiveInt)
    # minValueUnsignedInt (unsignedInt)
    # minValueQuantity (Quantity)
    # maxValueDate (date)
    # maxValueDateTime (dateTime)
    # maxValueInstant (instant)
    # maxValueTime (time)
    # maxValueDecimal (decimal)
    # maxValueInteger (integer)
    # maxValuePositiveInt (positiveInt)
    # maxValueUnsignedInt (unsignedInt)
    # maxValueQuantity (Quantity)
    # maxLength (integer)
    # condition (id)
    # constraint (ElementDefinition.Constraint)
    from spark_auto_mapper_fhir.backbone_elements.element_definition_constraint import (
        ElementDefinitionConstraint,
    )

    # mustSupport (boolean)
    # isModifier (boolean)
    # isModifierReason (string)
    # isSummary (boolean)
    # binding (ElementDefinition.Binding)
    from spark_auto_mapper_fhir.backbone_elements.element_definition_binding import (
        ElementDefinitionBinding,
    )

    # mapping (ElementDefinition.Mapping)
    from spark_auto_mapper_fhir.backbone_elements.element_definition_mapping import (
        ElementDefinitionMapping,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ElementDefinition(FhirBackboneElementBase):
    """
    ElementDefinition
        Captures constraints on each element within the resource, profile, or extension.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        path: FhirString,
        representation: Optional[FhirList[PropertyRepresentationCode]] = None,
        sliceName: Optional[FhirString] = None,
        sliceIsConstraining: Optional[FhirBoolean] = None,
        label: Optional[FhirString] = None,
        code: Optional[FhirList[Coding[LOINCCodesCode]]] = None,
        slicing: Optional[ElementDefinitionSlicing] = None,
        short: Optional[FhirString] = None,
        definition: Optional[FhirMarkdown] = None,
        comment: Optional[FhirMarkdown] = None,
        requirements: Optional[FhirMarkdown] = None,
        alias: Optional[FhirList[FhirString]] = None,
        min: Optional[FhirUnsignedInt] = None,
        max: Optional[FhirString] = None,
        base: Optional[ElementDefinitionBase] = None,
        contentReference: Optional[FhirUri] = None,
        type_: Optional[FhirList[ElementDefinitionType]] = None,
        defaultValueBase64Binary: Optional[FhirBase64Binary] = None,
        defaultValueBoolean: Optional[FhirBoolean] = None,
        defaultValueCanonical: Optional[FhirCanonical] = None,
        defaultValueCode: Optional[GenericTypeCode] = None,
        defaultValueDate: Optional[FhirDate] = None,
        defaultValueDateTime: Optional[FhirDateTime] = None,
        defaultValueDecimal: Optional[FhirDecimal] = None,
        defaultValueId: Optional[FhirId] = None,
        defaultValueInstant: Optional[FhirInstant] = None,
        defaultValueInteger: Optional[FhirInteger] = None,
        defaultValueMarkdown: Optional[FhirMarkdown] = None,
        defaultValueOid: Optional[FhirOid] = None,
        defaultValuePositiveInt: Optional[FhirPositiveInt] = None,
        defaultValueString: Optional[FhirString] = None,
        defaultValueTime: Optional[FhirTime] = None,
        defaultValueUnsignedInt: Optional[FhirUnsignedInt] = None,
        defaultValueUri: Optional[FhirUri] = None,
        defaultValueUrl: Optional[FhirUrl] = None,
        defaultValueUuid: Optional[FhirUuid] = None,
        defaultValueAddress: Optional[Address] = None,
        defaultValueAge: Optional[Age] = None,
        defaultValueAnnotation: Optional[Annotation] = None,
        defaultValueAttachment: Optional[Attachment] = None,
        defaultValueCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        defaultValueCoding: Optional[Coding[GenericTypeCode]] = None,
        defaultValueContactPoint: Optional[ContactPoint] = None,
        defaultValueCount: Optional[Count] = None,
        defaultValueDistance: Optional[Distance] = None,
        defaultValueDuration: Optional[Duration] = None,
        defaultValueHumanName: Optional[HumanName] = None,
        defaultValueIdentifier: Optional[Identifier] = None,
        defaultValueMoney: Optional[Money] = None,
        defaultValuePeriod: Optional[Period] = None,
        defaultValueQuantity: Optional[Quantity] = None,
        defaultValueRange: Optional[Range] = None,
        defaultValueRatio: Optional[Ratio] = None,
        defaultValueReference: Optional[Reference[Resource]] = None,
        defaultValueSampledData: Optional[SampledData] = None,
        defaultValueSignature: Optional[Signature] = None,
        defaultValueTiming: Optional[Timing] = None,
        defaultValueContactDetail: Optional[ContactDetail] = None,
        defaultValueContributor: Optional[Contributor] = None,
        defaultValueDataRequirement: Optional[DataRequirement] = None,
        defaultValueExpression: Optional[Expression] = None,
        defaultValueParameterDefinition: Optional[ParameterDefinition] = None,
        defaultValueRelatedArtifact: Optional[RelatedArtifact] = None,
        defaultValueTriggerDefinition: Optional[TriggerDefinition] = None,
        defaultValueUsageContext: Optional[UsageContext] = None,
        defaultValueDosage: Optional[Dosage] = None,
        defaultValueMeta: Optional[Meta] = None,
        meaningWhenMissing: Optional[FhirMarkdown] = None,
        orderMeaning: Optional[FhirString] = None,
        fixedBase64Binary: Optional[FhirBase64Binary] = None,
        fixedBoolean: Optional[FhirBoolean] = None,
        fixedCanonical: Optional[FhirCanonical] = None,
        fixedCode: Optional[GenericTypeCode] = None,
        fixedDate: Optional[FhirDate] = None,
        fixedDateTime: Optional[FhirDateTime] = None,
        fixedDecimal: Optional[FhirDecimal] = None,
        fixedId: Optional[FhirId] = None,
        fixedInstant: Optional[FhirInstant] = None,
        fixedInteger: Optional[FhirInteger] = None,
        fixedMarkdown: Optional[FhirMarkdown] = None,
        fixedOid: Optional[FhirOid] = None,
        fixedPositiveInt: Optional[FhirPositiveInt] = None,
        fixedString: Optional[FhirString] = None,
        fixedTime: Optional[FhirTime] = None,
        fixedUnsignedInt: Optional[FhirUnsignedInt] = None,
        fixedUri: Optional[FhirUri] = None,
        fixedUrl: Optional[FhirUrl] = None,
        fixedUuid: Optional[FhirUuid] = None,
        fixedAddress: Optional[Address] = None,
        fixedAge: Optional[Age] = None,
        fixedAnnotation: Optional[Annotation] = None,
        fixedAttachment: Optional[Attachment] = None,
        fixedCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        fixedCoding: Optional[Coding[GenericTypeCode]] = None,
        fixedContactPoint: Optional[ContactPoint] = None,
        fixedCount: Optional[Count] = None,
        fixedDistance: Optional[Distance] = None,
        fixedDuration: Optional[Duration] = None,
        fixedHumanName: Optional[HumanName] = None,
        fixedIdentifier: Optional[Identifier] = None,
        fixedMoney: Optional[Money] = None,
        fixedPeriod: Optional[Period] = None,
        fixedQuantity: Optional[Quantity] = None,
        fixedRange: Optional[Range] = None,
        fixedRatio: Optional[Ratio] = None,
        fixedReference: Optional[Reference[Resource]] = None,
        fixedSampledData: Optional[SampledData] = None,
        fixedSignature: Optional[Signature] = None,
        fixedTiming: Optional[Timing] = None,
        fixedContactDetail: Optional[ContactDetail] = None,
        fixedContributor: Optional[Contributor] = None,
        fixedDataRequirement: Optional[DataRequirement] = None,
        fixedExpression: Optional[Expression] = None,
        fixedParameterDefinition: Optional[ParameterDefinition] = None,
        fixedRelatedArtifact: Optional[RelatedArtifact] = None,
        fixedTriggerDefinition: Optional[TriggerDefinition] = None,
        fixedUsageContext: Optional[UsageContext] = None,
        fixedDosage: Optional[Dosage] = None,
        fixedMeta: Optional[Meta] = None,
        patternBase64Binary: Optional[FhirBase64Binary] = None,
        patternBoolean: Optional[FhirBoolean] = None,
        patternCanonical: Optional[FhirCanonical] = None,
        patternCode: Optional[GenericTypeCode] = None,
        patternDate: Optional[FhirDate] = None,
        patternDateTime: Optional[FhirDateTime] = None,
        patternDecimal: Optional[FhirDecimal] = None,
        patternId: Optional[FhirId] = None,
        patternInstant: Optional[FhirInstant] = None,
        patternInteger: Optional[FhirInteger] = None,
        patternMarkdown: Optional[FhirMarkdown] = None,
        patternOid: Optional[FhirOid] = None,
        patternPositiveInt: Optional[FhirPositiveInt] = None,
        patternString: Optional[FhirString] = None,
        patternTime: Optional[FhirTime] = None,
        patternUnsignedInt: Optional[FhirUnsignedInt] = None,
        patternUri: Optional[FhirUri] = None,
        patternUrl: Optional[FhirUrl] = None,
        patternUuid: Optional[FhirUuid] = None,
        patternAddress: Optional[Address] = None,
        patternAge: Optional[Age] = None,
        patternAnnotation: Optional[Annotation] = None,
        patternAttachment: Optional[Attachment] = None,
        patternCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        patternCoding: Optional[Coding[GenericTypeCode]] = None,
        patternContactPoint: Optional[ContactPoint] = None,
        patternCount: Optional[Count] = None,
        patternDistance: Optional[Distance] = None,
        patternDuration: Optional[Duration] = None,
        patternHumanName: Optional[HumanName] = None,
        patternIdentifier: Optional[Identifier] = None,
        patternMoney: Optional[Money] = None,
        patternPeriod: Optional[Period] = None,
        patternQuantity: Optional[Quantity] = None,
        patternRange: Optional[Range] = None,
        patternRatio: Optional[Ratio] = None,
        patternReference: Optional[Reference[Resource]] = None,
        patternSampledData: Optional[SampledData] = None,
        patternSignature: Optional[Signature] = None,
        patternTiming: Optional[Timing] = None,
        patternContactDetail: Optional[ContactDetail] = None,
        patternContributor: Optional[Contributor] = None,
        patternDataRequirement: Optional[DataRequirement] = None,
        patternExpression: Optional[Expression] = None,
        patternParameterDefinition: Optional[ParameterDefinition] = None,
        patternRelatedArtifact: Optional[RelatedArtifact] = None,
        patternTriggerDefinition: Optional[TriggerDefinition] = None,
        patternUsageContext: Optional[UsageContext] = None,
        patternDosage: Optional[Dosage] = None,
        patternMeta: Optional[Meta] = None,
        example: Optional[FhirList[ElementDefinitionExample]] = None,
        minValueDate: Optional[FhirDate] = None,
        minValueDateTime: Optional[FhirDateTime] = None,
        minValueInstant: Optional[FhirInstant] = None,
        minValueTime: Optional[FhirTime] = None,
        minValueDecimal: Optional[FhirDecimal] = None,
        minValueInteger: Optional[FhirInteger] = None,
        minValuePositiveInt: Optional[FhirPositiveInt] = None,
        minValueUnsignedInt: Optional[FhirUnsignedInt] = None,
        minValueQuantity: Optional[Quantity] = None,
        maxValueDate: Optional[FhirDate] = None,
        maxValueDateTime: Optional[FhirDateTime] = None,
        maxValueInstant: Optional[FhirInstant] = None,
        maxValueTime: Optional[FhirTime] = None,
        maxValueDecimal: Optional[FhirDecimal] = None,
        maxValueInteger: Optional[FhirInteger] = None,
        maxValuePositiveInt: Optional[FhirPositiveInt] = None,
        maxValueUnsignedInt: Optional[FhirUnsignedInt] = None,
        maxValueQuantity: Optional[Quantity] = None,
        maxLength: Optional[FhirInteger] = None,
        condition: Optional[FhirList[FhirId]] = None,
        constraint: Optional[FhirList[ElementDefinitionConstraint]] = None,
        mustSupport: Optional[FhirBoolean] = None,
        isModifier: Optional[FhirBoolean] = None,
        isModifierReason: Optional[FhirString] = None,
        isSummary: Optional[FhirBoolean] = None,
        binding: Optional[ElementDefinitionBinding] = None,
        mapping: Optional[FhirList[ElementDefinitionMapping]] = None,
    ) -> None:
        """
            Captures constraints on each element within the resource, profile, or
        extension.
            If the element is present, it must have a value for at least one of the
        defined elements, an @id referenced from the Narrative, or extensions

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param path: The path identifies the element and is expressed as a "."-separated list of
        ancestor elements, beginning with the name of the resource or extension.
            :param representation: Codes that define how this element is represented in instances, when the
        deviation varies from the normal case.
            :param sliceName: The name of this element definition slice, when slicing is working. The name
        must be a token with no dots or spaces. This is a unique name referring to a
        specific set of constraints applied to this element, used to provide a name to
        different slices of the same element.
            :param sliceIsConstraining: If true, indicates that this slice definition is constraining a slice
        definition with the same name in an inherited profile. If false, the slice is
        not overriding any slice in an inherited profile. If missing, the slice might
        or might not be overriding a slice in an inherited profile, depending on the
        sliceName.
            :param label: A single preferred label which is the text to display beside the element
        indicating its meaning or to use to prompt for the element in a user display
        or form.
            :param code: A code that has the same meaning as the element in a particular terminology.
            :param slicing: Indicates that the element is sliced into a set of alternative definitions
        (i.e. in a structure definition, there are multiple different constraints on a
        single element in the base resource). Slicing can be used in any resource that
        has cardinality ..* on the base resource, or any resource with a choice of
        types. The set of slices is any elements that come after this in the element
        sequence that have the same path, until a shorter path occurs (the shorter
        path terminates the set).
            :param short: A concise description of what this element means (e.g. for use in
        autogenerated summaries).
            :param definition: Provides a complete explanation of the meaning of the data element for human
        readability.  For the case of elements derived from existing elements (e.g.
        constraints), the definition SHALL be consistent with the base definition, but
        convey the meaning of the element in the particular context of use of the
        resource. (Note: The text you are reading is specified in
        ElementDefinition.definition).
            :param comment: Explanatory notes and implementation guidance about the data element,
        including notes about how to use the data properly, exceptions to proper use,
        etc. (Note: The text you are reading is specified in
        ElementDefinition.comment).
            :param requirements: This element is for traceability of why the element was created and why the
        constraints exist as they do. This may be used to point to source materials or
        specifications that drove the structure of this element.
            :param alias: Identifies additional names by which this element might also be known.
            :param min: The minimum number of times this element SHALL appear in the instance.
            :param max: The maximum number of times this element is permitted to appear in the
        instance.
            :param base: Information about the base definition of the element, provided to make it
        unnecessary for tools to trace the deviation of the element through the
        derived and related profiles. When the element definition is not the original
        definition of an element - i.g. either in a constraint on another type, or for
        elements from a super type in a snap shot - then the information in provided
        in the element definition may be different to the base definition. On the
        original definition of the element, it will be same.
            :param contentReference: Identifies an element defined elsewhere in the definition whose content rules
        should be applied to the current element. ContentReferences bring across all
        the rules that are in the ElementDefinition for the element, including
        definitions, cardinality constraints, bindings, invariants etc.
            :param type_: The data type or resource that the value of this element is permitted to be.
            :param defaultValueBase64Binary: None
            :param defaultValueBoolean: None
            :param defaultValueCanonical: None
            :param defaultValueCode: None
            :param defaultValueDate: None
            :param defaultValueDateTime: None
            :param defaultValueDecimal: None
            :param defaultValueId: None
            :param defaultValueInstant: None
            :param defaultValueInteger: None
            :param defaultValueMarkdown: None
            :param defaultValueOid: None
            :param defaultValuePositiveInt: None
            :param defaultValueString: None
            :param defaultValueTime: None
            :param defaultValueUnsignedInt: None
            :param defaultValueUri: None
            :param defaultValueUrl: None
            :param defaultValueUuid: None
            :param defaultValueAddress: None
            :param defaultValueAge: None
            :param defaultValueAnnotation: None
            :param defaultValueAttachment: None
            :param defaultValueCodeableConcept: None
            :param defaultValueCoding: None
            :param defaultValueContactPoint: None
            :param defaultValueCount: None
            :param defaultValueDistance: None
            :param defaultValueDuration: None
            :param defaultValueHumanName: None
            :param defaultValueIdentifier: None
            :param defaultValueMoney: None
            :param defaultValuePeriod: None
            :param defaultValueQuantity: None
            :param defaultValueRange: None
            :param defaultValueRatio: None
            :param defaultValueReference: None
            :param defaultValueSampledData: None
            :param defaultValueSignature: None
            :param defaultValueTiming: None
            :param defaultValueContactDetail: None
            :param defaultValueContributor: None
            :param defaultValueDataRequirement: None
            :param defaultValueExpression: None
            :param defaultValueParameterDefinition: None
            :param defaultValueRelatedArtifact: None
            :param defaultValueTriggerDefinition: None
            :param defaultValueUsageContext: None
            :param defaultValueDosage: None
            :param defaultValueMeta: None
            :param meaningWhenMissing: The Implicit meaning that is to be understood when this element is missing
        (e.g. 'when this element is missing, the period is ongoing').
            :param orderMeaning: If present, indicates that the order of the repeating element has meaning and
        describes what that meaning is.  If absent, it means that the order of the
        element has no meaning.
            :param fixedBase64Binary: None
            :param fixedBoolean: None
            :param fixedCanonical: None
            :param fixedCode: None
            :param fixedDate: None
            :param fixedDateTime: None
            :param fixedDecimal: None
            :param fixedId: None
            :param fixedInstant: None
            :param fixedInteger: None
            :param fixedMarkdown: None
            :param fixedOid: None
            :param fixedPositiveInt: None
            :param fixedString: None
            :param fixedTime: None
            :param fixedUnsignedInt: None
            :param fixedUri: None
            :param fixedUrl: None
            :param fixedUuid: None
            :param fixedAddress: None
            :param fixedAge: None
            :param fixedAnnotation: None
            :param fixedAttachment: None
            :param fixedCodeableConcept: None
            :param fixedCoding: None
            :param fixedContactPoint: None
            :param fixedCount: None
            :param fixedDistance: None
            :param fixedDuration: None
            :param fixedHumanName: None
            :param fixedIdentifier: None
            :param fixedMoney: None
            :param fixedPeriod: None
            :param fixedQuantity: None
            :param fixedRange: None
            :param fixedRatio: None
            :param fixedReference: None
            :param fixedSampledData: None
            :param fixedSignature: None
            :param fixedTiming: None
            :param fixedContactDetail: None
            :param fixedContributor: None
            :param fixedDataRequirement: None
            :param fixedExpression: None
            :param fixedParameterDefinition: None
            :param fixedRelatedArtifact: None
            :param fixedTriggerDefinition: None
            :param fixedUsageContext: None
            :param fixedDosage: None
            :param fixedMeta: None
            :param patternBase64Binary: None
            :param patternBoolean: None
            :param patternCanonical: None
            :param patternCode: None
            :param patternDate: None
            :param patternDateTime: None
            :param patternDecimal: None
            :param patternId: None
            :param patternInstant: None
            :param patternInteger: None
            :param patternMarkdown: None
            :param patternOid: None
            :param patternPositiveInt: None
            :param patternString: None
            :param patternTime: None
            :param patternUnsignedInt: None
            :param patternUri: None
            :param patternUrl: None
            :param patternUuid: None
            :param patternAddress: None
            :param patternAge: None
            :param patternAnnotation: None
            :param patternAttachment: None
            :param patternCodeableConcept: None
            :param patternCoding: None
            :param patternContactPoint: None
            :param patternCount: None
            :param patternDistance: None
            :param patternDuration: None
            :param patternHumanName: None
            :param patternIdentifier: None
            :param patternMoney: None
            :param patternPeriod: None
            :param patternQuantity: None
            :param patternRange: None
            :param patternRatio: None
            :param patternReference: None
            :param patternSampledData: None
            :param patternSignature: None
            :param patternTiming: None
            :param patternContactDetail: None
            :param patternContributor: None
            :param patternDataRequirement: None
            :param patternExpression: None
            :param patternParameterDefinition: None
            :param patternRelatedArtifact: None
            :param patternTriggerDefinition: None
            :param patternUsageContext: None
            :param patternDosage: None
            :param patternMeta: None
            :param example: A sample value for this element demonstrating the type of information that
        would typically be found in the element.
            :param minValueDate: None
            :param minValueDateTime: None
            :param minValueInstant: None
            :param minValueTime: None
            :param minValueDecimal: None
            :param minValueInteger: None
            :param minValuePositiveInt: None
            :param minValueUnsignedInt: None
            :param minValueQuantity: None
            :param maxValueDate: None
            :param maxValueDateTime: None
            :param maxValueInstant: None
            :param maxValueTime: None
            :param maxValueDecimal: None
            :param maxValueInteger: None
            :param maxValuePositiveInt: None
            :param maxValueUnsignedInt: None
            :param maxValueQuantity: None
            :param maxLength: Indicates the maximum length in characters that is permitted to be present in
        conformant instances and which is expected to be supported by conformant
        consumers that support the element.
            :param condition: A reference to an invariant that may make additional statements about the
        cardinality or value in the instance.
            :param constraint: Formal constraints such as co-occurrence and other constraints that can be
        computationally evaluated within the context of the instance.
            :param mustSupport: If true, implementations that produce or consume resources SHALL provide
        "support" for the element in some meaningful way.  If false, the element may
        be ignored and not supported. If false, whether to populate or use the data
        element in any way is at the discretion of the implementation.
            :param isModifier: If true, the value of this element affects the interpretation of the element
        or resource that contains it, and the value of the element cannot be ignored.
        Typically, this is used for status, negation and qualification codes. The
        effect of this is that the element cannot be ignored by systems: they SHALL
        either recognize the element and process it, and/or a pre-determination has
        been made that it is not relevant to their particular system.
            :param isModifierReason: Explains how that element affects the interpretation of the resource or
        element that contains it.
            :param isSummary: Whether the element should be included if a client requests a search with the
        parameter _summary=true.
            :param binding: Binds to a value set if this element is coded (code, Coding, CodeableConcept,
        Quantity), or the data types (string, uri).
            :param mapping: Identifies a concept from an external specification that roughly corresponds
        to this element.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            path=path,
            representation=representation,
            sliceName=sliceName,
            sliceIsConstraining=sliceIsConstraining,
            label=label,
            code=code,
            slicing=slicing,
            short=short,
            definition=definition,
            comment=comment,
            requirements=requirements,
            alias=alias,
            min=min,
            max=max,
            base=base,
            contentReference=contentReference,
            type_=type_,
            defaultValueBase64Binary=defaultValueBase64Binary,
            defaultValueBoolean=defaultValueBoolean,
            defaultValueCanonical=defaultValueCanonical,
            defaultValueCode=defaultValueCode,
            defaultValueDate=defaultValueDate,
            defaultValueDateTime=defaultValueDateTime,
            defaultValueDecimal=defaultValueDecimal,
            defaultValueId=defaultValueId,
            defaultValueInstant=defaultValueInstant,
            defaultValueInteger=defaultValueInteger,
            defaultValueMarkdown=defaultValueMarkdown,
            defaultValueOid=defaultValueOid,
            defaultValuePositiveInt=defaultValuePositiveInt,
            defaultValueString=defaultValueString,
            defaultValueTime=defaultValueTime,
            defaultValueUnsignedInt=defaultValueUnsignedInt,
            defaultValueUri=defaultValueUri,
            defaultValueUrl=defaultValueUrl,
            defaultValueUuid=defaultValueUuid,
            defaultValueAddress=defaultValueAddress,
            defaultValueAge=defaultValueAge,
            defaultValueAnnotation=defaultValueAnnotation,
            defaultValueAttachment=defaultValueAttachment,
            defaultValueCodeableConcept=defaultValueCodeableConcept,
            defaultValueCoding=defaultValueCoding,
            defaultValueContactPoint=defaultValueContactPoint,
            defaultValueCount=defaultValueCount,
            defaultValueDistance=defaultValueDistance,
            defaultValueDuration=defaultValueDuration,
            defaultValueHumanName=defaultValueHumanName,
            defaultValueIdentifier=defaultValueIdentifier,
            defaultValueMoney=defaultValueMoney,
            defaultValuePeriod=defaultValuePeriod,
            defaultValueQuantity=defaultValueQuantity,
            defaultValueRange=defaultValueRange,
            defaultValueRatio=defaultValueRatio,
            defaultValueReference=defaultValueReference,
            defaultValueSampledData=defaultValueSampledData,
            defaultValueSignature=defaultValueSignature,
            defaultValueTiming=defaultValueTiming,
            defaultValueContactDetail=defaultValueContactDetail,
            defaultValueContributor=defaultValueContributor,
            defaultValueDataRequirement=defaultValueDataRequirement,
            defaultValueExpression=defaultValueExpression,
            defaultValueParameterDefinition=defaultValueParameterDefinition,
            defaultValueRelatedArtifact=defaultValueRelatedArtifact,
            defaultValueTriggerDefinition=defaultValueTriggerDefinition,
            defaultValueUsageContext=defaultValueUsageContext,
            defaultValueDosage=defaultValueDosage,
            defaultValueMeta=defaultValueMeta,
            meaningWhenMissing=meaningWhenMissing,
            orderMeaning=orderMeaning,
            fixedBase64Binary=fixedBase64Binary,
            fixedBoolean=fixedBoolean,
            fixedCanonical=fixedCanonical,
            fixedCode=fixedCode,
            fixedDate=fixedDate,
            fixedDateTime=fixedDateTime,
            fixedDecimal=fixedDecimal,
            fixedId=fixedId,
            fixedInstant=fixedInstant,
            fixedInteger=fixedInteger,
            fixedMarkdown=fixedMarkdown,
            fixedOid=fixedOid,
            fixedPositiveInt=fixedPositiveInt,
            fixedString=fixedString,
            fixedTime=fixedTime,
            fixedUnsignedInt=fixedUnsignedInt,
            fixedUri=fixedUri,
            fixedUrl=fixedUrl,
            fixedUuid=fixedUuid,
            fixedAddress=fixedAddress,
            fixedAge=fixedAge,
            fixedAnnotation=fixedAnnotation,
            fixedAttachment=fixedAttachment,
            fixedCodeableConcept=fixedCodeableConcept,
            fixedCoding=fixedCoding,
            fixedContactPoint=fixedContactPoint,
            fixedCount=fixedCount,
            fixedDistance=fixedDistance,
            fixedDuration=fixedDuration,
            fixedHumanName=fixedHumanName,
            fixedIdentifier=fixedIdentifier,
            fixedMoney=fixedMoney,
            fixedPeriod=fixedPeriod,
            fixedQuantity=fixedQuantity,
            fixedRange=fixedRange,
            fixedRatio=fixedRatio,
            fixedReference=fixedReference,
            fixedSampledData=fixedSampledData,
            fixedSignature=fixedSignature,
            fixedTiming=fixedTiming,
            fixedContactDetail=fixedContactDetail,
            fixedContributor=fixedContributor,
            fixedDataRequirement=fixedDataRequirement,
            fixedExpression=fixedExpression,
            fixedParameterDefinition=fixedParameterDefinition,
            fixedRelatedArtifact=fixedRelatedArtifact,
            fixedTriggerDefinition=fixedTriggerDefinition,
            fixedUsageContext=fixedUsageContext,
            fixedDosage=fixedDosage,
            fixedMeta=fixedMeta,
            patternBase64Binary=patternBase64Binary,
            patternBoolean=patternBoolean,
            patternCanonical=patternCanonical,
            patternCode=patternCode,
            patternDate=patternDate,
            patternDateTime=patternDateTime,
            patternDecimal=patternDecimal,
            patternId=patternId,
            patternInstant=patternInstant,
            patternInteger=patternInteger,
            patternMarkdown=patternMarkdown,
            patternOid=patternOid,
            patternPositiveInt=patternPositiveInt,
            patternString=patternString,
            patternTime=patternTime,
            patternUnsignedInt=patternUnsignedInt,
            patternUri=patternUri,
            patternUrl=patternUrl,
            patternUuid=patternUuid,
            patternAddress=patternAddress,
            patternAge=patternAge,
            patternAnnotation=patternAnnotation,
            patternAttachment=patternAttachment,
            patternCodeableConcept=patternCodeableConcept,
            patternCoding=patternCoding,
            patternContactPoint=patternContactPoint,
            patternCount=patternCount,
            patternDistance=patternDistance,
            patternDuration=patternDuration,
            patternHumanName=patternHumanName,
            patternIdentifier=patternIdentifier,
            patternMoney=patternMoney,
            patternPeriod=patternPeriod,
            patternQuantity=patternQuantity,
            patternRange=patternRange,
            patternRatio=patternRatio,
            patternReference=patternReference,
            patternSampledData=patternSampledData,
            patternSignature=patternSignature,
            patternTiming=patternTiming,
            patternContactDetail=patternContactDetail,
            patternContributor=patternContributor,
            patternDataRequirement=patternDataRequirement,
            patternExpression=patternExpression,
            patternParameterDefinition=patternParameterDefinition,
            patternRelatedArtifact=patternRelatedArtifact,
            patternTriggerDefinition=patternTriggerDefinition,
            patternUsageContext=patternUsageContext,
            patternDosage=patternDosage,
            patternMeta=patternMeta,
            example=example,
            minValueDate=minValueDate,
            minValueDateTime=minValueDateTime,
            minValueInstant=minValueInstant,
            minValueTime=minValueTime,
            minValueDecimal=minValueDecimal,
            minValueInteger=minValueInteger,
            minValuePositiveInt=minValuePositiveInt,
            minValueUnsignedInt=minValueUnsignedInt,
            minValueQuantity=minValueQuantity,
            maxValueDate=maxValueDate,
            maxValueDateTime=maxValueDateTime,
            maxValueInstant=maxValueInstant,
            maxValueTime=maxValueTime,
            maxValueDecimal=maxValueDecimal,
            maxValueInteger=maxValueInteger,
            maxValuePositiveInt=maxValuePositiveInt,
            maxValueUnsignedInt=maxValueUnsignedInt,
            maxValueQuantity=maxValueQuantity,
            maxLength=maxLength,
            condition=condition,
            constraint=constraint,
            mustSupport=mustSupport,
            isModifier=isModifier,
            isModifierReason=isModifierReason,
            isSummary=isSummary,
            binding=binding,
            mapping=mapping,
        )
