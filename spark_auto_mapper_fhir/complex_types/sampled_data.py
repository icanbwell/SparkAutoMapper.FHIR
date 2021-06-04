from typing import Optional

from spark_auto_mapper_fhir.fhir_types.string import FhirString

from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

from spark_auto_mapper_fhir.complex_types.simple_quantity import SimpleQuantity

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import (
    FhirComplexTypeBase,
)


class SampledData(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        origin: SimpleQuantity,
        period: FhirDecimal,
        dimensions: FhirPositiveInt,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        factor: Optional[FhirDecimal] = None,
        lowerLimit: Optional[FhirDecimal] = None,
        upperLimit: Optional[FhirDecimal] = None,
        data: Optional[FhirString] = None,
    ) -> None:
        """
        SampledData Complex Type in FHIR
        https://www.hl7.org/fhir/datatypes.html#SampledData
        A series of measurements taken by a device


        :param origin: Zero value and units
        :param period: Number of milliseconds between samples
        :param factor: 	Multiply data by this before adding to origin
        :param lowerLimit: Lower limit of detection
        :param upperLimit: Upper limit of detection
        :param dimensions: Number of sample points at each time point
        :param data: Decimal values with spaces, or "E" | "U" | "L"
        """
        super().__init__(
            id_=id_,
            extension=extension,
            origin=origin,
            period=period,
            factor=factor,
            lowerLimit=lowerLimit,
            upperLimit=upperLimit,
            dimensions=dimensions,
            data=data,
        )
