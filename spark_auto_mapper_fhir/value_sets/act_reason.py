from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ActReason(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class ActReasonValues:
    Actaccommodationreason = ActReason("_ActAccommodationReason")
    Actcoveragereason = ActReason("_ActCoverageReason")
    Actinformationmanagementreason = ActReason("_ActInformationManagementReason")
    Actinvalidreason = ActReason("_ActInvalidReason")
    Actinvoicecancelreason = ActReason("_ActInvoiceCancelReason")
    Actnoimmunizationreason = ActReason("_ActNoImmunizationReason")
    Actsupplyfulfillmentrefusalreason = ActReason("_ActSupplyFulfillmentRefusalReason")
    Clinicalresearcheventreason = ActReason("_ClinicalResearchEventReason")
    Clinicalresearchobservationreason = ActReason("_ClinicalResearchObservationReason")
    Combinedpharmacyordersuspendreasoncode = ActReason(
        "_CombinedPharmacyOrderSuspendReasonCode"
    )
    Controlactnullificationreasoncode = ActReason("_ControlActNullificationReasonCode")
    Controlactnullificationrefusalreasontype = ActReason(
        "_ControlActNullificationRefusalReasonType"
    )
    Controlactreason = ActReason("_ControlActReason")
    Genericupdatereasoncode = ActReason("_GenericUpdateReasonCode")
    PatientProfileQueryReason = ActReason("_PatientProfileQueryReasonCode")
    Pharmacysupplyrequestfulfillerrevisionrefusalreasoncode = ActReason(
        "_PharmacySupplyRequestFulfillerRevisionRefusalReasonCode"
    )
    Refusalreasoncode = ActReason("_RefusalReasonCode")
    Schedulingactreason = ActReason("_SchedulingActReason")
    Statusrevisionrefusalreasoncode = ActReason("_StatusRevisionRefusalReasonCode")
    Substanceadministrationpermissionrefusalreasoncode = ActReason(
        "_SubstanceAdministrationPermissionRefusalReasonCode"
    )
    Substanceadminsubstitutionnotallowedreason = ActReason(
        "_SubstanceAdminSubstitutionNotAllowedReason"
    )
    Substanceadminsubstitutionreason = ActReason("_SubstanceAdminSubstitutionReason")
    Transferactreason = ActReason("_TransferActReason")
    Actbillableservicereason = ActReason("_ActBillableServiceReason")
    Bonus = ActReason("BONUS")
    ChildrenOnly = ActReason("CHD")
    DependentsOnly = ActReason("DEP")
    EmployeeAndChildren = ActReason("ECH")
    Edu = ActReason("EDU")
    EmployeeOnly = ActReason("EMP")
    EmployeeAndSpouse = ActReason("ESP")
    Family = ActReason("FAM")
    Individual = ActReason("IND")
    Invoice = ActReason("INVOICE")
    Proa = ActReason("PROA")
    Recov = ActReason("RECOV")
    Retro = ActReason("RETRO")
    SpouseAndChildren = ActReason("SPC")
    SpouseOnly = ActReason("SPO")
    Tran = ActReason("TRAN")