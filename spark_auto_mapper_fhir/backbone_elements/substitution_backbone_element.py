from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.act_substance_admin_substitution_code import (
    ActSubstanceAdminSubstitutionCode,
)
from spark_auto_mapper_fhir.valuesets.substance_admin_substitution_reason import (
    SubstanceAdminSubstitutionReasonCode,
)


class SubstitutionBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        allowedBoolean: Optional[FhirBoolean] = None,
        allowedCodeableConcept: Optional[
            CodeableConcept[ActSubstanceAdminSubstitutionCode]
        ] = None,
        reason: Optional[CodeableConcept[SubstanceAdminSubstitutionReasonCode]] = None,
    ):
        """
        SubstitutionBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#SubstitutionBackboneElement


        :param allowedBoolean: Whether substitution is allowed or not. https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
        :param allowedCodeableConcept: Whether substitution is allowed or not. https://hl7.org/FHIR/v3/ActSubstanceAdminSubstitutionCode/vs.html
        :param reason: Why should (not) substitution be made. https://hl7.org/FHIR/v3/SubstanceAdminSubstitutionReason/vs.html
        """
        super().__init__(
            id_=id_,
            extension=extension,
            allowedBoolean=allowedBoolean,
            allowedCodeableConcept=allowedCodeableConcept,
            reason=reason,
        )
