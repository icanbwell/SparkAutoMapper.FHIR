from typing import Optional, Union

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.coverage_type_and_self_pay import FhirCoverageTypeAndSelfPayCode
from spark_auto_mapper_fhir.fhir_types.valuesets.financial_resource_status import FhirFinancialResourceStatusCode
from spark_auto_mapper_fhir.fhir_types.valuesets.subscriber_relationship import FhirSubscriberRelationshipCode
from spark_auto_mapper_fhir.fhir_types.contract import FhirContract
from spark_auto_mapper_fhir.fhir_types.cost_to_beneficiary_backbone_element import FhirCostToBeneficiaryBackboneElement
from spark_auto_mapper_fhir.fhir_types.coverage_classification_backbone_element import \
    FhirCoverageClassificationBackboneElement
from spark_auto_mapper_fhir.fhir_types.identifier import FhirIdentifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.related_person import FhirRelatedPerson
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirCoverage(FhirResourceBase):
    # noinspection SpellCheckingInspection,PyPep8Naming
    @classmethod
    def map(
        cls,
        status: FhirFinancialResourceStatusCode,
        payor: FhirList[FhirReference[Union[FhirOrganization, FhirPatient,
                                            FhirRelatedPerson]]],
        beneficiary: FhirReference[FhirPatient],
        identifier: Optional[FhirList[FhirIdentifier]] = None,
        type_: Optional[FhirCodeableConcept[FhirCoverageTypeAndSelfPayCode]
                        ] = None,
        policyHolder: Optional[FhirReference[Union[FhirPatient,
                                                   FhirRelatedPerson,
                                                   FhirOrganization]]] = None,
        subscriber: Optional[FhirReference[Union[FhirPatient,
                                                 FhirRelatedPerson]]] = None,
        subscriberId: Optional[FhirString] = None,
        dependent: Optional[FhirString] = None,
        relationship: Optional[
            FhirCodeableConcept[FhirSubscriberRelationshipCode]] = None,
        period: Optional[FhirPeriod] = None,
        class_: Optional[FhirList[FhirCoverageClassificationBackboneElement]
                         ] = None,
        order: Optional[FhirPositiveInt] = None,
        network: Optional[FhirString] = None,
        costToBeneficiary: Optional[
            FhirList[FhirCostToBeneficiaryBackboneElement]] = None,
        subrogation: Optional[FhirBoolean] = None,
        contract: Optional[FhirList[FhirReference[FhirContract]]] = None
    ) -> 'FhirCoverage':
        """
        Coverage Resource in FHIR
        https://hl7.org/FHIR/coverage.html
        Insurance or medical plan or a payment agreement


        :param status: active | cancelled | draft | entered-in-error. https://hl7.org/FHIR/valueset-fm-status.html
        :param payor: Issuer of the policy
        :param beneficiary: Plan beneficiary

        :param identifier: Business Identifier for the coverage
        :param type_: Coverage category such as medical or accident. https://hl7.org/FHIR/valueset-coverage-type.html
        :param policyHolder: Owner of the policy
        :param subscriber: Subscriber to the policy
        :param subscriberId: ID assigned to the subscriber
        :param dependent: Dependent number
        :param relationship: Beneficiary relationship to the subscriber.
                            https://hl7.org/FHIR/valueset-subscriber-relationship.html
        :param period: Coverage start and end dates
        :param class_: Additional coverage classifications
        :param order: Relative order of the coverage
        :param network: Insurer network
        :param costToBeneficiary: Patient payments for services/products
        :param subrogation: Reimbursement to insurer
        :param contract: Contract details
        """
        return FhirCoverage(
            status=status,
            payor=payor,
            beneficiary=beneficiary,
            identifier=identifier,
            type_=type_,
            policyHolder=policyHolder,
            subscriber=subscriber,
            subscriberId=subscriberId,
            dependent=dependent,
            relationship=relationship,
            period=period,
            class_=class_,
            order=order,
            network=network,
            costToBeneficiary=costToBeneficiary,
            subrogation=subrogation,
            contract=contract
        )
