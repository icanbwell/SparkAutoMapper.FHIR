from typing import Optional, Union

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.encounter_admit_source import (
    EncounterAdmitSourceCode,
)
from spark_auto_mapper_fhir.valuesets.encounter_diet import EncounterDietCode
from spark_auto_mapper_fhir.valuesets.encounter_dischage_disposition import (
    EncounterDischargeDispositionCode,
)
from spark_auto_mapper_fhir.valuesets.encounter_special_Courtesy import (
    EncounterSpecialCourtesyCode,
)
from spark_auto_mapper_fhir.valuesets.v3_re_admission_indicator import (
    V3ReAdmissionIndicatorCode,
)


class EncounterHospitalizationBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        *,
        id_: Optional[FhirId] = None,
        preAdmissionIdentifier: Optional[Identifier] = None,
        origin: Optional[Reference[Union[Location, Organization]]] = None,
        admitSource: Optional[CodeableConcept[EncounterAdmitSourceCode]] = None,
        reAdmission: Optional[CodeableConcept[V3ReAdmissionIndicatorCode]] = None,
        dietPreference: Optional[FhirList[CodeableConcept[EncounterDietCode]]] = None,
        specialCourtesy: Optional[
            FhirList[CodeableConcept[EncounterSpecialCourtesyCode]]
        ] = None,
        specialArrangement: Optional[
            FhirList[CodeableConcept[EncounterSpecialCourtesyCode]]
        ] = None,
        destination: Optional[Reference[Union[Location, Organization]]] = None,
        dischargeDisposition: Optional[
            CodeableConcept[EncounterDischargeDispositionCode]
        ] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        EncounterHospitalizationBackboneElement Backbone Element in FHIR
        IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                    properties not just the ones you need
        https://hl7.org/FHIR/encounter-definitions.html#Encounter.hospitalization
        """
        super().__init__(
            id_=id_,
            preAdmissionIdentifier=preAdmissionIdentifier,
            origin=origin,
            admitSource=admitSource,
            reAdmission=reAdmission,
            dietPreference=dietPreference,
            specialCourtesy=specialCourtesy,
            specialArrangement=specialArrangement,
            destination=destination,
            dischargeDisposition=dischargeDisposition,
            extension=extension,
        )
