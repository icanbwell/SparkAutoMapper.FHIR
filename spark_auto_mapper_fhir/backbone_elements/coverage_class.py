from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.coverage_class_codes import (
        CoverageClassCodesCode,
    )

    # End Import for CodeableConcept for type_
    # value (string)
    # name (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CoverageClass(FhirBackboneElementBase):
    """
    Coverage.Class
        Financial instrument which may be used to reimburse or pay for health care products and services. Includes both insurance and self-payment.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        type_: CodeableConcept[CoverageClassCodesCode],
        value: FhirString,
        name: Optional[FhirString] = None,
    ) -> None:
        """
            Financial instrument which may be used to reimburse or pay for health care
        products and services. Includes both insurance and self-payment.

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
            :param type_: The type of classification for which an insurer-specific class label or number
        and optional name is provided, for example may be used to identify a class of
        coverage or employer group, Policy, Plan.
            :param value: The alphanumeric string value associated with the insurer issued label.
            :param name: A short description for the class.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            type_=type_,
            value=value,
            name=name,
        )
