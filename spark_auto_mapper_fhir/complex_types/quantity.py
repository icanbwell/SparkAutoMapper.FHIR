from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)

from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper_fhir.valuesets.quantity_comparator import QuantityComparatorCode


class Quantity(FhirComplexTypeBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        value: Optional[FhirDecimal] = None,
        comparator: Optional[QuantityComparatorCode] = None,
        unit: Optional[FhirString] = None,
        system: Optional[FhirUri] = None,
        code: Optional[FhirValueSetBase] = None,
    ):
        """
        Quantity Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#quantity


        :param value: Numerical value (with implicit precision)
        :param comparator: < | <= | >= | > - how to understand the value.
                            https://hl7.org/FHIR/valueset-quantity-comparator.html
        :param unit: Unit representation
        :param system: System that defines coded unit form
        :param code: Coded form of the unit
        """
        super().__init__(
            id_=id_,
            extension=extension,
            value=value,
            comparator=comparator,
            unit=unit,
            system=system,
            code=code,
        )
