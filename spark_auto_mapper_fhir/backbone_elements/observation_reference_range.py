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
    # low (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # high (Quantity)
    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for type_
    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.observation_reference_range_meaning_codes import (
        ObservationReferenceRangeMeaningCodesCode,
    )

    # End Import for CodeableConcept for type_
    # appliesTo (CodeableConcept)
    # End Import for References for appliesTo
    # Import for CodeableConcept for appliesTo
    from spark_auto_mapper_fhir.value_sets.observation_reference_range_applies_to_codes import (
        ObservationReferenceRangeAppliesToCodesCode,
    )

    # End Import for CodeableConcept for appliesTo
    # age (Range)
    from spark_auto_mapper_fhir.complex_types.range import Range

    # text (string)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ObservationReferenceRange(FhirBackboneElementBase):
    """
    Observation.ReferenceRange
        Measurements and simple assertions made about a patient, device or other subject.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        low: Optional[Quantity] = None,
        high: Optional[Quantity] = None,
        type_: Optional[
            CodeableConcept[ObservationReferenceRangeMeaningCodesCode]
        ] = None,
        appliesTo: Optional[
            FhirList[CodeableConcept[ObservationReferenceRangeAppliesToCodesCode]]
        ] = None,
        age: Optional[Range] = None,
        text: Optional[FhirString] = None,
    ) -> None:
        """
            Measurements and simple assertions made about a patient, device or other
        subject.

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
            :param low: The value of the low bound of the reference range.  The low bound of the
        reference range endpoint is inclusive of the value (e.g.  reference range is
        >=5 - <=9). If the low bound is omitted,  it is assumed to be meaningless
        (e.g. reference range is <=2.3).
            :param high: The value of the high bound of the reference range.  The high bound of the
        reference range endpoint is inclusive of the value (e.g.  reference range is
        >=5 - <=9). If the high bound is omitted,  it is assumed to be meaningless
        (e.g. reference range is >= 2.3).
            :param type_: Codes to indicate the what part of the targeted reference population it
        applies to. For example, the normal or therapeutic range.
            :param appliesTo: Codes to indicate the target population this reference range applies to.  For
        example, a reference range may be based on the normal population or a
        particular sex or race.  Multiple `appliesTo`  are interpreted as an "AND" of
        the target populations.  For example, to represent a target population of
        African American females, both a code of female and a code for African
        American would be used.
            :param age: The age at which this reference range is applicable. This is a neonatal age
        (e.g. number of weeks at term) if the meaning says so.
            :param text: Text based reference range in an observation which may be used when a
        quantitative range is not appropriate for an observation.  An example would be
        a reference value of "Negative" or a list or table of "normals".
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            low=low,
            high=high,
            type_=type_,
            appliesTo=appliesTo,
            age=age,
            text=text,
        )
