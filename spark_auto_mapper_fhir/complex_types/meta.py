from typing import Optional

from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.complex_types.structure_definition import StructureDefinition

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.instant import FhirInstant
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_auto_mapper_fhir.valuesets.common_tags import CommonTagsCode
from spark_auto_mapper_fhir.valuesets.security_labels import SecurityLabelsCode


class Meta(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        versionId: Optional[FhirId] = None,
        lastUpdated: Optional[FhirInstant] = None,
        source: Optional[FhirUri] = None,
        profile: Optional[FhirList[StructureDefinition]] = None,
        security: Optional[FhirList[Coding[SecurityLabelsCode]]] = None,
        tag: Optional[FhirList[Coding[CommonTagsCode]]] = None,
    ) -> None:
        """
        Meta Complex Type in FHIR
        https://www.hl7.org/fhir/resource.html#Meta
        Metadata about a resource
        There are 3 different versions of interest for a resource:
            The Record Version: changes each time the resource changes (usually managed by a server)
            The Business version: changes each time the content in the resources changes (managed by a human author or
                by business policy)
            The FHIR Version: the version of FHIR in which the resource is represented (controlled by the author
                of the resource)


        :param versionId: Version specific identifier
        :param lastUpdated: When the resource version last changed
        :param source: 	Identifies where the resource comes from
        :param profile: Profiles this resource claims to conform to
        :param security: Security Labels applied to this resource
        :param tag: Tags applied to this resource
        """
        super().__init__(
            id_=id_,
            extension=extension,
            versionId=versionId,
            lastUpdated=lastUpdated,
            source=source,
            profile=profile,
            security=security,
            tag=tag
        )
