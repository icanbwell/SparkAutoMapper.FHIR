from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirAllTypesCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-all-types.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirAllTypesCode']) -> None:
            self.f: Callable[..., 'FhirAllTypesCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirAllTypesCode']
        ) -> 'FhirAllTypesCode':
            return self.f(owner)

    @classproperty
    def Address(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("address")

    @classproperty
    def Annotation(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("annotation")

    @classproperty
    def BackboneElement(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("backbone_element")

    @classproperty
    def Coding(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("coding")

    @classproperty
    def ContactPoint(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("contact_point")

    @classproperty
    def Count(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("count")

    @classproperty
    def Distance(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("distance")

    @classproperty
    def Duration(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("duration")

    @classproperty
    def ElementDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("element_definition")

    @classproperty
    def Extension(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("extension")

    @classproperty
    def Identifier(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("identifier")

    @classproperty
    def Meta(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("meta")

    @classproperty
    def MoneyQuantity(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("money_quantity")

    @classproperty
    def ParameterDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("parameter_definition")

    @classproperty
    def Population(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("population")

    @classproperty
    def ProductShelfLife(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("product_shelf_life")

    @classproperty
    def Range(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("range")

    @classproperty
    def Reference(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("reference")

    @classproperty
    def SampledData(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("sampled_data")

    @classproperty
    def SimpleQuantity(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("simple_quantity")

    @classproperty
    def Timing(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("timing")

    @classproperty
    def UsageContext(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("usage_context")

    @classproperty
    def boolean(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("boolean")

    @classproperty
    def code(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("code")

    @classproperty
    def dateTime(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("date_time")

    @classproperty
    def id(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("id")

    @classproperty
    def integer(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("integer")

    @classproperty
    def oid_(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("oid")

    @classproperty
    def string(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("string")

    @classproperty
    def unsignedInt(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("unsigned_int")

    @classproperty
    def url(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("url")

    @classproperty
    def xhtml(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("xhtml")

    @classproperty
    def ActivityDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("activity_definition")

    @classproperty
    def AllergyIntolerance(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("allergy_intolerance")

    @classproperty
    def AppointmentResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("appointment_response")

    @classproperty
    def Basic(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("basic")

    @classproperty
    def BiologicallyDerivedProduct(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("biologically_derived_product")

    @classproperty
    def Bundle(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("bundle")

    @classproperty
    def CarePlan(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("care_plan")

    @classproperty
    def CatalogEntry(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("catalog_entry")

    @classproperty
    def ChargeItemDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("charge_item_definition")

    @classproperty
    def ClaimResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("claim_response")

    @classproperty
    def CodeSystem(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("code_system")

    @classproperty
    def CommunicationRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("communication_request")

    @classproperty
    def Composition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("composition")

    @classproperty
    def Condition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("condition")

    @classproperty
    def Contract(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("contract")

    @classproperty
    def CoverageEligibilityRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("coverage_eligibility_request")

    @classproperty
    def DetectedIssue(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("detected_issue")

    @classproperty
    def DeviceDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("device_definition")

    @classproperty
    def DeviceRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("device_request")

    @classproperty
    def DiagnosticReport(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("diagnostic_report")

    @classproperty
    def DocumentReference(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("document_reference")

    @classproperty
    def EffectEvidenceSynthesis(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("effect_evidence_synthesis")

    @classproperty
    def Endpoint(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("endpoint")

    @classproperty
    def EnrollmentResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("enrollment_response")

    @classproperty
    def EventDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("event_definition")

    @classproperty
    def EvidenceVariable(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("evidence_variable")

    @classproperty
    def ExplanationOfBenefit(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("explanation_of_benefit")

    @classproperty
    def Flag(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("flag")

    @classproperty
    def GraphDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("graph_definition")

    @classproperty
    def GuidanceResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("guidance_response")

    @classproperty
    def ImagingStudy(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("imaging_study")

    @classproperty
    def ImmunizationEvaluation(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("immunization_evaluation")

    @classproperty
    def ImplementationGuide(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("implementation_guide")

    @classproperty
    def Invoice(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("invoice")

    @classproperty
    def Linkage(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("linkage")

    @classproperty
    def Location(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("location")

    @classproperty
    def MeasureReport(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("measure_report")

    @classproperty
    def Medication(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medication")

    @classproperty
    def MedicationDispense(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medication_dispense")

    @classproperty
    def MedicationRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medication_request")

    @classproperty
    def MedicinalProduct(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinal_product")

    @classproperty
    def MedicinalProductContraindication(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinal_product_contraindication")

    @classproperty
    def MedicinalProductIngredient(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinal_product_ingredient")

    @classproperty
    def MedicinalProductManufactured(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinal_product_manufactured")

    @classproperty
    def MedicinalProductPharmaceutical(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinal_product_pharmaceutical")

    @classproperty
    def MessageDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("message_definition")

    @classproperty
    def MolecularSequence(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("molecular_sequence")

    @classproperty
    def NutritionOrder(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("nutrition_order")

    @classproperty
    def ObservationDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("observation_definition")

    @classproperty
    def OperationOutcome(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("operation_outcome")

    @classproperty
    def OrganizationAffiliation(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("organization_affiliation")

    @classproperty
    def Patient(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("patient")

    @classproperty
    def PaymentReconciliation(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("payment_reconciliation")

    @classproperty
    def PlanDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("plan_definition")

    @classproperty
    def PractitionerRole(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("practitioner_role")

    @classproperty
    def Provenance(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("provenance")

    @classproperty
    def QuestionnaireResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("questionnaire_response")

    @classproperty
    def RequestGroup(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("request_group")

    @classproperty
    def ResearchElementDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("research_element_definition")

    @classproperty
    def ResearchSubject(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("research_subject")

    @classproperty
    def RiskAssessment(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("risk_assessment")

    @classproperty
    def Schedule(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("schedule")

    @classproperty
    def ServiceRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("service_request")

    @classproperty
    def Specimen(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("specimen")

    @classproperty
    def StructureDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("structure_definition")

    @classproperty
    def Subscription(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("subscription")

    @classproperty
    def SubstanceNucleicAcid(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("substance_nucleic_acid")

    @classproperty
    def SubstanceProtein(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("substance_protein")

    @classproperty
    def SubstanceSourceMaterial(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("substance_source_material")

    @classproperty
    def SupplyDelivery(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("supply_delivery")

    @classproperty
    def Task(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("task")

    @classproperty
    def TestReport(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("test_report")

    @classproperty
    def ValueSet(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("value_set")

    @classproperty
    def VisionPrescription(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("vision_prescription")

    @classproperty
    def Any(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("any")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/all-types
        """
        return "http://hl7.org/fhir/ValueSet/all-types"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.25
        """
        return "2.16.840.1.113883.4.642.3.25"
