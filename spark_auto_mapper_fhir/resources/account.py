from typing import Optional, Union

from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.careplan import CarePlanSchema

from spark_auto_mapper_fhir.backbone_elements.coverage_backbone_element import (
    CoverageBackboneElement,
)
from spark_auto_mapper_fhir.backbone_elements.guarantor_backbone_element import (
    GuarantorBackboneElement,
)
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.device import Device
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.healthcare_service import HealthcareService
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.valuesets.account_status import AccountStatusCode
from spark_auto_mapper_fhir.valuesets.account_type import AccountTypeCode


class Account(FhirResourceBase):
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: AccountStatusCode,
        type_: Optional[CodeableConcept[AccountTypeCode]] = None,
        name: Optional[FhirString] = None,
        subject: Optional[
            FhirList[
                Reference[
                    Union[
                        Patient,
                        Device,
                        Practitioner,
                        PractitionerRole,
                        Location,
                        HealthcareService,
                        Organization,
                    ]
                ]
            ]
        ] = None,
        servicePeriod: Optional[Period] = None,
        coverage: Optional[FhirList[CoverageBackboneElement]] = None,
        owner: Optional[Reference[Organization]] = None,
        description: Optional[FhirString] = None,
        guarantor: Optional[FhirList[GuarantorBackboneElement]] = None,
        partOf: Optional[Reference["Account"]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        Account Resource in FHIR
        https://www.hl7.org/fhir/account.html


        :param id_: id of resource
        :param identifier: Account number
        :param status:
        :param type_:
        :param name:
        :param subject:
        :param servicePeriod:
        :param coverage:
        :param owner:
        :param description:
        :param guarantor:
        :param partOf:
        """
        super().__init__(
            resourceType="Account",
            id_=id_,
            meta=meta,
            identifier=identifier,
            status=status,
            type_=type_,
            name=name,
            subject=subject,
            servicePeriod=servicePeriod,
            coverage=coverage,
            owner=owner,
            description=description,
            guarantor=guarantor,
            partOf=partOf,
            extension=extension,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return CarePlanSchema.get_schema(include_extension=include_extension)
