from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import FhirBackboneElementBase
from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal


class PositionBackboneElement(FhirBackboneElementBase):
    def __init__(
        self, longitude: FhirDecimal, latitude: FhirDecimal,
        altitude: FhirDecimal
    ) -> None:
        """
        PositionBackboneElement Backbone Element in FHIR
        https://hl7.org/FHIR/location-definitions.html#Location.position
        The absolute geographic location

        :param longitude: Longitude with WGS84 datum
        :param latitude: Latitude with WGS84 datum
        :param altitude: Altitude with WGS84 datum
        """
        super().__init__(
            longitude=longitude, latitude=longitude, altitude=altitude
        )
