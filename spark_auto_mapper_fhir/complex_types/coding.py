from typing import Optional, TypeVar, Generic, Union

from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase

_T = TypeVar("_T", bound=Union[FhirValueSetBase])


class Coding(FhirComplexTypeBase, Generic[_T]):
    # noinspection PyPep8Naming
    def __init__(
        self,
        system: Optional[FhirUri] = None,
        version: Optional[FhirString] = None,
        code: Optional[_T] = None,
        display: Optional[FhirString] = None,
        userSelected: Optional[FhirBoolean] = None
    ):
        """
        Coding Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Coding


        :param system: Identity of the terminology system
        :param version: Version of the system - if relevant
        :param code: 	Symbol in syntax defined by the system
        :param display: Representation defined by the system
        :param userSelected: If this coding was chosen directly by the user
        """
        super().__init__(
            system=system,
            version=version,
            code=code,
            display=display,
            userSelected=userSelected
        )
