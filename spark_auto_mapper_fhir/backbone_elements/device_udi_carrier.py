from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.complex_types.uri import uri
    from spark_auto_mapper_fhir.complex_types.base64_binary import base64Binary
    from spark_auto_mapper_fhir.complex_types.string import string
    from spark_auto_mapper_fhir.complex_types.udi_entry_type import UDIEntryType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class DeviceUdiCarrier(FhirBackboneElementBase):
    """ """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: FhirId,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        deviceIdentifier: Optional[string] = None,
        issuer: Optional[uri] = None,
        jurisdiction: Optional[uri] = None,
        carrierAIDC: Optional[base64Binary] = None,
        carrierHRF: Optional[string] = None,
        entryType: Optional[UDIEntryType] = None,
    ) -> None:
        """

            :param id_: id of resource
            :param meta: Meta
            :param extension: extensions
            :param deviceIdentifier: The device identifier (DI) is a mandatory, fixed portion of a UDI that
        identifies the labeler and the specific version or model of a device.
            :param issuer: Organization that is charged with issuing UDIs for devices.  For example, the
        US FDA issuers include :
        1) GS1:
        http://hl7.org/fhir/NamingSystem/gs1-di,
        2) HIBCC:
        http://hl7.org/fhir/NamingSystem/hibcc-dI,
        3) ICCBBA for blood containers:
        http://hl7.org/fhir/NamingSystem/iccbba-blood-di,
        4) ICCBA for other devices:
        http://hl7.org/fhir/NamingSystem/iccbba-other-di.
            :param jurisdiction: The identity of the authoritative source for UDI generation within a
        jurisdiction.  All UDIs are globally unique within a single namespace with the
        appropriate repository uri as the system.  For example,  UDIs of devices
        managed in the U.S. by the FDA, the value is
        http://hl7.org/fhir/NamingSystem/fda-udi.
            :param carrierAIDC: The full UDI carrier of the Automatic Identification and Data Capture (AIDC)
        technology representation of the barcode string as printed on the packaging of
        the device - e.g., a barcode or RFID.   Because of limitations on character
        sets in XML and the need to round-trip JSON data through XML, AIDC Formats
        *SHALL* be base64 encoded.
            :param carrierHRF: The full UDI carrier as the human readable form (HRF) representation of the
        barcode string as printed on the packaging of the device.
            :param entryType: A coded entry to indicate how the data was entered.
        """
        super().__init__(
            resourceType="DeviceUdiCarrier",
            id_=id_,
            meta=meta,
            extension=extension,
            deviceIdentifier=deviceIdentifier,
            issuer=issuer,
            jurisdiction=jurisdiction,
            carrierAIDC=carrierAIDC,
            carrierHRF=carrierHRF,
            entryType=entryType,
        )