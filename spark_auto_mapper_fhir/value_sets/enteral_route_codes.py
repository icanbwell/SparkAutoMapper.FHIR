from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class EnteralRouteCodes(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class EnteralRouteCodesValues:
    Routebymethod = EnteralRouteCodes("_RouteByMethod")
    Routebysite = EnteralRouteCodes("_RouteBySite")
    PO = EnteralRouteCodes("PO")
    EFT = EnteralRouteCodes("EFT")
    ENTINSTL = EnteralRouteCodes("ENTINSTL")
    GT = EnteralRouteCodes("GT")
    NGT = EnteralRouteCodes("NGT")
    OGT = EnteralRouteCodes("OGT")
    GJT = EnteralRouteCodes("GJT")
    JJTINSTL = EnteralRouteCodes("JJTINSTL")
    OJJ = EnteralRouteCodes("OJJ")