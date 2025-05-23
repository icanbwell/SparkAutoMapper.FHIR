from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # identifier (uri)
    # timestamp (dateTime)
    # total (integer)
    # offset (integer)
    # parameter (ValueSet.Parameter)
    from spark_auto_mapper_fhir.backbone_elements.value_set_parameter import (
        ValueSetParameter,
    )

    # contains (ValueSet.Contains)
    from spark_auto_mapper_fhir.backbone_elements.value_set_contains import (
        ValueSetContains,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ValueSetExpansion(FhirBackboneElementBase):
    """
    ValueSet.Expansion
        A ValueSet resource instance specifies a set of codes drawn from one or more code systems, intended for use in a particular context. Value sets link between [[[CodeSystem]]] definitions and their use in [coded elements](terminologies.html).
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirUri] = None,
        timestamp: FhirDateTime,
        total: Optional[FhirInteger] = None,
        offset: Optional[FhirInteger] = None,
        parameter: Optional[FhirList[ValueSetParameter]] = None,
        contains: Optional[FhirList[ValueSetContains]] = None,
    ) -> None:
        """
            A ValueSet resource instance specifies a set of codes drawn from one or more
        code systems, intended for use in a particular context. Value sets link
        between [[[CodeSystem]]] definitions and their use in [coded
        elements](terminologies.html).

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
            :param identifier: An identifier that uniquely identifies this expansion of the valueset, based
        on a unique combination of the provided parameters, the system default
        parameters, and the underlying system code system versions etc. Systems may
        re-use the same identifier as long as those factors remain the same, and the
        expansion is the same, but are not required to do so. This is a business
        identifier.
            :param timestamp: The time at which the expansion was produced by the expanding system.
            :param total: The total number of concepts in the expansion. If the number of concept nodes
        in this resource is less than the stated number, then the server can return
        more using the offset parameter.
            :param offset: If paging is being used, the offset at which this resource starts.  I.e. this
        resource is a partial view into the expansion. If paging is not being used,
        this element SHALL NOT be present.
            :param parameter: A parameter that controlled the expansion process. These parameters may be
        used by users of expanded value sets to check whether the expansion is
        suitable for a particular purpose, or to pick the correct expansion.
            :param contains: The codes that are contained in the value set expansion.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            identifier=identifier,
            timestamp=timestamp,
            total=total,
            offset=offset,
            parameter=parameter,
            contains=contains,
        )
