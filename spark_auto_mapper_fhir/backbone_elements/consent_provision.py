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
    from spark_auto_mapper_fhir.complex_types.consent_provision_type import (
        ConsentProvisionType,
    )
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.backbone_elements.consent_actor import ConsentActor
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.coding import Coding
    from spark_auto_mapper_fhir.complex_types.coding import Coding
    from spark_auto_mapper_fhir.complex_types.coding import Coding
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept
    from spark_auto_mapper_fhir.complex_types.period import Period
    from spark_auto_mapper_fhir.backbone_elements.consent_data import ConsentData
    from spark_auto_mapper_fhir.backbone_elements.consent_provision import (
        ConsentProvision,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ConsentProvision(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type: Optional[ConsentProvisionType] = None,
        period: Optional[Period] = None,
        actor: Optional[FhirList[ConsentActor]] = None,
        action: Optional[FhirList[CodeableConcept]] = None,
        securityLabel: Optional[FhirList[Coding]] = None,
        purpose: Optional[FhirList[Coding]] = None,
        class_: Optional[FhirList[Coding]] = None,
        code: Optional[FhirList[CodeableConcept]] = None,
        dataPeriod: Optional[Period] = None,
        data: Optional[FhirList[ConsentData]] = None,
        provision: Optional[FhirList[ConsentProvision]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param type: Action  to take - permit or deny - when the rule conditions are met.  Not
        permitted in root rule, required in all nested rules.
            :param period: The timeframe in this rule is valid.
            :param actor: Who or what is controlled by this rule. Use group to identify a set of actors
        by some property they share (e.g. 'admitting officers').
            :param action: Actions controlled by this Rule.
            :param securityLabel: A security label, comprised of 0..* security label fields (Privacy tags),
        which define which resources are controlled by this exception.
            :param purpose: The context of the activities a user is taking - why the user is accessing the
        data - that are controlled by this rule.
            :param class_: The class of information covered by this rule. The type can be a FHIR resource
        type, a profile on a type, or a CDA document, or some other type that
        indicates what sort of information the consent relates to.
            :param code: If this code is found in an instance, then the rule applies.
            :param dataPeriod: Clinical or Operational Relevant period of time that bounds the data
        controlled by this rule.
            :param data: The resources controlled by this rule if specific resources are referenced.
            :param provision: Rules which provide exceptions to the base rule or subrules.
        """
        super().__init__(
            resourceType="ConsentProvision",
            id_=id_,
            meta=meta,
            extension=extension,
            type=type,
            period=period,
            actor=actor,
            action=action,
            securityLabel=securityLabel,
            purpose=purpose,
            class_=class_,
            code=code,
            dataPeriod=dataPeriod,
            data=data,
            provision=provision,
        )