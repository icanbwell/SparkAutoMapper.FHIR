from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.coverage import FhirCoverage
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirInsuranceBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        focal: FhirBoolean,
        coverage: FhirReference[FhirCoverage],
        preAuthRef: Optional[FhirList[FhirString]] = None
    ) -> 'FhirInsuranceBackboneElement':
        """
        InsuranceBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#InsuranceBackboneElement
        Patient insurance information


        :param focal: Coverage to be used for adjudication
        :param coverage: Insurance information
        :param preAuthRef: 	Prior authorization reference number
        """
        return FhirInsuranceBackboneElement(
            focal=focal, coverage=coverage, preAuthRef=preAuthRef
        )
