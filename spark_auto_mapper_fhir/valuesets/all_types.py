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
        return FhirAllTypesCode("backboneelement")

    @classproperty
    def Coding(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("coding")

    @classproperty
    def ContactPoint(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("contactpoint")

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
        return FhirAllTypesCode("elementdefinition")

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
        return FhirAllTypesCode("moneyquantity")

    @classproperty
    def ParameterDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("parameterdefinition")

    @classproperty
    def Population(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("population")

    @classproperty
    def ProductShelfLife(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("productshelflife")

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
        return FhirAllTypesCode("sampleddata")

    @classproperty
    def SimpleQuantity(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("simplequantity")

    @classproperty
    def Timing(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("timing")

    @classproperty
    def UsageContext(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("usagecontext")

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
        return FhirAllTypesCode("datetime")

    @classproperty
    def id(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("id")

    @classproperty
    def integer(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("integer")

    @classproperty
    def string(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("string")

    @classproperty
    def unsignedInt(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("unsignedint")

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
        return FhirAllTypesCode("activitydefinition")

    @classproperty
    def AllergyIntolerance(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("allergyintolerance")

    @classproperty
    def AppointmentResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("appointmentresponse")

    @classproperty
    def Basic(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("basic")

    @classproperty
    def BiologicallyDerivedProduct(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("biologicallyderivedproduct")

    @classproperty
    def Bundle(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("bundle")

    @classproperty
    def CarePlan(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("careplan")

    @classproperty
    def CatalogEntry(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("catalogentry")

    @classproperty
    def ChargeItemDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("chargeitemdefinition")

    @classproperty
    def ClaimResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("claimresponse")

    @classproperty
    def CodeSystem(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("codesystem")

    @classproperty
    def CommunicationRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("communicationrequest")

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
        return FhirAllTypesCode("coverageeligibilityrequest")

    @classproperty
    def DetectedIssue(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("detectedissue")

    @classproperty
    def DeviceDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("devicedefinition")

    @classproperty
    def DeviceRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("devicerequest")

    @classproperty
    def DiagnosticReport(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("diagnosticreport")

    @classproperty
    def DocumentReference(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("documentreference")

    @classproperty
    def EffectEvidenceSynthesis(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("effectevidencesynthesis")

    @classproperty
    def Endpoint(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("endpoint")

    @classproperty
    def EnrollmentResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("enrollmentresponse")

    @classproperty
    def EventDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("eventdefinition")

    @classproperty
    def EvidenceVariable(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("evidencevariable")

    @classproperty
    def ExplanationOfBenefit(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("explanationofbenefit")

    @classproperty
    def Flag(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("flag")

    @classproperty
    def GraphDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("graphdefinition")

    @classproperty
    def GuidanceResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("guidanceresponse")

    @classproperty
    def ImagingStudy(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("imagingstudy")

    @classproperty
    def ImmunizationEvaluation(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("immunizationevaluation")

    @classproperty
    def ImplementationGuide(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("implementationguide")

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
        return FhirAllTypesCode("measurereport")

    @classproperty
    def Medication(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medication")

    @classproperty
    def MedicationDispense(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicationdispense")

    @classproperty
    def MedicationRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicationrequest")

    @classproperty
    def MedicinalProduct(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinalproduct")

    @classproperty
    def MedicinalProductContraindication(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinalproductcontraindication")

    @classproperty
    def MedicinalProductIngredient(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinalproductingredient")

    @classproperty
    def MedicinalProductManufactured(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinalproductmanufactured")

    @classproperty
    def MedicinalProductPharmaceutical(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("medicinalproductpharmaceutical")

    @classproperty
    def MessageDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("messagedefinition")

    @classproperty
    def MolecularSequence(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("molecularsequence")

    @classproperty
    def NutritionOrder(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("nutritionorder")

    @classproperty
    def ObservationDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("observationdefinition")

    @classproperty
    def OperationOutcome(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("operationoutcome")

    @classproperty
    def OrganizationAffiliation(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("organizationaffiliation")

    @classproperty
    def Patient(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("patient")

    @classproperty
    def PaymentReconciliation(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("paymentreconciliation")

    @classproperty
    def PlanDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("plandefinition")

    @classproperty
    def PractitionerRole(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("practitionerrole")

    @classproperty
    def Provenance(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("provenance")

    @classproperty
    def QuestionnaireResponse(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("questionnaireresponse")

    @classproperty
    def RequestGroup(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("requestgroup")

    @classproperty
    def ResearchElementDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("researchelementdefinition")

    @classproperty
    def ResearchSubject(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("researchsubject")

    @classproperty
    def RiskAssessment(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("riskassessment")

    @classproperty
    def Schedule(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("schedule")

    @classproperty
    def ServiceRequest(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("servicerequest")

    @classproperty
    def Specimen(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("specimen")

    @classproperty
    def StructureDefinition(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("structuredefinition")

    @classproperty
    def Subscription(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("subscription")

    @classproperty
    def SubstanceNucleicAcid(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("substancenucleicacid")

    @classproperty
    def SubstanceProtein(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("substanceprotein")

    @classproperty
    def SubstanceSourceMaterial(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("substancesourcematerial")

    @classproperty
    def SupplyDelivery(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("supplydelivery")

    @classproperty
    def Task(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("task")

    @classproperty
    def TestReport(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("testreport")

    @classproperty
    def ValueSet(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("valueset")

    @classproperty
    def VisionPrescription(cls) -> 'FhirAllTypesCode':
        # noinspection PyCallingNonCallable
        return FhirAllTypesCode("visionprescription")

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
