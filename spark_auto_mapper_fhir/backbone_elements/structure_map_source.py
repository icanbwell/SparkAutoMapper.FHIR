from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

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
    # context (id)
    from spark_auto_mapper_fhir.complex_types.id import id

    # min (integer)
    # max (string)
    # type_ (string)
    # element (string)
    # listMode (StructureMapSourceListMode)
    from spark_auto_mapper_fhir.value_sets.structure_map_source_list_mode import (
        StructureMapSourceListModeCode,
    )

    # variable (id)
    # condition (string)
    # check (string)
    # logMessage (string)
    # defaultValueBase64Binary (base64Binary)
    from spark_auto_mapper_fhir.complex_types.base64_binary import base64Binary

    # defaultValueBoolean (boolean)
    # defaultValueCanonical (canonical)
    from spark_auto_mapper_fhir.fhir_types.canonical import FhirCanonical

    # defaultValueCode (code)
    from spark_auto_mapper_fhir.complex_types.code import code

    # defaultValueDate (date)
    # defaultValueDateTime (dateTime)
    # defaultValueDecimal (decimal)
    from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

    # defaultValueId (id)
    # defaultValueInstant (instant)
    from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant

    # defaultValueInteger (integer)
    # defaultValueMarkdown (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # defaultValueOid (oid)
    from spark_auto_mapper_fhir.complex_types.oid import oid

    # defaultValuePositiveInt (positiveInt)
    from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

    # defaultValueString (string)
    # defaultValueTime (time)
    from spark_auto_mapper_fhir.fhir_types.time import FhirTime

    # defaultValueUnsignedInt (unsignedInt)
    from spark_auto_mapper_fhir.complex_types.unsigned_int import unsignedInt

    # defaultValueUri (uri)
    # defaultValueUrl (url)
    from spark_auto_mapper_fhir.complex_types.url import url

    # defaultValueUuid (uuid)
    from spark_auto_mapper_fhir.complex_types.uuid import uuid

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
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for defaultValueCodeableConcept
    # defaultValueCoding (Coding)
    from spark_auto_mapper_fhir.complex_types.coding import Coding

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


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class StructureMapSource(FhirBackboneElementBase):
    """
    StructureMap.Source
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        context: id,
        min: Optional[FhirInteger] = None,
        max: Optional[FhirString] = None,
        type_: Optional[FhirString] = None,
        element: Optional[FhirString] = None,
        listMode: Optional[StructureMapSourceListModeCode] = None,
        variable: Optional[id] = None,
        condition: Optional[FhirString] = None,
        check: Optional[FhirString] = None,
        logMessage: Optional[FhirString] = None,
        defaultValueBase64Binary: Optional[base64Binary] = None,
        defaultValueBoolean: Optional[FhirBoolean] = None,
        defaultValueCanonical: Optional[FhirCanonical] = None,
        defaultValueCode: Optional[code] = None,
        defaultValueDate: Optional[FhirDate] = None,
        defaultValueDateTime: Optional[FhirDateTime] = None,
        defaultValueDecimal: Optional[FhirDecimal] = None,
        defaultValueId: Optional[id] = None,
        defaultValueInstant: Optional[FhirInstant] = None,
        defaultValueInteger: Optional[FhirInteger] = None,
        defaultValueMarkdown: Optional[FhirMarkdown] = None,
        defaultValueOid: Optional[oid] = None,
        defaultValuePositiveInt: Optional[FhirPositiveInt] = None,
        defaultValueString: Optional[FhirString] = None,
        defaultValueTime: Optional[FhirTime] = None,
        defaultValueUnsignedInt: Optional[unsignedInt] = None,
        defaultValueUri: Optional[FhirUri] = None,
        defaultValueUrl: Optional[url] = None,
        defaultValueUuid: Optional[uuid] = None,
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
        defaultValueReference: Optional[Reference[Union[Resource]]] = None,
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
    ) -> None:
        """

            :param id_: id of resource
            :param extension: extensions
            :param context: Type or variable this rule applies to.
            :param min: Specified minimum cardinality for the element. This is optional; if present,
        it acts an implicit check on the input content.
            :param max: Specified maximum cardinality for the element - a number or a "*". This is
        optional; if present, it acts an implicit check on the input content (* just
        serves as documentation; it's the default value).
            :param type_: Specified type for the element. This works as a condition on the mapping - use
        for polymorphic elements.
            :param element: Optional field for this source.
            :param listMode: How to handle the list mode for this element.
            :param variable: Named context for field, if a field is specified.
            :param condition: FHIRPath expression  - must be true or the rule does not apply.
            :param check: FHIRPath expression  - must be true or the mapping engine throws an error
        instead of completing.
            :param logMessage: A FHIRPath expression which specifies a message to put in the transform log
        when content matching the source rule is found.
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
        """
        super().__init__(
            id_=id_,
            extension=extension,
            context=context,
            min=min,
            max=max,
            type_=type_,
            element=element,
            listMode=listMode,
            variable=variable,
            condition=condition,
            check=check,
            logMessage=logMessage,
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
        )
