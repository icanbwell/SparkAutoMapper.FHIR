from typing import Optional
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

from spark_auto_mapper_fhir.complex_types.duration import Duration
from spark_auto_mapper_fhir.complex_types.fill import Fill
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt


class DispenseRequestBackboneElement(FhirBackboneElementBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        initialFill: Optional[Fill] = None,
        dispenseInterval: Optional[Duration] = None,
        validityPeriod: Optional[Period] = None,
        numberOfRepeatsAllowed: Optional[FhirUnsignedInt] = None,
        quantity: Optional[SimpleQuantity] = None,
        expectedSupplyDuration: Optional[Duration] = None,
        performer: Optional[Reference[Organization]] = None,
    ):
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
        super().__init__(
            id_=id_,
            extension=extension,
            initialFill=initialFill,
            dispenseInterval=dispenseInterval,
            validityPeriod=validityPeriod,
            numberOfRepeatsAllowed=numberOfRepeatsAllowed,
            quantity=quantity,
            expectedSupplyDuration=expectedSupplyDuration,
            performer=performer,
        )
