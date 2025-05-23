from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DiagnosticServiceSectionCodesCode(GenericTypeCode):
    """
    DiagnosticServiceSectionCodes
    From: http://hl7.org/fhir/ValueSet/diagnostic-service-sections in valuesets.xml
        This value set includes all the codes in HL7 V2 table 0074.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v2-0074
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v2-0074"


class DiagnosticServiceSectionCodesCodeValues:
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """

    Audiology = DiagnosticServiceSectionCodesCode("AU")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    BloodGases = DiagnosticServiceSectionCodesCode("BG")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    BloodBank = DiagnosticServiceSectionCodesCode("BLB")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Cytogenetics = DiagnosticServiceSectionCodesCode("CG")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Chemistry = DiagnosticServiceSectionCodesCode("CH")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Cytopathology = DiagnosticServiceSectionCodesCode("CP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    CATScan = DiagnosticServiceSectionCodesCode("CT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    CardiacCatheterization = DiagnosticServiceSectionCodesCode("CTH")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    CardiacUltrasound = DiagnosticServiceSectionCodesCode("CUS")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Electrocardiac_e_g_EKG_EEC_Holter_ = DiagnosticServiceSectionCodesCode("EC")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Electroneuro_EEG_EMG_EP_PSG_ = DiagnosticServiceSectionCodesCode("EN")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Genetics = DiagnosticServiceSectionCodesCode("GE")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Hematology = DiagnosticServiceSectionCodesCode("HM")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    BedsideICUMonitoring = DiagnosticServiceSectionCodesCode("ICU")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    DiagnosticImaging = DiagnosticServiceSectionCodesCode("IMG")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Immunology = DiagnosticServiceSectionCodesCode("IMM")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Laboratory = DiagnosticServiceSectionCodesCode("LAB")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Microbiology = DiagnosticServiceSectionCodesCode("MB")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Mycobacteriology = DiagnosticServiceSectionCodesCode("MCB")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Mycology = DiagnosticServiceSectionCodesCode("MYC")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    NuclearMagneticResonance = DiagnosticServiceSectionCodesCode("NMR")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    NuclearMedicineScan = DiagnosticServiceSectionCodesCode("NMS")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    NursingServiceMeasures = DiagnosticServiceSectionCodesCode("NRS")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    OutsideLab = DiagnosticServiceSectionCodesCode("OSL")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    OccupationalTherapy = DiagnosticServiceSectionCodesCode("OT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Other = DiagnosticServiceSectionCodesCode("OTH")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    OBUltrasound = DiagnosticServiceSectionCodesCode("OUS")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Parasitology = DiagnosticServiceSectionCodesCode("PAR")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Pathology_gross_Histopath_NotSurgical_ = DiagnosticServiceSectionCodesCode("PAT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    PulmonaryFunction = DiagnosticServiceSectionCodesCode("PF")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Pharmacy = DiagnosticServiceSectionCodesCode("PHR")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Physician_Hx_Dx_AdmissionNote_Etc_ = DiagnosticServiceSectionCodesCode("PHY")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    PhysicalTherapy = DiagnosticServiceSectionCodesCode("PT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Radiology = DiagnosticServiceSectionCodesCode("RAD")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    RespiratoryCare_therapy_ = DiagnosticServiceSectionCodesCode("RC")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    RadiationTherapy = DiagnosticServiceSectionCodesCode("RT")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    RadiologyUltrasound = DiagnosticServiceSectionCodesCode("RUS")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Radiograph = DiagnosticServiceSectionCodesCode("RX")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    SurgicalPathology = DiagnosticServiceSectionCodesCode("SP")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Serology = DiagnosticServiceSectionCodesCode("SR")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Toxicology = DiagnosticServiceSectionCodesCode("TX")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Urinalysis = DiagnosticServiceSectionCodesCode("URN")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Virology = DiagnosticServiceSectionCodesCode("VR")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    VascularUltrasound = DiagnosticServiceSectionCodesCode("VUS")
    """
    From: http://terminology.hl7.org/CodeSystem/v2-0074 in v2-tables.xml
    """
    Cineradiograph = DiagnosticServiceSectionCodesCode("XRC")
