from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
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
    # language (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for language
    # Import for CodeableConcept for language
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # End Import for CodeableConcept for language
    # preferred (boolean)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class RelatedPersonCommunication(FhirBackboneElementBase):
    """
    RelatedPerson.Communication
        Information about a person that is involved in the care for a patient, but who is not the target of healthcare, nor has a formal responsibility in the care process.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        language: CodeableConcept[CommonLanguagesCode],
        preferred: Optional[FhirBoolean] = None,
    ) -> None:
        """
            Information about a person that is involved in the care for a patient, but who
        is not the target of healthcare, nor has a formal responsibility in the care
        process.

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
            :param language: The ISO-639-1 alpha 2 code in lower case for the language, optionally followed
        by a hyphen and the ISO-3166-1 alpha 2 code for the region in upper case; e.g.
        "en" for English, or "en-US" for American English versus "en-EN" for England
        English.
            :param preferred: Indicates whether or not the patient prefers this language (over other
        languages he masters up a certain level).
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            language=language,
            preferred=preferred,
        )
