from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimInformationCategoryCodesCode(GenericTypeCode):
    """
    ClaimInformationCategoryCodes
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
        This value set includes sample Information Category codes.
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/claiminformationcategory
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/claiminformationcategory"


class ClaimInformationCategoryCodesCodeValues:
    """
    Codes conveying additional situation and condition information.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """

    Information = ClaimInformationCategoryCodesCode("info")
    """
    Discharge status and discharge to locations.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    Discharge = ClaimInformationCategoryCodesCode("discharge")
    """
    Period, start or end dates of aspects of the Condition.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    Onset = ClaimInformationCategoryCodesCode("onset")
    """
    Nature and date of the related event e.g. Last exam, service, X-ray etc.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    RelatedServices = ClaimInformationCategoryCodesCode("related")
    """
    Insurance policy exceptions.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    Exception = ClaimInformationCategoryCodesCode("exception")
    """
    Materials being forwarded, e.g. Models, molds, images, documents.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    MaterialsForwarded = ClaimInformationCategoryCodesCode("material")
    """
    Materials attached such as images, documents and resources.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    Attachment = ClaimInformationCategoryCodesCode("attachment")
    """
    Teeth which are missing for any reason, for example: prior extraction, never
    developed.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    MissingTooth = ClaimInformationCategoryCodesCode("missingtooth")
    """
    The type of prosthesis and date of supply if a previously supplied prosthesis.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    Prosthesis = ClaimInformationCategoryCodesCode("prosthesis")
    """
    Other information identified by the type.system.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    Other = ClaimInformationCategoryCodesCode("other")
    """
    An indication that the patient was hospitalized, the period if known otherwise
    a Yes/No (boolean).
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    Hospitalized = ClaimInformationCategoryCodesCode("hospitalized")
    """
    An indication that the patient was unable to work, the period if known
    otherwise a Yes/No (boolean).
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    EmploymentImpacted = ClaimInformationCategoryCodesCode("employmentimpacted")
    """
    The external cause of an illness or injury.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    ExternalCaause = ClaimInformationCategoryCodesCode("externalcause")
    """
    The reason for the patient visit.
    From: http://terminology.hl7.org/CodeSystem/claiminformationcategory in valuesets.xml
    """
    PatientReasonForVisit = ClaimInformationCategoryCodesCode("patientreasonforvisit")
