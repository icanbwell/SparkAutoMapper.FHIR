from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class OrganizationTypeCode(FhirValueSetBase):
    """
    http://hl7.org/fhir/valueset-organization-type.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'OrganizationTypeCode']) -> None:
            self.f: Callable[..., 'OrganizationTypeCode'] = f

        def __get__(
            self, obj: Any, owner: Type['OrganizationTypeCode']
        ) -> 'OrganizationTypeCode':
            return self.f(owner)

    @classproperty
    def HealthcareProvider(cls) -> 'OrganizationTypeCode':
        """
        An organization that provides healthcare services.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("prov")

    @classproperty
    def HospitalDepartment(cls) -> 'OrganizationTypeCode':
        """
        A department or ward within a hospital (Generally is not applicable to top level organizations)
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("dept")

    @classproperty
    def OrganizationalTeam(cls) -> 'OrganizationTypeCode':
        """
        An organizational team is usually a grouping of practitioners that perform a specific function
        within an organization (which could be a top level organization, or a department).
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("team")

    @classproperty
    def Government(cls) -> 'OrganizationTypeCode':
        """
        A political body, often used when including organization records for government bodies
        such as a Federal Government, State or Local Government.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("govt")

    @classproperty
    def InsuranceCompany(cls) -> 'OrganizationTypeCode':
        """
        A company that provides insurance to its subscribers that may include healthcare related policies.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("ins")

    @classproperty
    def Payer(cls) -> 'OrganizationTypeCode':
        """
        A company, charity, or governmental organization, which processes claims and/or issues payments
         to providers on behalf of patients or groups of patients.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("pay")

    @classproperty
    def EducationalInstitute(cls) -> 'OrganizationTypeCode':
        """
        An educational institution that provides education or research facilities.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("edu")

    @classproperty
    def ReligiousInstitution(cls) -> 'OrganizationTypeCode':
        """
        An organization that is identified as a part of a religious institution.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("reli")

    @classproperty
    def ClinicalResearchSponsor(cls) -> 'OrganizationTypeCode':
        """
        An organization that is identified as a Pharmaceutical/Clinical Research Sponsor.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("crs")

    @classproperty
    def CommunityGroup(cls) -> 'OrganizationTypeCode':
        """
        An un-incorporated community group.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("cg")

    @classproperty
    def NonHealthcareBusiness(cls) -> 'OrganizationTypeCode':
        """
        An organization that is a registered business or corporation but not identified by other types.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("bus")

    @classproperty
    def Other(cls) -> 'OrganizationTypeCode':
        """
        Other type of organization not already specified.
        """
        # noinspection PyCallingNonCallable
        return OrganizationTypeCode("other")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/organization-type"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.414"
