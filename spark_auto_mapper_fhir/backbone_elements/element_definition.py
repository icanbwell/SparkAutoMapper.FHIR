from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.property_representation import (
        PropertyRepresentation,
    )
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.boolean import boolean
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.coding import Coding
    from spark_auto_mapper_fhir.backbone_elements.element_definition_slicing import (
        ElementDefinitionSlicing,
    )
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.markdown import markdown
    from spark_auto_mapper_fhir.complex_types.markdown import markdown
    from spark_auto_mapper_fhir.complex_types.markdown import markdown
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.unsigned_int import unsignedInt
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.backbone_elements.element_definition_base import (
        ElementDefinitionBase,
    )
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.backbone_elements.element_definition_type import (
        ElementDefinitionType,
    )
    from spark_auto_mapper_fhir.complex_types.markdown import markdown
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.backbone_elements.element_definition_example import (
        ElementDefinitionExample,
    )
    from spark_auto_mapper_fhir.complex_types.integer import integer
    from spark_auto_mapper_fhir.complex_types.id import id
    from spark_auto_mapper_fhir.backbone_elements.element_definition_constraint import (
        ElementDefinitionConstraint,
    )
    from spark_auto_mapper_fhir.complex_types.boolean import boolean
    from spark_auto_mapper_fhir.complex_types.boolean import boolean
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.boolean import boolean
    from spark_auto_mapper_fhir.backbone_elements.element_definition_binding import (
        ElementDefinitionBinding,
    )
    from spark_auto_mapper_fhir.backbone_elements.element_definition_mapping import (
        ElementDefinitionMapping,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ElementDefinition(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        path: string,
        representation: Optional[FhirList[PropertyRepresentation]] = None,
        sliceName: Optional[string] = None,
        sliceIsConstraining: Optional[boolean] = None,
        label: Optional[string] = None,
        code: Optional[FhirList[Coding]] = None,
        slicing: Optional[ElementDefinitionSlicing] = None,
        short: Optional[string] = None,
        definition: Optional[markdown] = None,
        comment: Optional[markdown] = None,
        requirements: Optional[markdown] = None,
        alias: Optional[FhirList[string]] = None,
        min: Optional[unsignedInt] = None,
        max: Optional[string] = None,
        base: Optional[ElementDefinitionBase] = None,
        contentReference: Optional[uri] = None,
        type: Optional[FhirList[ElementDefinitionType]] = None,
        meaningWhenMissing: Optional[markdown] = None,
        orderMeaning: Optional[string] = None,
        example: Optional[FhirList[ElementDefinitionExample]] = None,
        maxLength: Optional[integer] = None,
        condition: Optional[FhirList[id]] = None,
        constraint: Optional[FhirList[ElementDefinitionConstraint]] = None,
        mustSupport: Optional[boolean] = None,
        isModifier: Optional[boolean] = None,
        isModifierReason: Optional[string] = None,
        isSummary: Optional[boolean] = None,
        binding: Optional[ElementDefinitionBinding] = None,
        mapping: Optional[FhirList[ElementDefinitionMapping]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
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
            :param type: The data type or resource that the value of this element is permitted to be.
            :param meaningWhenMissing: The Implicit meaning that is to be understood when this element is missing
        (e.g. 'when this element is missing, the period is ongoing').
            :param orderMeaning: If present, indicates that the order of the repeating element has meaning and
        describes what that meaning is.  If absent, it means that the order of the
        element has no meaning.
            :param example: A sample value for this element demonstrating the type of information that
        would typically be found in the element.
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
            resourceType="ElementDefinition",
            id_=id_,
            meta=meta,
            extension=extension,
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
            type=type,
            meaningWhenMissing=meaningWhenMissing,
            orderMeaning=orderMeaning,
            example=example,
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