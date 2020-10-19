from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.address import Address
from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.accident_incident import AccidentIncidentCode
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.resources.location import Location
from spark_auto_mapper_fhir.resources.reference import Reference


class AccidentBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        date: Optional[FhirDate] = None,
        type_: Optional[CodeableConcept[AccidentIncidentCode]] = None,
        locationAddress: Optional[Address] = None,
        locationReference: Optional[Reference[Location]] = None
    ) -> None:
        """
        AccidentBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.accident
        Details of the event

        :param date: When the incident occurred
        :param type_: The nature of the accident.  https://hl7.org/FHIR/v3/ActIncidentCode/vs.html
        :param locationAddress: Where the event occurred
        :param locationReference: Where the event occurred
        """
        super().__init__(
            date=date,
            type_=type_,
            locationAddress=locationAddress,
            locationReference=locationReference
        )
