from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DetectedIssueCategory(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class DetectedIssueCategoryValues:
    Actaccountcode = DetectedIssueCategory("_ActAccountCode")
    Actadjudicationcode = DetectedIssueCategory("_ActAdjudicationCode")
    Actadjudicationresultactioncode = DetectedIssueCategory(
        "_ActAdjudicationResultActionCode"
    )
    Actbillablemodifiercode = DetectedIssueCategory("_ActBillableModifierCode")
    Actbillingarrangementcode = DetectedIssueCategory("_ActBillingArrangementCode")
    Actboundedroicode = DetectedIssueCategory("_ActBoundedROICode")
    ActCareProvision = DetectedIssueCategory("_ActCareProvisionCode")
    Actclaimattachmentcategorycode = DetectedIssueCategory(
        "_ActClaimAttachmentCategoryCode"
    )
    Actconsenttype = DetectedIssueCategory("_ActConsentType")
    Actcontainerregistrationcode = DetectedIssueCategory(
        "_ActContainerRegistrationCode"
    )
    Actcontrolvariable = DetectedIssueCategory("_ActControlVariable")
    Actcoverageconfirmationcode = DetectedIssueCategory("_ActCoverageConfirmationCode")
    Actcoveragelimitcode = DetectedIssueCategory("_ActCoverageLimitCode")
    Actcoveragetypecode = DetectedIssueCategory("_ActCoverageTypeCode")
    Actdetectedissuemanagementcode = DetectedIssueCategory(
        "_ActDetectedIssueManagementCode"
    )
    Actexposurecode = DetectedIssueCategory("_ActExposureCode")
    Actfinancialtransactioncode = DetectedIssueCategory("_ActFinancialTransactionCode")
    Actincidentcode = DetectedIssueCategory("_ActIncidentCode")
    Actinformationaccesscode = DetectedIssueCategory("_ActInformationAccessCode")
    Actinformationaccesscontextcode = DetectedIssueCategory(
        "_ActInformationAccessContextCode"
    )
    Actinformationcategorycode = DetectedIssueCategory("_ActInformationCategoryCode")
    Actinvoiceelementcode = DetectedIssueCategory("_ActInvoiceElementCode")
    Actinvoiceelementsummarycode = DetectedIssueCategory(
        "_ActInvoiceElementSummaryCode"
    )
    Actinvoiceoverridecode = DetectedIssueCategory("_ActInvoiceOverrideCode")
    Actlistcode = DetectedIssueCategory("_ActListCode")
    Actmonitoringprotocolcode = DetectedIssueCategory("_ActMonitoringProtocolCode")
    Actnonobservationindicationcode = DetectedIssueCategory(
        "_ActNonObservationIndicationCode"
    )
    ActObservationVerification = DetectedIssueCategory(
        "_ActObservationVerificationType"
    )
    Actpaymentcode = DetectedIssueCategory("_ActPaymentCode")
    Actpharmacysupplytype = DetectedIssueCategory("_ActPharmacySupplyType")
    Actpolicytype = DetectedIssueCategory("_ActPolicyType")
    Actproductacquisitioncode = DetectedIssueCategory("_ActProductAcquisitionCode")
    Actspecimentransportcode = DetectedIssueCategory("_ActSpecimenTransportCode")
    Actspecimentreatmentcode = DetectedIssueCategory("_ActSpecimenTreatmentCode")
    Actsubstanceadministrationcode = DetectedIssueCategory(
        "_ActSubstanceAdministrationCode"
    )
    Acttaskcode = DetectedIssueCategory("_ActTaskCode")
    Acttransportationmodecode = DetectedIssueCategory("_ActTransportationModeCode")
    Observationtype = DetectedIssueCategory("_ObservationType")
    Roioverlayshape = DetectedIssueCategory("_ROIOverlayShape")
    Corrected = DetectedIssueCategory("C")
    Diet = DetectedIssueCategory("DIET")
    DrugProgram = DetectedIssueCategory("DRUGPRG")
    Final = DetectedIssueCategory("F")
    Preliminary = DetectedIssueCategory("PRLMN")
    Securityobservationtype = DetectedIssueCategory("SECOBS")
    SubsidizedFeeForServiceProgram = DetectedIssueCategory("SUBSIDFFS")
    workersCompensationProgram = DetectedIssueCategory("WRKCOMP")
    Actprocedurecode = DetectedIssueCategory("_ActProcedureCode")
    Hl7definedactcodes = DetectedIssueCategory("_HL7DefinedActCodes")
    Copay = DetectedIssueCategory("COPAY")
    Deduct = DetectedIssueCategory("DEDUCT")
    Doseind = DetectedIssueCategory("DOSEIND")
    Pra = DetectedIssueCategory("PRA")
    Storage = DetectedIssueCategory("STORE")
    Actaccountcode = DetectedIssueCategory("_ActAccountCode")
    Actadjudicationcode = DetectedIssueCategory("_ActAdjudicationCode")
    Actadjudicationresultactioncode = DetectedIssueCategory(
        "_ActAdjudicationResultActionCode"
    )
    Actbillablemodifiercode = DetectedIssueCategory("_ActBillableModifierCode")
    Actbillingarrangementcode = DetectedIssueCategory("_ActBillingArrangementCode")
    Actboundedroicode = DetectedIssueCategory("_ActBoundedROICode")
    ActCareProvision = DetectedIssueCategory("_ActCareProvisionCode")
    Actclaimattachmentcategorycode = DetectedIssueCategory(
        "_ActClaimAttachmentCategoryCode"
    )
    Actconsenttype = DetectedIssueCategory("_ActConsentType")
    Actcontainerregistrationcode = DetectedIssueCategory(
        "_ActContainerRegistrationCode"
    )
    Actcontrolvariable = DetectedIssueCategory("_ActControlVariable")
    Actcoverageconfirmationcode = DetectedIssueCategory("_ActCoverageConfirmationCode")
    Actcoveragelimitcode = DetectedIssueCategory("_ActCoverageLimitCode")
    Actcoveragetypecode = DetectedIssueCategory("_ActCoverageTypeCode")
    Actdetectedissuemanagementcode = DetectedIssueCategory(
        "_ActDetectedIssueManagementCode"
    )
    Actexposurecode = DetectedIssueCategory("_ActExposureCode")
    Actfinancialtransactioncode = DetectedIssueCategory("_ActFinancialTransactionCode")
    Actincidentcode = DetectedIssueCategory("_ActIncidentCode")
    Actinformationaccesscode = DetectedIssueCategory("_ActInformationAccessCode")
    Actinformationaccesscontextcode = DetectedIssueCategory(
        "_ActInformationAccessContextCode"
    )
    Actinformationcategorycode = DetectedIssueCategory("_ActInformationCategoryCode")
    Actinvoiceelementcode = DetectedIssueCategory("_ActInvoiceElementCode")
    Actinvoiceelementsummarycode = DetectedIssueCategory(
        "_ActInvoiceElementSummaryCode"
    )
    Actinvoiceoverridecode = DetectedIssueCategory("_ActInvoiceOverrideCode")
    Actlistcode = DetectedIssueCategory("_ActListCode")
    Actmonitoringprotocolcode = DetectedIssueCategory("_ActMonitoringProtocolCode")
    Actnonobservationindicationcode = DetectedIssueCategory(
        "_ActNonObservationIndicationCode"
    )
    ActObservationVerification = DetectedIssueCategory(
        "_ActObservationVerificationType"
    )
    Actpaymentcode = DetectedIssueCategory("_ActPaymentCode")
    Actpharmacysupplytype = DetectedIssueCategory("_ActPharmacySupplyType")
    Actpolicytype = DetectedIssueCategory("_ActPolicyType")
    Actproductacquisitioncode = DetectedIssueCategory("_ActProductAcquisitionCode")
    Actspecimentransportcode = DetectedIssueCategory("_ActSpecimenTransportCode")
    Actspecimentreatmentcode = DetectedIssueCategory("_ActSpecimenTreatmentCode")
    Actsubstanceadministrationcode = DetectedIssueCategory(
        "_ActSubstanceAdministrationCode"
    )
    Acttaskcode = DetectedIssueCategory("_ActTaskCode")
    Acttransportationmodecode = DetectedIssueCategory("_ActTransportationModeCode")
    Observationtype = DetectedIssueCategory("_ObservationType")
    Roioverlayshape = DetectedIssueCategory("_ROIOverlayShape")
    Corrected = DetectedIssueCategory("C")
    Diet = DetectedIssueCategory("DIET")
    DrugProgram = DetectedIssueCategory("DRUGPRG")
    Final = DetectedIssueCategory("F")
    Preliminary = DetectedIssueCategory("PRLMN")
    Securityobservationtype = DetectedIssueCategory("SECOBS")
    SubsidizedFeeForServiceProgram = DetectedIssueCategory("SUBSIDFFS")
    workersCompensationProgram = DetectedIssueCategory("WRKCOMP")
    Actprocedurecode = DetectedIssueCategory("_ActProcedureCode")
    Hl7definedactcodes = DetectedIssueCategory("_HL7DefinedActCodes")
    Copay = DetectedIssueCategory("COPAY")
    Deduct = DetectedIssueCategory("DEDUCT")
    Doseind = DetectedIssueCategory("DOSEIND")
    Pra = DetectedIssueCategory("PRA")
    Storage = DetectedIssueCategory("STORE")
    Actaccountcode = DetectedIssueCategory("_ActAccountCode")
    Actadjudicationcode = DetectedIssueCategory("_ActAdjudicationCode")
    Actadjudicationresultactioncode = DetectedIssueCategory(
        "_ActAdjudicationResultActionCode"
    )
    Actbillablemodifiercode = DetectedIssueCategory("_ActBillableModifierCode")
    Actbillingarrangementcode = DetectedIssueCategory("_ActBillingArrangementCode")
    Actboundedroicode = DetectedIssueCategory("_ActBoundedROICode")
    ActCareProvision = DetectedIssueCategory("_ActCareProvisionCode")
    Actclaimattachmentcategorycode = DetectedIssueCategory(
        "_ActClaimAttachmentCategoryCode"
    )
    Actconsenttype = DetectedIssueCategory("_ActConsentType")
    Actcontainerregistrationcode = DetectedIssueCategory(
        "_ActContainerRegistrationCode"
    )
    Actcontrolvariable = DetectedIssueCategory("_ActControlVariable")
    Actcoverageconfirmationcode = DetectedIssueCategory("_ActCoverageConfirmationCode")
    Actcoveragelimitcode = DetectedIssueCategory("_ActCoverageLimitCode")
    Actcoveragetypecode = DetectedIssueCategory("_ActCoverageTypeCode")
    Actdetectedissuemanagementcode = DetectedIssueCategory(
        "_ActDetectedIssueManagementCode"
    )
    Actexposurecode = DetectedIssueCategory("_ActExposureCode")
    Actfinancialtransactioncode = DetectedIssueCategory("_ActFinancialTransactionCode")
    Actincidentcode = DetectedIssueCategory("_ActIncidentCode")
    Actinformationaccesscode = DetectedIssueCategory("_ActInformationAccessCode")
    Actinformationaccesscontextcode = DetectedIssueCategory(
        "_ActInformationAccessContextCode"
    )
    Actinformationcategorycode = DetectedIssueCategory("_ActInformationCategoryCode")
    Actinvoiceelementcode = DetectedIssueCategory("_ActInvoiceElementCode")
    Actinvoiceelementsummarycode = DetectedIssueCategory(
        "_ActInvoiceElementSummaryCode"
    )
    Actinvoiceoverridecode = DetectedIssueCategory("_ActInvoiceOverrideCode")
    Actlistcode = DetectedIssueCategory("_ActListCode")
    Actmonitoringprotocolcode = DetectedIssueCategory("_ActMonitoringProtocolCode")
    Actnonobservationindicationcode = DetectedIssueCategory(
        "_ActNonObservationIndicationCode"
    )
    ActObservationVerification = DetectedIssueCategory(
        "_ActObservationVerificationType"
    )
    Actpaymentcode = DetectedIssueCategory("_ActPaymentCode")
    Actpharmacysupplytype = DetectedIssueCategory("_ActPharmacySupplyType")
    Actpolicytype = DetectedIssueCategory("_ActPolicyType")
    Actproductacquisitioncode = DetectedIssueCategory("_ActProductAcquisitionCode")
    Actspecimentransportcode = DetectedIssueCategory("_ActSpecimenTransportCode")
    Actspecimentreatmentcode = DetectedIssueCategory("_ActSpecimenTreatmentCode")
    Actsubstanceadministrationcode = DetectedIssueCategory(
        "_ActSubstanceAdministrationCode"
    )
    Acttaskcode = DetectedIssueCategory("_ActTaskCode")
    Acttransportationmodecode = DetectedIssueCategory("_ActTransportationModeCode")
    Observationtype = DetectedIssueCategory("_ObservationType")
    Roioverlayshape = DetectedIssueCategory("_ROIOverlayShape")
    Corrected = DetectedIssueCategory("C")
    Diet = DetectedIssueCategory("DIET")
    DrugProgram = DetectedIssueCategory("DRUGPRG")
    Final = DetectedIssueCategory("F")
    Preliminary = DetectedIssueCategory("PRLMN")
    Securityobservationtype = DetectedIssueCategory("SECOBS")
    SubsidizedFeeForServiceProgram = DetectedIssueCategory("SUBSIDFFS")
    workersCompensationProgram = DetectedIssueCategory("WRKCOMP")
    Actprocedurecode = DetectedIssueCategory("_ActProcedureCode")
    Hl7definedactcodes = DetectedIssueCategory("_HL7DefinedActCodes")
    Copay = DetectedIssueCategory("COPAY")
    Deduct = DetectedIssueCategory("DEDUCT")
    Doseind = DetectedIssueCategory("DOSEIND")
    Pra = DetectedIssueCategory("PRA")
    Storage = DetectedIssueCategory("STORE")