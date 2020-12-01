from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.insuranceplan import InsurancePlanSchema

from spark_auto_mapper_fhir.backbone_elements.contact_backbone_element import ContactBackboneElement
from spark_auto_mapper_fhir.backbone_elements.insurance_plan_backbone_element import InsurancePlanBackboneElement
from spark_auto_mapper_fhir.backbone_elements.insurance_plan_coverage_backbone_element import \
    InsurancePlanCoverageBackboneElement
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.endpoint import Endpoint
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.insurance_plan_type import InsurancePlanTypeCode
from spark_auto_mapper_fhir.valuesets.publication_status import PublicationStatusCode


class InsurancePlan(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: Optional[PublicationStatusCode] = None,
        type_: Optional[CodeableConcept[InsurancePlanTypeCode]] = None,
        name: Optional[FhirString] = None,
        alias: Optional[FhirList[FhirString]] = None,
        period: Optional[Period] = None,
        ownedBy: Optional[Reference[Organization]] = None,
        administeredBy: Optional[Reference[Organization]] = None,
        coverageArea: Optional[FhirList[Reference[Location]]] = None,
        contact: Optional[FhirList[ContactBackboneElement]] = None,
        endpoint: Optional[FhirList[Reference[Endpoint]]] = None,
        network: Optional[FhirList[Reference[Organization]]] = None,
        coverage: Optional[FhirList[InsurancePlanCoverageBackboneElement]
                           ] = None,
        plan: Optional[FhirList[InsurancePlanBackboneElement]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        InsurancePlan Resource in FHIR
        https://www.hl7.org/fhir/insuranceplan.html
        Details of a Health Insurance product/plan provided by an organization
        + Rule: The organization SHALL at least have a name or an identifier, and possibly more than one

        :param id_: id of resource
        :param identifier: Business Identifier for Product
        :param status: 	draft | active | retired | unknown
        :param type_: Kind of product
        :param name: Official name
        :param alias: Alternate names
        :param period: When the product is available
        :param ownedBy: Plan issuer
        :param administeredBy: Product administrator
        :param coverageArea: Where product applies
        :param contact: Contact for the product
        :param endpoint: Technical endpoint
        :param network: What networks are Included
        :param coverage: Coverage details
        :param plan: Plan details
        """
        super().__init__(
            resourceType="InsurancePlan",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            type_=type_,
            name=name,
            alias=alias,
            period=period,
            ownedBy=ownedBy,
            administeredBy=administeredBy,
            coverageArea=coverageArea,
            contact=contact,
            endpoint=endpoint,
            network=network,
            coverage=coverage,
            plan=plan,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return InsurancePlanSchema.get_schema(
            include_extension=include_extension
        )
