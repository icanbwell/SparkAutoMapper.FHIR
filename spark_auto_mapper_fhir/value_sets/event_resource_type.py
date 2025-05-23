from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EventResourceTypeCode(GenericTypeCode):
    """
    EventResourceType
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
        A list of all the event resource types defined in this version of the FHIR
    specification.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://hl7.org/fhir/event-resource-types
    """
    codeset: FhirUri = "http://hl7.org/fhir/event-resource-types"


class EventResourceTypeCodeValues:
    """
    Item containing charge code(s) associated with the provision of healthcare
    provider products.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """

    ChargeItem = EventResourceTypeCode("ChargeItem")
    """
    Remittance resource.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    ClaimResponse = EventResourceTypeCode("ClaimResponse")
    """
    A clinical assessment performed when planning treatments and management
    strategies for a patient.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    ClinicalImpression = EventResourceTypeCode("ClinicalImpression")
    """
    A record of information transmitted from a sender to a receiver.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Communication = EventResourceTypeCode("Communication")
    """
    A set of resources composed into a single coherent clinical statement with
    clinical attestation.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Composition = EventResourceTypeCode("Composition")
    """
    Detailed information about conditions, problems or diagnoses.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Condition = EventResourceTypeCode("Condition")
    """
    A healthcare consumer's policy choices to permits or denies recipients or
    roles to perform actions for specific purposes and periods of time.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Consent = EventResourceTypeCode("Consent")
    """
    Insurance or medical plan or a payment agreement.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Coverage = EventResourceTypeCode("Coverage")
    """
    Record of use of a device.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    DeviceUseStatement = EventResourceTypeCode("DeviceUseStatement")
    """
    A Diagnostic report - a combination of request information, atomic results,
    images, interpretation, as well as formatted reports.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    DiagnosticReport = EventResourceTypeCode("DiagnosticReport")
    """
    A list that defines a set of documents.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    DocumentManifest = EventResourceTypeCode("DocumentManifest")
    """
    A reference to a document.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    DocumentReference = EventResourceTypeCode("DocumentReference")
    """
    An interaction during which services are provided to the patient.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Encounter = EventResourceTypeCode("Encounter")
    """
    EnrollmentResponse resource.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    EnrollmentResponse = EventResourceTypeCode("EnrollmentResponse")
    """
    An association of a Patient with an Organization and  Healthcare Provider(s)
    for a period of time that the Organization assumes some level of
    responsibility.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    EpisodeOfCare = EventResourceTypeCode("EpisodeOfCare")
    """
    Explanation of Benefit resource.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    ExplanationOfBenefit = EventResourceTypeCode("ExplanationOfBenefit")
    """
    Information about patient's relatives, relevant for patient.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    FamilyMemberHistory = EventResourceTypeCode("FamilyMemberHistory")
    """
    The formal response to a guidance request.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    GuidanceResponse = EventResourceTypeCode("GuidanceResponse")
    """
    A set of images produced in single study (one or more series of references
    images).
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    ImagingStudy = EventResourceTypeCode("ImagingStudy")
    """
    Immunization event information.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Immunization = EventResourceTypeCode("Immunization")
    """
    Results of a measure evaluation.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    MeasureReport = EventResourceTypeCode("MeasureReport")
    """
    A photo, video, or audio recording acquired or used in healthcare. The actual
    content may be inline or provided by direct reference.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Media = EventResourceTypeCode("Media")
    """
    Administration of medication to a patient.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    MedicationAdministration = EventResourceTypeCode("MedicationAdministration")
    """
    Dispensing a medication to a named patient.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    MedicationDispense = EventResourceTypeCode("MedicationDispense")
    """
    Record of medication being taken by a patient.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    MedicationStatement = EventResourceTypeCode("MedicationStatement")
    """
    Measurements and simple assertions.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Observation = EventResourceTypeCode("Observation")
    """
    PaymentNotice request.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    PaymentNotice = EventResourceTypeCode("PaymentNotice")
    """
    PaymentReconciliation resource.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    PaymentReconciliation = EventResourceTypeCode("PaymentReconciliation")
    """
    An action that is being or was performed on a patient.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Procedure = EventResourceTypeCode("Procedure")
    """
    ProcessResponse resource.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    ProcessResponse = EventResourceTypeCode("ProcessResponse")
    """
    A structured set of questions and their answers.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    QuestionnaireResponse = EventResourceTypeCode("QuestionnaireResponse")
    """
    Potential outcomes for a subject with likelihood.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    RiskAssessment = EventResourceTypeCode("RiskAssessment")
    """
    Delivery of bulk Supplies.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    SupplyDelivery = EventResourceTypeCode("SupplyDelivery")
    """
    A task to be performed.
    From: http://hl7.org/fhir/event-resource-types in valuesets.xml
    """
    Task = EventResourceTypeCode("Task")
