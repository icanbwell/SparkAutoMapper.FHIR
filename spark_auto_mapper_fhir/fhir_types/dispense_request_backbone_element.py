from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.duration import AutoMapperFhirDataTypeDuration
from spark_auto_mapper_fhir.fhir_types.fill import AutoMapperFhirDataTypeFill
from spark_auto_mapper_fhir.fhir_types.organization import AutoMapperFhirDataTypeOrganization
from spark_auto_mapper_fhir.fhir_types.period import AutoMapperFhirDataTypePeriod
from spark_auto_mapper_fhir.fhir_types.reference import AutoMapperFhirDataTypeReference
from spark_auto_mapper_fhir.fhir_types.simple_quantity import AutoMapperFhirDataTypeSimpleQuantity
from spark_auto_mapper_fhir.fhir_types.unsigned_int import AutoMapperFhirUnsignedIntInputType


class AutoMapperFhirDataTypeDispenseRequestBackboneElement(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            initialFill: Optional[AutoMapperFhirDataTypeFill] = None,
            dispenseInterval: Optional[AutoMapperFhirDataTypeDuration] = None,
            validityPeriod: Optional[AutoMapperFhirDataTypePeriod] = None,
            numberOfRepeatsAllowed: Optional[AutoMapperFhirUnsignedIntInputType] = None,
            quantity: Optional[AutoMapperFhirDataTypeSimpleQuantity] = None,
            expectedSupplyDuration: Optional[AutoMapperFhirDataTypeDuration] = None,
            performer: Optional[AutoMapperFhirDataTypeReference[AutoMapperFhirDataTypeOrganization]] = None
            ) -> 'AutoMapperFhirDataTypeDispenseRequestBackboneElement':
        """
        DispenseRequestBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DispenseRequestBackboneElement
        Medication supply authorization

        :param initialFill: First fill details
        :param dispenseInterval: Minimum period of time between dispenses
        :param validityPeriod: Time period supply is authorized for
        :param numberOfRepeatsAllowed: Number of refills authorized
        :param quantity: Amount of medication to supply per dispense
        :param expectedSupplyDuration: Number of days supply per dispense
        :param performer: Intended dispenser
        """
        return AutoMapperFhirDataTypeDispenseRequestBackboneElement(
            initialFill=initialFill,
            dispenseInterval=dispenseInterval,
            validityPeriod=validityPeriod,
            numberOfRepeatsAllowed=numberOfRepeatsAllowed,
            quantity=quantity,
            expectedSupplyDuration=expectedSupplyDuration,
            performer=performer
        )
