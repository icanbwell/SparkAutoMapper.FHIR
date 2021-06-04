from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.coverage import CoverageSchema

from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.coverage_type_and_self_pay import (
    CoverageTypeAndSelfPayCode,
)
from spark_auto_mapper_fhir.valuesets.financial_resource_status import (
    FinancialResourceStatusCode,
)
from spark_auto_mapper_fhir.valuesets.subscriber_relationship import (
    SubscriberRelationshipCode,
)
from spark_auto_mapper_fhir.resources.contract import Contract
from spark_auto_mapper_fhir.backbone_elements.cost_to_beneficiary_backbone_element import (
    CostToBeneficiaryBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.coverage_classification_backbone_element import (
    CoverageClassificationBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class Coverage(FhirResourceBase):
    # noinspection SpellCheckingInspection,PyPep8Naming
    def __init__(
        self,
        status: FinancialResourceStatusCode,
        payor: FhirList[Reference[Union[Organization, Patient, RelatedPerson]]],
        beneficiary: Reference[Patient],
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        type_: Optional[CodeableConcept[CoverageTypeAndSelfPayCode]] = None,
        policyHolder: Optional[
            Reference[Union[Patient, RelatedPerson, Organization]]
        ] = None,
        subscriber: Optional[Reference[Union[Patient, RelatedPerson]]] = None,
        subscriberId: Optional[FhirString] = None,
        dependent: Optional[FhirString] = None,
        relationship: Optional[CodeableConcept[SubscriberRelationshipCode]] = None,
        period: Optional[Period] = None,
        class_: Optional[FhirList[CoverageClassificationBackboneElement]] = None,
        order: Optional[FhirPositiveInt] = None,
        network: Optional[FhirString] = None,
        costToBeneficiary: Optional[FhirList[CostToBeneficiaryBackboneElement]] = None,
        subrogation: Optional[FhirBoolean] = None,
        contract: Optional[FhirList[Reference[Contract]]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ):
        """
        Coverage Resource in FHIR
        https://hl7.org/FHIR/coverage.html
        Insurance or medical plan or a payment agreement


        :param status: active | cancelled | draft | entered-in-error. https://hl7.org/FHIR/valueset-fm-status.html
        :param payor: Issuer of the policy
        :param beneficiary: Plan beneficiary

        :param id_: id of resource
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
        super().__init__(
            resourceType="Coverage",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            type_=type_,
            policyHolder=policyHolder,
            subscriber=subscriber,
            subscriberId=subscriberId,
            beneficiary=beneficiary,
            dependent=dependent,
            relationship=relationship,
            period=period,
            payor=payor,
            class_=class_,
            order=order,
            network=network,
            costToBeneficiary=costToBeneficiary,
            subrogation=subrogation,
            contract=contract,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return CoverageSchema.get_schema(include_extension=include_extension)
