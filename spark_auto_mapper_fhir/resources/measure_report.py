from typing import Optional, Union, Any
from pyspark.sql.types import StructType, DataType
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.backbone_elements.group_backbone_element import (
    GroupBackboneElement,
)
from spark_auto_mapper_fhir.resources.organization import Organization

from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime

from spark_auto_mapper_fhir.resources.group import Group

from spark_auto_mapper_fhir.resources.related_person import RelatedPerson

from spark_auto_mapper_fhir.resources.device import Device

from spark_auto_mapper_fhir.resources.location import Location

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole

from spark_auto_mapper_fhir.resources.practitioner import Practitioner

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.fhir_types.uri import FhirCanonical
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_fhir_schemas.r4.resources.measurereport import MeasureReportSchema
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.valuesets.measure_improvement_notation import (
    MeasureImprovementNotationCode,
)
from spark_auto_mapper_fhir.valuesets.measure_report_status import (
    MeasureReportStatusCode,
)
from spark_auto_mapper_fhir.valuesets.measure_report_type import MeasureReportTypeCode


class MeasureReport(FhirResourceBase):
    def __init__(
        self,
        status: MeasureReportStatusCode,
        type_: MeasureReportTypeCode,
        measure: FhirCanonical,
        period: Period,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        subject: Optional[
            Reference[
                Union[
                    Practitioner,
                    PractitionerRole,
                    Location,
                    Device,
                    RelatedPerson,
                    Group,
                ]
            ]
        ] = None,
        date: Optional[FhirDateTime] = None,
        reporter: Optional[
            Reference[Union[Practitioner, PractitionerRole, Location, Organization]]
        ] = None,
        improvementNotation: Optional[
            CodeableConcept[MeasureImprovementNotationCode]
        ] = None,
        group: Optional[FhirList[GroupBackboneElement]] = None,
        evaluatedResource: Optional[FhirList[Reference[Any]]] = None,
        extension: Optional[FhirList[Extension]] = None,
    ) -> None:
        """
        MeasureReport Resource in FHIR
        https://www.hl7.org/fhir/measurereport.html

        :param id_: id of resource
        :param identifier: Additional identifier for the MeasureReport
        :param status: complete | pending | error
        :param type_: individual | subject-list | summary | data-collection
        :param measure: What measure was calculated
        :param subject: What individual(s) the report is for
        :param date: When the report was generated
        :param reporter: Who is reporting the data
        :param period: What period the report covers
        :param improvementNotation: increase | decrease
        :param group: Measure results from each group
        :param evaluatedResource: What data was used to calculate the measure score
        """
        super().__init__(
            resourceType="MeasureReport",
            id_=id_,
            meta=meta,
            identifier=identifier,
            status=status,
            type_=type_,
            measure=measure,
            subject=subject,
            date=date,
            reporter=reporter,
            period=period,
            improvementNotation=improvementNotation,
            group=group,
            evaluatedResource=evaluatedResource,
            extension=extension,
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return MeasureReportSchema.get_schema(include_extension=include_extension)
