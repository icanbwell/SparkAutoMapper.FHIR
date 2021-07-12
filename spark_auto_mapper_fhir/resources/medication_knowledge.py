from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.medicationknowledge import (
    MedicationKnowledgeSchema,
)

if TYPE_CHECKING:
    pass
    # id_ (id)
    # meta (Meta)
    # implicitRules (uri)
    # language (CommonLanguages)
    from spark_auto_mapper_fhir.value_sets.common_languages import CommonLanguagesCode

    # text (Narrative)
    from spark_auto_mapper_fhir.complex_types.narrative import Narrative

    # contained (ResourceContainer)
    from spark_auto_mapper_fhir.complex_types.resource_container import (
        ResourceContainer,
    )

    # extension (Extension)
    # modifierExtension (Extension)
    # code (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for code
    from spark_auto_mapper_fhir.value_sets.snomedct_medication_codes import (
        SNOMEDCTMedicationCodesCode,
    )

    # End Import for CodeableConcept for code
    # status (MedicationKnowledge Status Codes)
    from spark_auto_mapper_fhir.value_sets.medication_knowledge_status_codes import (
        MedicationKnowledgeStatusCodesCode,
    )

    # manufacturer (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for manufacturer
    from spark_auto_mapper_fhir.resources.organization import Organization

    # doseForm (CodeableConcept)
    # Import for CodeableConcept for doseForm
    from spark_auto_mapper_fhir.value_sets.snomedct_form_codes import (
        SNOMEDCTFormCodesCode,
    )

    # End Import for CodeableConcept for doseForm
    # amount (Quantity)
    from spark_auto_mapper_fhir.complex_types.quantity import Quantity

    # synonym (string)
    # relatedMedicationKnowledge (MedicationKnowledge.RelatedMedicationKnowledge)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_related_medication_knowledge import (
        MedicationKnowledgeRelatedMedicationKnowledge,
    )

    # associatedMedication (Reference)
    # Imports for References for associatedMedication
    from spark_auto_mapper_fhir.resources.medication import Medication

    # productType (CodeableConcept)
    # Import for CodeableConcept for productType
    from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode

    # End Import for CodeableConcept for productType
    # monograph (MedicationKnowledge.Monograph)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_monograph import (
        MedicationKnowledgeMonograph,
    )

    # ingredient (MedicationKnowledge.Ingredient)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_ingredient import (
        MedicationKnowledgeIngredient,
    )

    # preparationInstruction (markdown)
    from spark_auto_mapper_fhir.fhir_types.markdown import FhirMarkdown

    # intendedRoute (CodeableConcept)
    # Import for CodeableConcept for intendedRoute
    from spark_auto_mapper_fhir.value_sets.snomedct_route_codes import (
        SNOMEDCTRouteCodesCode,
    )

    # End Import for CodeableConcept for intendedRoute
    # cost (MedicationKnowledge.Cost)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_cost import (
        MedicationKnowledgeCost,
    )

    # monitoringProgram (MedicationKnowledge.MonitoringProgram)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_monitoring_program import (
        MedicationKnowledgeMonitoringProgram,
    )

    # administrationGuidelines (MedicationKnowledge.AdministrationGuidelines)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_administration_guidelines import (
        MedicationKnowledgeAdministrationGuidelines,
    )

    # medicineClassification (MedicationKnowledge.MedicineClassification)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_medicine_classification import (
        MedicationKnowledgeMedicineClassification,
    )

    # packaging (MedicationKnowledge.Packaging)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_packaging import (
        MedicationKnowledgePackaging,
    )

    # drugCharacteristic (MedicationKnowledge.DrugCharacteristic)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_drug_characteristic import (
        MedicationKnowledgeDrugCharacteristic,
    )

    # contraindication (Reference)
    # Imports for References for contraindication
    from spark_auto_mapper_fhir.resources.detected_issue import DetectedIssue

    # regulatory (MedicationKnowledge.Regulatory)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_regulatory import (
        MedicationKnowledgeRegulatory,
    )

    # kinetics (MedicationKnowledge.Kinetics)
    from spark_auto_mapper_fhir.backbone_elements.medication_knowledge_kinetics import (
        MedicationKnowledgeKinetics,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class MedicationKnowledge(FhirResourceBase):
    """
    MedicationKnowledge
    medicationknowledge.xsd
        Information about a medication that is used to support knowledge.
        If the element is present, it must have either a @value, an @id, or extensions
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        implicitRules: Optional[FhirUri] = None,
        language: Optional[CommonLanguagesCode] = None,
        text: Optional[Narrative] = None,
        contained: Optional[FhirList[ResourceContainer]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        code: Optional[CodeableConcept[SNOMEDCTMedicationCodesCode]] = None,
        status: Optional[MedicationKnowledgeStatusCodesCode] = None,
        manufacturer: Optional[Reference[Organization]] = None,
        doseForm: Optional[CodeableConcept[SNOMEDCTFormCodesCode]] = None,
        amount: Optional[Quantity] = None,
        synonym: Optional[FhirList[FhirString]] = None,
        relatedMedicationKnowledge: Optional[
            FhirList[MedicationKnowledgeRelatedMedicationKnowledge]
        ] = None,
        associatedMedication: Optional[FhirList[Reference[Medication]]] = None,
        productType: Optional[FhirList[CodeableConcept[GenericTypeCode]]] = None,
        monograph: Optional[FhirList[MedicationKnowledgeMonograph]] = None,
        ingredient: Optional[FhirList[MedicationKnowledgeIngredient]] = None,
        preparationInstruction: Optional[FhirMarkdown] = None,
        intendedRoute: Optional[
            FhirList[CodeableConcept[SNOMEDCTRouteCodesCode]]
        ] = None,
        cost: Optional[FhirList[MedicationKnowledgeCost]] = None,
        monitoringProgram: Optional[
            FhirList[MedicationKnowledgeMonitoringProgram]
        ] = None,
        administrationGuidelines: Optional[
            FhirList[MedicationKnowledgeAdministrationGuidelines]
        ] = None,
        medicineClassification: Optional[
            FhirList[MedicationKnowledgeMedicineClassification]
        ] = None,
        packaging: Optional[MedicationKnowledgePackaging] = None,
        drugCharacteristic: Optional[
            FhirList[MedicationKnowledgeDrugCharacteristic]
        ] = None,
        contraindication: Optional[FhirList[Reference[DetectedIssue]]] = None,
        regulatory: Optional[FhirList[MedicationKnowledgeRegulatory]] = None,
        kinetics: Optional[FhirList[MedicationKnowledgeKinetics]] = None,
    ) -> None:
        """
            Information about a medication that is used to support knowledge.
            If the element is present, it must have either a @value, an @id, or extensions

            :param id_: The logical id of the resource, as used in the URL for the resource. Once
        assigned, this value never changes.
            :param meta: The metadata about the resource. This is content that is maintained by the
        infrastructure. Changes to the content might not always be associated with
        version changes to the resource.
            :param implicitRules: A reference to a set of rules that were followed when the resource was
        constructed, and which must be understood when processing the content. Often,
        this is a reference to an implementation guide that defines the special rules
        along with other profiles etc.
            :param language: The base language in which the resource is written.
            :param text: A human-readable narrative that contains a summary of the resource and can be
        used to represent the content of the resource to a human. The narrative need
        not encode all the structured data, but is required to contain sufficient
        detail to make it "clinically safe" for a human to just read the narrative.
        Resource definitions may define what content should be represented in the
        narrative to ensure clinical safety.
            :param contained: These resources do not have an independent existence apart from the resource
        that contains them - they cannot be identified independently, and nor can they
        have their own independent transaction scope.
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the resource. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the resource and that modifies the understanding of the element
        that contains it and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer is allowed to define an extension, there is a set of requirements
        that SHALL be met as part of the definition of the extension. Applications
        processing a resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param code: A code that specifies this medication, or a textual description if no code is
        available. Usage note: This could be a standard medication code such as a code
        from RxNorm, SNOMED CT, IDMP etc. It could also be a national or local
        formulary code, optionally with translations to other code systems.
            :param status: A code to indicate if the medication is in active use.  The status refers to
        the validity about the information of the medication and not to its medicinal
        properties.
            :param manufacturer: Describes the details of the manufacturer of the medication product.  This is
        not intended to represent the distributor of a medication product.
            :param doseForm: Describes the form of the item.  Powder; tablets; capsule.
            :param amount: Specific amount of the drug in the packaged product.  For example, when
        specifying a product that has the same strength (For example, Insulin glargine
        100 unit per mL solution for injection), this attribute provides additional
        clarification of the package amount (For example, 3 mL, 10mL, etc.).
            :param synonym: Additional names for a medication, for example, the name(s) given to a
        medication in different countries.  For example, acetaminophen and paracetamol
        or salbutamol and albuterol.
            :param relatedMedicationKnowledge: Associated or related knowledge about a medication.
            :param associatedMedication: Associated or related medications.  For example, if the medication is a
        branded product (e.g. Crestor), this is the Therapeutic Moeity (e.g.
        Rosuvastatin) or if this is a generic medication (e.g. Rosuvastatin), this
        would link to a branded product (e.g. Crestor).
            :param productType: Category of the medication or product (e.g. branded product, therapeutic
        moeity, generic product, innovator product, etc.).
            :param monograph: Associated documentation about the medication.
            :param ingredient: Identifies a particular constituent of interest in the product.
            :param preparationInstruction: The instructions for preparing the medication.
            :param intendedRoute: The intended or approved route of administration.
            :param cost: The price of the medication.
            :param monitoringProgram: The program under which the medication is reviewed.
            :param administrationGuidelines: Guidelines for the administration of the medication.
            :param medicineClassification: Categorization of the medication within a formulary or classification system.
            :param packaging: Information that only applies to packages (not products).
            :param drugCharacteristic: Specifies descriptive properties of the medicine, such as color, shape,
        imprints, etc.
            :param contraindication: Potential clinical issue with or between medication(s) (for example, drug-drug
        interaction, drug-disease contraindication, drug-allergy interaction, etc.).
            :param regulatory: Regulatory information about a medication.
            :param kinetics: The time course of drug absorption, distribution, metabolism and excretion of
        a medication from the body.
        """
        super().__init__(
            resourceType="MedicationKnowledge",
            id_=id_,
            meta=meta,
            implicitRules=implicitRules,
            language=language,
            text=text,
            contained=contained,
            extension=extension,
            modifierExtension=modifierExtension,
            code=code,
            status=status,
            manufacturer=manufacturer,
            doseForm=doseForm,
            amount=amount,
            synonym=synonym,
            relatedMedicationKnowledge=relatedMedicationKnowledge,
            associatedMedication=associatedMedication,
            productType=productType,
            monograph=monograph,
            ingredient=ingredient,
            preparationInstruction=preparationInstruction,
            intendedRoute=intendedRoute,
            cost=cost,
            monitoringProgram=monitoringProgram,
            administrationGuidelines=administrationGuidelines,
            medicineClassification=medicineClassification,
            packaging=packaging,
            drugCharacteristic=drugCharacteristic,
            contraindication=contraindication,
            regulatory=regulatory,
            kinetics=kinetics,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MedicationKnowledgeSchema.get_schema(include_extension=include_extension)
