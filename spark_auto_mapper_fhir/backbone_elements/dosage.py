from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.integer import FhirInteger
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
    # sequence (integer)
    # text (string)
    # additionalInstruction (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # End Import for References for additionalInstruction
    # Import for CodeableConcept for additionalInstruction
    from spark_auto_mapper_fhir.value_sets.snomedct_additional_dosage_instructions import (
        SNOMEDCTAdditionalDosageInstructionsCode,
    )

    # End Import for CodeableConcept for additionalInstruction
    # patientInstruction (string)
    # timing (Timing)
    from spark_auto_mapper_fhir.backbone_elements.timing import Timing

    # asNeededBoolean (boolean)
    # asNeededCodeableConcept (CodeableConcept)
    # End Import for References for asNeededCodeableConcept
    # Import for CodeableConcept for asNeededCodeableConcept
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for asNeededCodeableConcept
    # site (CodeableConcept)
    # End Import for References for site
    # Import for CodeableConcept for site
    from spark_auto_mapper_fhir.value_sets.snomedct_anatomical_structure_for_administration_site_codes import (
        SNOMEDCTAnatomicalStructureForAdministrationSiteCodesCode,
    )

    # End Import for CodeableConcept for site
    # route (CodeableConcept)
    # End Import for References for route
    # Import for CodeableConcept for route
    from spark_auto_mapper_fhir.value_sets.snomedct_route_codes import (
        SNOMEDCTRouteCodesCode,
    )

    # End Import for CodeableConcept for route
    # method (CodeableConcept)
    # End Import for References for method
    # Import for CodeableConcept for method
    from spark_auto_mapper_fhir.value_sets.snomedct_administration_method_codes import (
        SNOMEDCTAdministrationMethodCodesCode,
    )

    # End Import for CodeableConcept for method
    # doseAndRate (Dosage.DoseAndRate)
    from spark_auto_mapper_fhir.backbone_elements.dosage_dose_and_rate import (
        DosageDoseAndRate,
    )

    # maxDosePerPeriod (Ratio)
    from spark_auto_mapper_fhir.complex_types.ratio import Ratio

    # maxDosePerAdministration (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # maxDosePerLifetime (Quantity)


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Dosage(FhirBackboneElementBase):
    """
    Dosage
        Indicates how the medication is/was taken or should be taken by the patient.
        If the element is present, it must have a value for at least one of the defined elements, an @id referenced from the Narrative, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        sequence: Optional[FhirInteger] = None,
        text: Optional[FhirString] = None,
        additionalInstruction: Optional[
            FhirList[CodeableConcept[SNOMEDCTAdditionalDosageInstructionsCode]]
        ] = None,
        patientInstruction: Optional[FhirString] = None,
        timing: Optional[Timing] = None,
        asNeededBoolean: Optional[FhirBoolean] = None,
        asNeededCodeableConcept: Optional[CodeableConcept[GenericTypeCode]] = None,
        site: Optional[
            CodeableConcept[SNOMEDCTAnatomicalStructureForAdministrationSiteCodesCode]
        ] = None,
        route: Optional[CodeableConcept[SNOMEDCTRouteCodesCode]] = None,
        method: Optional[CodeableConcept[SNOMEDCTAdministrationMethodCodesCode]] = None,
        doseAndRate: Optional[FhirList[DosageDoseAndRate]] = None,
        maxDosePerPeriod: Optional[Ratio] = None,
        maxDosePerAdministration: Optional[Quantity] = None,
        maxDosePerLifetime: Optional[Quantity] = None,
    ) -> None:
        """
            Indicates how the medication is/was taken or should be taken by the patient.
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
            :param sequence: Indicates the order in which the dosage instructions should be applied or
        interpreted.
            :param text: Free text dosage instructions e.g. SIG.
            :param additionalInstruction: Supplemental instructions to the patient on how to take the medication  (e.g.
        "with meals" or"take half to one hour before food") or warnings for the
        patient about the medication (e.g. "may cause drowsiness" or "avoid exposure
        of skin to direct sunlight or sunlamps").
            :param patientInstruction: Instructions in terms that are understood by the patient or consumer.
            :param timing: When medication should be administered.
            :param asNeededBoolean: None
            :param asNeededCodeableConcept: None
            :param site: Body site to administer to.
            :param route: How drug should enter body.
            :param method: Technique for administering medication.
            :param doseAndRate: The amount of medication administered.
            :param maxDosePerPeriod: Upper limit on medication per unit of time.
            :param maxDosePerAdministration: Upper limit on medication per administration.
            :param maxDosePerLifetime: Upper limit on medication per lifetime of the patient.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            sequence=sequence,
            text=text,
            additionalInstruction=additionalInstruction,
            patientInstruction=patientInstruction,
            timing=timing,
            asNeededBoolean=asNeededBoolean,
            asNeededCodeableConcept=asNeededCodeableConcept,
            site=site,
            route=route,
            method=method,
            doseAndRate=doseAndRate,
            maxDosePerPeriod=maxDosePerPeriod,
            maxDosePerAdministration=maxDosePerAdministration,
            maxDosePerLifetime=maxDosePerLifetime,
        )
