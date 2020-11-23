from typing import Optional

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.coverage import Coverage


class InsuranceBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        focal: FhirBoolean,
        coverage: Reference[Coverage],
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        preAuthRef: Optional[FhirList[FhirString]] = None
    ):
        """
        InsuranceBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#InsuranceBackboneElement
        Patient insurance information


        :param focal: Coverage to be used for adjudication
        :param coverage: Insurance information
        :param preAuthRef: 	Prior authorization reference number
        """
        super().__init__(
            id_=id_,
            extension=extension,
            focal=focal,
            coverage=coverage,
            preAuthRef=preAuthRef
        )
