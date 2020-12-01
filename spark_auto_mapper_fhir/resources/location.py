from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.location import LocationSchema

from spark_auto_mapper_fhir.backbone_elements.hours_of_operation_backbone_element import HoursOfOperationBackboneElement
from spark_auto_mapper_fhir.backbone_elements.position_backbone_element import PositionBackboneElement
from spark_auto_mapper_fhir.complex_types.address import Address
from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.coding import Coding
from spark_auto_mapper_fhir.complex_types.contact_point import ContactPoint
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.complex_types.reference import Reference
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.resources.endpoint import Endpoint
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.valuesets.bed_status import BedStatusCode
from spark_auto_mapper_fhir.valuesets.location_mode import LocationModeCode
from spark_auto_mapper_fhir.valuesets.location_status import LocationStatusCode
from spark_auto_mapper_fhir.valuesets.location_type import LocationTypeCode
from spark_auto_mapper_fhir.valuesets.service_delivery_location_type import ServiceDeliveryLocationTypeCode


class Location(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        status: Optional[LocationStatusCode] = None,
        operationalStatus: Optional[Coding[BedStatusCode]] = None,
        name: Optional[FhirString] = None,
        alias: Optional[FhirList[FhirString]] = None,
        description: Optional[FhirString] = None,
        mode: Optional[LocationModeCode] = None,
        type_: Optional[FhirList[
            CodeableConcept[ServiceDeliveryLocationTypeCode]]] = None,
        telecom: Optional[FhirList[ContactPoint]] = None,
        address: Optional[Address] = None,
        physicalType: Optional[CodeableConcept[LocationTypeCode]] = None,
        position: Optional[PositionBackboneElement] = None,
        managingOrganization: Optional[Reference[Organization]] = None,
        partOf: Optional[Reference['Location']] = None,
        hoursOfOperation: Optional[FhirList[HoursOfOperationBackboneElement]
                                   ] = None,
        availabilityExceptions: Optional[FhirString] = None,
        endpoint: Optional[FhirList[Reference[Endpoint]]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ):
        """
        Location Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Location
        Details and position information for a physical place


        :param id_: id of resource
        :param identifier: Unique code or number identifying the location to its users
        :param status: active | suspended | inactive
        :param operationalStatus: The operational status of the location (typically only for a bed/room)
        :param name: Name of the location as used by humans
        :param alias: A list of alternate names that the location is known as, or was known as, in the past
        :param description: Additional details about the location that could be displayed as further information
                            to identify the location beyond its name
        :param mode: instance | kind
        :param type_: Type of function performed
        :param telecom: Contact details of the location
        :param address: Physical location
        :param physicalType: Physical form of the location
        :param position: The absolute geographic location
        :param managingOrganization: Organization responsible for provisioning and upkeep
        :param partOf: Another Location this one is physically a part of
        :param hoursOfOperation: What days/times during a week is this location usually open
        :param availabilityExceptions: Description of availability exceptions
        :param endpoint: Technical endpoints providing access to services operated for the location
        """
        super().__init__(
            resourceType="Location",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            status=status,
            operationalStatus=operationalStatus,
            name=name,
            alias=alias,
            description=description,
            mode=mode,
            type_=type_,
            telecom=telecom,
            address=address,
            physicalType=physicalType,
            position=position,
            managingOrganization=managingOrganization,
            partOf=partOf,
            hoursOfOperation=hoursOfOperation,
            availabilityExceptions=availabilityExceptions,
            endpoint=endpoint,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return LocationSchema.get_schema(include_extension=include_extension)
