from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_complex_type_base import FhirComplexTypeBase

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.contributor_type import ContributorType
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.contact_detail import ContactDetail


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class Contributor(FhirComplexTypeBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        type: ContributorType,
        name: string,
        contact: Optional[FhirList[ContactDetail]] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param type: The type of contributor.
            :param name: The name of the individual or organization responsible for the contribution.
            :param contact: Contact details to assist a user in finding and communicating with the
        contributor.
        """
        super().__init__(
            resourceType="Contributor",
            id_=id_,
            meta=meta,
            extension=extension,
            type=type,
            name=name,
            contact=contact,
        )