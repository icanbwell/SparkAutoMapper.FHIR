from typing import Optional, TypeVar, Generic

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

_T = TypeVar("_T")


class FhirCoding(Generic[_T], FhirResourceBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(
        cls,
        system: Optional[FhirUri] = None,
        version: Optional[FhirString] = None,
        code: Optional[_T] = None,
        display: Optional[FhirString] = None,
        userSelected: Optional[FhirBoolean] = None
    ) -> 'FhirCoding[_T]':
        """
        Coding Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Coding


        :param system: Identity of the terminology system
        :param version: Version of the system - if relevant
        :param code: 	Symbol in syntax defined by the system
        :param display: Representation defined by the system
        :param userSelected: If this coding was chosen directly by the user
        """
        return FhirCoding[_T](
            system=system,
            version=version,
            code=code,
            display=display,
            userSelected=userSelected
        )
