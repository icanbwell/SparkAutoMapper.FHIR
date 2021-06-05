from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class OrganizationAffiliationRoleCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-organization-role.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "OrganizationAffiliationRoleCode"]) -> None:
            self.f: Callable[..., "OrganizationAffiliationRoleCode"] = f

        def __get__(
            self, obj: Any, owner: Type["OrganizationAffiliationRoleCode"]
        ) -> "OrganizationAffiliationRoleCode":
            return self.f(owner)

    @classproperty
    def Provider(cls) -> "OrganizationAffiliationRoleCode":
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return OrganizationAffiliationRoleCode("provider")

    @classproperty
    def Agency(cls) -> "OrganizationAffiliationRoleCode":
        """
        An organization such as a public health agency, community/social services provider, etc.
        """
        # noinspection PyCallingNonCallable
        return OrganizationAffiliationRoleCode("agency")

    @classproperty
    def Research(cls) -> "OrganizationAffiliationRoleCode":
        """
        An organization providing research-related services such as conducting research, recruiting research participants, analyzing data, etc.
        """
        # noinspection PyCallingNonCallable
        return OrganizationAffiliationRoleCode("research")

    @classproperty
    def Payer(cls) -> "OrganizationAffiliationRoleCode":
        """
        An organization providing reimbursement, payment, or related services
        """
        # noinspection PyCallingNonCallable
        return OrganizationAffiliationRoleCode("payer")

    @classproperty
    def Diagnostics(cls) -> "OrganizationAffiliationRoleCode":
        """
        An organization providing diagnostic testing/laboratory services
        """
        # noinspection PyCallingNonCallable
        return OrganizationAffiliationRoleCode("diagnostics")

    @classproperty
    def Supplier(cls) -> "OrganizationAffiliationRoleCode":
        """
        An organization that provides medical supplies (e.g. medical devices, equipment, pharmaceutical products, etc.)
        """
        # noinspection PyCallingNonCallable
        return OrganizationAffiliationRoleCode("supplier")

    @classproperty
    def HIE(cls) -> "OrganizationAffiliationRoleCode":
        """
        An organization that facilitates electronic clinical data exchange between entities
        """
        # noinspection PyCallingNonCallable
        return OrganizationAffiliationRoleCode("HIE/HIO")

    @classproperty
    def Member(cls) -> "OrganizationAffiliationRoleCode":
        """
        A type of non-ownership relationship between entities (encompasses partnerships, collaboration, joint ventures, etc.)
        """
        # noinspection PyCallingNonCallable
        return OrganizationAffiliationRoleCode("member")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://hl7.org/fhir/ValueSet/organization-role
        """
        return "http://hl7.org/fhir/ValueSet/organization-role"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.880
        """
        return "2.16.840.1.113883.4.642.3.880"
