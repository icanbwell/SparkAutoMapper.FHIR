from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.identifier_type import IdentifierTypeCode
from spark_auto_mapper_fhir.valuesets.identifier_use import IdentifierUseCode
from spark_auto_mapper_fhir.complex_types.period import Period
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class Identifier(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        use: Optional[IdentifierUseCode] = None,
        type_: Optional[CodeableConcept[IdentifierTypeCode]] = None,
        system: Optional[FhirUri] = None,
        value: Optional[FhirString] = None,
        period: Optional[Period] = None,
        assigner: Optional[FhirResourceBase] = None
        # should be FhirReference[FhirOrganization] but this is causing circular import
    ):
        """
        Identifier Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Identifier
        An identifier intended for computation


        :param use: usual | official | temp | secondary | old (If known)
                    (https://hl7.org/FHIR/valueset-identifier-use.html)
        :param type_: Description of identifier https://hl7.org/FHIR/valueset-identifier-type.html
        :param system: 	The namespace for the identifier value
        :param value: The value that is unique
        :param period: Time period when id is/was valid for use
        :param assigner: Organization that issued id (may be just text)
        """
        super().__init__(
            id_=id_,
            extension=extension,
            use=use,
            type_=type_,
            system=system,
            value=value,
            period=period,
            assigner=assigner
        )

    use = A.column("use")
    type_ = A.column("type")
    system = A.column("system")
    # value = A.column("value")
    period = A.column("period")
    assigner = A.column("assigner")
