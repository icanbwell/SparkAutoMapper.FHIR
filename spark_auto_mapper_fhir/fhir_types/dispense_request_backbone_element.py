from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.duration import FhirDuration
from spark_auto_mapper_fhir.fhir_types.fill import FhirFill
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference
from spark_auto_mapper_fhir.fhir_types.simple_quantity import FhirSimpleQuantity
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt


class FhirDispenseRequestBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        initialFill: Optional[FhirFill] = None,
        dispenseInterval: Optional[FhirDuration] = None,
        validityPeriod: Optional[FhirPeriod] = None,
        numberOfRepeatsAllowed: Optional[FhirUnsignedInt] = None,
        quantity: Optional[FhirSimpleQuantity] = None,
        expectedSupplyDuration: Optional[FhirDuration] = None,
        performer: Optional[FhirReference[FhirOrganization]] = None
    ) -> 'FhirDispenseRequestBackboneElement':
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
        return FhirDispenseRequestBackboneElement(
            initialFill=initialFill,
            dispenseInterval=dispenseInterval,
            validityPeriod=validityPeriod,
            numberOfRepeatsAllowed=numberOfRepeatsAllowed,
            quantity=quantity,
            expectedSupplyDuration=expectedSupplyDuration,
            performer=performer
        )
