from typing import Optional

from spark_auto_mapper_fhir.complex_types.sort import Sort
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

from spark_auto_mapper_fhir.complex_types.date_filter import DateFilter
from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.resources.group import Group

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept

from spark_auto_mapper_fhir.complex_types.code_filter import CodeFilter
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)
from spark_auto_mapper_fhir.fhir_types.uri import FhirCanonical
from spark_auto_mapper_fhir.valuesets.all_types import FhirAllTypesCode
from spark_auto_mapper_fhir.valuesets.subject_type import SubjectTypeCode


class DataRequirement(FhirComplexTypeBase):
    def __init__(
        self,
        type_: FhirAllTypesCode,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        profile: Optional[FhirList[FhirCanonical]] = None,
        subjectCodeableConcept: Optional[CodeableConcept[SubjectTypeCode]] = None,
        subjectReference: Optional[Reference[Group]] = None,
        mustSupport: Optional[FhirList[FhirString]] = None,
        code_filter: Optional[FhirList[CodeFilter]] = None,
        date_filter: Optional[FhirList[DateFilter]] = None,
        limit: Optional[FhirPositiveInt] = None,
        sort: Optional[FhirList[Sort]] = None,
    ) -> None:
        """
        DataRequirement Complex Type in FHIR
        https://www.hl7.org/fhir/metadatatypes.html#DataRequirement
        Describes a required data item


        :param type_: The type of the required data
        :param profile: The profile of the required data
        :param subjectCodeableConcept: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
        :param subjectReference: E.g. Patient, Practitioner, RelatedPerson, Organization, Location, Device
        :param mustSupport: Indicates specific structure elements that are referenced by the knowledge module
        :param code_filter: What codes are expected
                            + Rule: Either a path or a searchParam must be provided, but not both
        :param date_filter: What dates/date ranges are expected
                            + Rule: Either a path or a searchParam must be provided, but not both
        :param limit: Number of results
        :param sort: Order of the results
        """
        super().__init__(
            id_=id_,
            extension=extension,
            type_=type_,
            profile=profile,
            subjectCodeableConcept=subjectCodeableConcept,
            subjectReference=subjectReference,
            mustSupport=mustSupport,
            code_filter=code_filter,
            date_filter=date_filter,
            limit=limit,
            sort=sort,
        )
