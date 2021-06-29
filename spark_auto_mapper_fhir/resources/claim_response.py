from __future__ import annotations
from typing import Optional, TYPE_CHECKING, Union

# noinspection PyPackageRequirements
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_resource_base import FhirResourceBase
from spark_fhir_schemas.r4.resources.claimresponse import ClaimResponseSchema

if TYPE_CHECKING:
    pass
    # identifier (Identifier)
    from spark_auto_mapper_fhir.complex_types.identifier import Identifier

    # status (FinancialResourceStatusCodes)
    from spark_auto_mapper_fhir.value_sets.financial_resource_status_codes import (
        FinancialResourceStatusCodesCode,
    )

    # type_ (CodeableConcept)
    from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

    # Import for CodeableConcept for type_
    from spark_auto_mapper_fhir.value_sets.claim_type_codes import ClaimTypeCodesCode

    # End Import for CodeableConcept for type_
    # subType (CodeableConcept)
    # Import for CodeableConcept for subType
    from spark_auto_mapper_fhir.value_sets.example_claim_sub_type_codes import (
        ExampleClaimSubTypeCodesCode,
    )

    # End Import for CodeableConcept for subType
    # use (Use)
    from spark_auto_mapper_fhir.value_sets.use import UseCode

    # patient (Reference)
    from spark_auto_mapper_fhir.complex_types.reference import Reference

    # Imports for References for patient
    from spark_auto_mapper_fhir.resources.patient import Patient

    # created (dateTime)
    # insurer (Reference)
    # Imports for References for insurer
    from spark_auto_mapper_fhir.resources.organization import Organization

    # requestor (Reference)
    # Imports for References for requestor
    from spark_auto_mapper_fhir.resources.practitioner import Practitioner
    from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

    # request (Reference)
    # Imports for References for request
    from spark_auto_mapper_fhir.resources.claim import Claim

    # outcome (ClaimProcessingCodes)
    from spark_auto_mapper_fhir.value_sets.claim_processing_codes import (
        ClaimProcessingCodesCode,
    )

    # disposition (string)
    # preAuthRef (string)
    # preAuthPeriod (Period)
    from spark_auto_mapper_fhir.complex_types.period import Period

    # payeeType (CodeableConcept)
    # Import for CodeableConcept for payeeType
    from spark_auto_mapper_fhir.value_sets.claim_payee_type_codes import (
        ClaimPayeeTypeCodesCode,
    )

    # End Import for CodeableConcept for payeeType
    # item (ClaimResponse.Item)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_item import (
        ClaimResponseItem,
    )

    # addItem (ClaimResponse.AddItem)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_add_item import (
        ClaimResponseAddItem,
    )

    # adjudication (ClaimResponse.Adjudication)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_adjudication import (
        ClaimResponseAdjudication,
    )

    # total (ClaimResponse.Total)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_total import (
        ClaimResponseTotal,
    )

    # payment (ClaimResponse.Payment)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_payment import (
        ClaimResponsePayment,
    )

    # fundsReserve (CodeableConcept)
    # Import for CodeableConcept for fundsReserve
    from spark_auto_mapper_fhir.value_sets.funds_reservation_codes import (
        FundsReservationCodesCode,
    )

    # End Import for CodeableConcept for fundsReserve
    # formCode (CodeableConcept)
    # Import for CodeableConcept for formCode
    from spark_auto_mapper_fhir.value_sets.form_codes import FormCodesCode

    # End Import for CodeableConcept for formCode
    # form (Attachment)
    from spark_auto_mapper_fhir.complex_types.attachment import Attachment

    # processNote (ClaimResponse.ProcessNote)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_process_note import (
        ClaimResponseProcessNote,
    )

    # communicationRequest (Reference)
    # Imports for References for communicationRequest
    from spark_auto_mapper_fhir.resources.communication_request import (
        CommunicationRequest,
    )

    # insurance (ClaimResponse.Insurance)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_insurance import (
        ClaimResponseInsurance,
    )

    # error (ClaimResponse.Error)
    from spark_auto_mapper_fhir.backbone_elements.claim_response_error import (
        ClaimResponseError,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ClaimResponse(FhirResourceBase):
    """
    ClaimResponse
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: FinancialResourceStatusCodesCode,
        type_: CodeableConcept[ClaimTypeCodesCode],
        subType: Optional[CodeableConcept[ExampleClaimSubTypeCodesCode]] = None,
        use: UseCode,
        patient: Reference[Union[Patient]],
        created: FhirDateTime,
        insurer: Reference[Union[Organization]],
        requestor: Optional[
            Reference[Union[Practitioner, PractitionerRole, Organization]]
        ] = None,
        request: Optional[Reference[Union[Claim]]] = None,
        outcome: ClaimProcessingCodesCode,
        disposition: Optional[FhirString] = None,
        preAuthRef: Optional[FhirString] = None,
        preAuthPeriod: Optional[Period] = None,
        payeeType: Optional[CodeableConcept[ClaimPayeeTypeCodesCode]] = None,
        item: Optional[FhirList[ClaimResponseItem]] = None,
        addItem: Optional[FhirList[ClaimResponseAddItem]] = None,
        adjudication: Optional[FhirList[ClaimResponseAdjudication]] = None,
        total: Optional[FhirList[ClaimResponseTotal]] = None,
        payment: Optional[ClaimResponsePayment] = None,
        fundsReserve: Optional[CodeableConcept[FundsReservationCodesCode]] = None,
        formCode: Optional[CodeableConcept[FormCodesCode]] = None,
        form: Optional[Attachment] = None,
        processNote: Optional[FhirList[ClaimResponseProcessNote]] = None,
        communicationRequest: Optional[
            FhirList[Reference[Union[CommunicationRequest]]]
        ] = None,
        insurance: Optional[FhirList[ClaimResponseInsurance]] = None,
        error: Optional[FhirList[ClaimResponseError]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param identifier: A unique identifier assigned to this claim response.
            :param status: The status of the resource instance.
            :param type_: A finer grained suite of claim type codes which may convey additional
        information such as Inpatient vs Outpatient and/or a specialty service.
            :param subType: A finer grained suite of claim type codes which may convey additional
        information such as Inpatient vs Outpatient and/or a specialty service.
            :param use: A code to indicate whether the nature of the request is: to request
        adjudication of products and services previously rendered; or requesting
        authorization and adjudication for provision in the future; or requesting the
        non-binding adjudication of the listed products and services which could be
        provided in the future.
            :param patient: The party to whom the professional services and/or products have been supplied
        or are being considered and for whom actual for facast reimbursement is
        sought.
            :param created: The date this resource was created.
            :param insurer: The party responsible for authorization, adjudication and reimbursement.
            :param requestor: The provider which is responsible for the claim, predetermination or
        preauthorization.
            :param request: Original request resource reference.
            :param outcome: The outcome of the claim, predetermination, or preauthorization processing.
            :param disposition: A human readable description of the status of the adjudication.
            :param preAuthRef: Reference from the Insurer which is used in later communications which refers
        to this adjudication.
            :param preAuthPeriod: The time frame during which this authorization is effective.
            :param payeeType: Type of Party to be reimbursed: subscriber, provider, other.
            :param item: A claim line. Either a simple (a product or service) or a 'group' of details
        which can also be a simple items or groups of sub-details.
            :param addItem: The first-tier service adjudications for payor added product or service lines.
            :param adjudication: The adjudication results which are presented at the header level rather than
        at the line-item or add-item levels.
            :param total: Categorized monetary totals for the adjudication.
            :param payment: Payment details for the adjudication of the claim.
            :param fundsReserve: A code, used only on a response to a preauthorization, to indicate whether the
        benefits payable have been reserved and for whom.
            :param formCode: A code for the form to be used for printing the content.
            :param form: The actual form, by reference or inclusion, for printing the content or an
        EOB.
            :param processNote: A note that describes or explains adjudication results in a human readable
        form.
            :param communicationRequest: Request for additional supporting or authorizing information.
            :param insurance: Financial instruments for reimbursement for the health care products and
        services specified on the claim.
            :param error: Errors encountered during the processing of the adjudication.
        """
        super().__init__(
            resourceType="ClaimResponse",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            type_=type_,
            subType=subType,
            use=use,
            patient=patient,
            created=created,
            insurer=insurer,
            requestor=requestor,
            request=request,
            outcome=outcome,
            disposition=disposition,
            preAuthRef=preAuthRef,
            preAuthPeriod=preAuthPeriod,
            payeeType=payeeType,
            item=item,
            addItem=addItem,
            adjudication=adjudication,
            total=total,
            payment=payment,
            fundsReserve=fundsReserve,
            formCode=formCode,
            form=form,
            processNote=processNote,
            communicationRequest=communicationRequest,
            insurance=insurance,
            error=error,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return ClaimResponseSchema.get_schema(include_extension=include_extension)
