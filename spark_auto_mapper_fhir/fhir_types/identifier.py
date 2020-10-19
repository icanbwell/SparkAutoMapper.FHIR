from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.identifier_type import FhirIdentifierTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.identifier_use import FhirIdentifierUseCode
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class FhirIdentifier(FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        use: Optional[FhirIdentifierUseCode] = None,
        type_: Optional[FhirCodeableConcept[FhirIdentifierTypeCode]] = None,
        system: Optional[FhirUri] = None,
        value: Optional[FhirString] = None,
        period: Optional[FhirPeriod] = None,
        assigner: Optional[FhirResourceBase] = None
        # should be FhirReference[FhirOrganization] but this is causing circular import
    ) -> 'FhirIdentifier':
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
        return FhirIdentifier(
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
