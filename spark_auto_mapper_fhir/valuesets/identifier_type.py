from typing import Callable, Type, Any

from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class IdentifierTypeCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-identifier-type.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "IdentifierTypeCode"]) -> None:
            self.f: Callable[..., "IdentifierTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["IdentifierTypeCode"]
        ) -> "IdentifierTypeCode":
            return self.f(owner)

    @classproperty
    def AccreditationCertificationIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("AC")

    @classproperty
    def AmericanMedicalAssociationNumber(cls) -> "IdentifierTypeCode":
        """
        A physician identifier assigned by the AMA.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("AMA")

    @classproperty
    def AccountNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to an account.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("AN")

    @classproperty
    def AccountNumberCreditor(cls) -> "IdentifierTypeCode":
        """
        Class: Financial
        A more precise definition of an account number: sometimes two distinct account numbers must be transmitted
        in the same message, one as the creditor, the other as the debitor.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("ANC")

    # noinspection SpellCheckingInspection
    @classproperty
    def AccountNumberDebitor(cls) -> "IdentifierTypeCode":
        """
        Class: Financial
        A more precise definition of an account number: sometimes two distinct account numbers must be
        transmitted in the same message, one as the creditor, the other as the debitor.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("AND")

    @classproperty
    def AnonymousIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("ANON")

    @classproperty
    def TemporaryAccountNumber(cls) -> "IdentifierTypeCode":
        """
        Class: Financial
        Temporary version of an Account Number.
        Use Case: An ancillary system that does not normally assign account numbers is the first time
         to register a patient. This ancillary system will generate a temporary account number that will
         only be used until an official account number is assigned.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("ANT")

    @classproperty
    def BankAccountNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("BA")

    @classproperty
    def BankCardNumber(cls) -> "IdentifierTypeCode":
        """
        Class: Financial
        An identifier that is unique to a person's bank card.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("BC")

    @classproperty
    def BirthCertificateFileNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("BCFN")

    @classproperty
    def BirthCertificate(cls) -> "IdentifierTypeCode":
        """
        A number associated with a document identifying the event of a person's birth.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("BCT")

    @classproperty
    def BirthRegistryNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier unique within the Assigning Authority that is the official legal record of a person's birth.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("BR")

    @classproperty
    def CostCenterNumber(cls) -> "IdentifierTypeCode":
        """
        Class: Financial
        Use Case: needed especially for transmitting information about invoices.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("CC")

    @classproperty
    def ChangeOfNameDocument(cls) -> "IdentifierTypeCode":
        """
        A number associated with a document identifying a person's legal change of name.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("CONM")

    @classproperty
    def CountyNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("CY")

    @classproperty
    def CitizenshipCard(cls) -> "IdentifierTypeCode":
        """
        A number assigned by a person's country of residence to identify a person's citizenship.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("CZ")

    @classproperty
    def DeathCertificateId(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DC")

    @classproperty
    def DeathCertificateFileNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DCFN")

    @classproperty
    def DentistLicenseNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to a dentist within the jurisdiction of the licensing board
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DDS")

    @classproperty
    def DrugEnforcementAdministrationRegistrationNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier for an individual or organization relative to controlled substance regulation and transactions.
        Use case: This is a registration number that identifies an individual or organization relative to
        controlled substance regulation and transactions. A DEA number has a very precise and widely accepted
         meaning within the United States. Surprisingly, the US Drug Enforcement Administration does not
         solely assign DEA numbers in the United States. Hospitals have the authority to issue DEA numbers
          to their medical residents. These DEA numbers are based upon the hospital’s DEA number,
          but the authority rests with the hospital on the assignment to the residents.
          Thus, DEA as an Identifier Type is necessary in addition to DEA as an Assigning Authority.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DEA")

    @classproperty
    def DrugFurnishingOrPrescriptiveAuthorityNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DFN")

    @classproperty
    def DriverLicenseNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DL")

    @classproperty
    def DoctorNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DN")

    @classproperty
    def OsteopathicLicenseNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to an osteopath within the jurisdiction of a licensing board.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DO")

    @classproperty
    def PodiatristLicenseNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to a podiatrist within the jurisdiction of the licensing board.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("DPM")

    @classproperty
    def EmployeeId(cls) -> "IdentifierTypeCode":
        """
        A number that uniquely identifies an employee to an employer.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("EI")

    @classproperty
    def EmployerNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("EN")

    @classproperty
    def StaffEnterpriseNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to a staff member within an enterprise (as identified by the Assigning Authority).
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("ESN")

    @classproperty
    def FacilityId(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("FI")

    @classproperty
    def GuarantorInternalIdentifier(cls) -> "IdentifierTypeCode":
        """
        Class: Financial
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("GI")

    @classproperty
    def GeneralLedgerNumber(cls) -> "IdentifierTypeCode":
        """
        Class: Financial
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("GL")

    @classproperty
    def GuarantorExternalIdentifier(cls) -> "IdentifierTypeCode":
        """
        Class: Financial
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("GN")

    @classproperty
    def HealthCardNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("HC")

    @classproperty
    def LicenseNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("LN")

    @classproperty
    def PatientMedicaidNumber(cls) -> "IdentifierTypeCode":
        """
        Class: Insurance
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MA")

    @classproperty
    def MemberNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier for the insured of an insurance policy (this insured always has a subscriber),
        usually assigned by the insurance carrier. Use Case: Person is covered by an insurance policy.
        This person may or may not be the subscriber of the policy.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MB")

    @classproperty
    def PatientMedicareNumber(cls) -> "IdentifierTypeCode":
        """
        Patient's Medicare number. Class: Insurance
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MC")

    @classproperty
    def PractitionerMedicaidNumber(cls) -> "IdentifierTypeCode":
        """
        Practitioner Medicaid number. Class: Insurance
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MCD")

    @classproperty
    def PractitionerMedicareNumber(cls) -> "IdentifierTypeCode":
        """
        Practitioner Medicare number. Class: Insurance
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MCR")

    @classproperty
    def MedicalLicenseNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to a medical doctor within the jurisdiction of a licensing board.
        Use Case: These license numbers are sometimes used as identifiers. In some states,
        the same authority issues all three identifiers, e.g., medical, osteopathic, and
        physician assistant licenses all issued by one state medical board.
        For this case, the CX data type requires distinct identifier types to accurately interpret component
        1. Additionally, the distinction among these license types is critical in most health care settings
        (this is not to convey full licensing information, which requires a segment to support all related attributes).
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MD")

    @classproperty
    def MilitaryIdNumber(cls) -> "IdentifierTypeCode":
        """
        A number assigned to an individual who has had military duty, but is not currently on active duty.
        The number is assigned by the DOD or Veterans' Affairs (VA).
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MI")

    @classproperty
    def MedicalRecordNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to a patient within a set of medical records,
        not necessarily unique within an application.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MR")

    @classproperty
    def TemporaryMedicalRecordNumber(cls) -> "IdentifierTypeCode":
        """
        Temporary version of a Medical Record Number
        Use Case: An ancillary system that does not normally assign medical record numbers
        is the first time to register a patient. This ancillary system will generate a temporary
        medical record number that will only be used until an official medical record number is assigned.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("MRT")

    @classproperty
    def NaturalizationCertificate(cls) -> "IdentifierTypeCode":
        """
        A number associated with a document identifying a person's retention of citizenship in a particular country.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("NCT")

    @classproperty
    def NationalEmployerIdentifier(cls) -> "IdentifierTypeCode":
        """
        In the US, the Assigning Authority for this value is typically CMS, but it may be used by all providers
         and insurance companies in HIPAA related transactions.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("NE")

    @classproperty
    def NationalHealthPlanIdentifier(cls) -> "IdentifierTypeCode":
        """
        Class: Insurance
        Used for the UK NHS national identifier.
        In the US, the Assigning Authority for this value is typically CMS, but it may be used by
        all providers and insurance companies in HIPAA related transactions.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("NH")

    @classproperty
    def NationalUniqueIndividualIdentifier(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to a nurse practitioner within the jurisdiction of a certifying board.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("NI")

    @classproperty
    def NursePractitionerNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to a nurse practitioner within the jurisdiction of a certifying board.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("NP")

    @classproperty
    def NationalProviderIdentifier(cls) -> "IdentifierTypeCode":
        """
        Class: Insurance In the US, the Assigning Authority for this value is typically CMS,
        but it may be used by all providers and insurance companies in HIPAA related transactions.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("NPI")

    @classproperty
    def OptometristLicenseNumber(cls) -> "IdentifierTypeCode":
        """
        A number that is unique to an individual optometrist within the jurisdiction of the licensing board.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("OD")

    @classproperty
    def PhysicianAssistantNumber(cls) -> "IdentifierTypeCode":
        """
        An identifier that is unique to a physician assistant within the jurisdiction of a licensing board
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("PA")

    @classproperty
    def PensionNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("PEN")

    @classproperty
    def PatientInternalIdentifier(cls) -> "IdentifierTypeCode":
        """
        A number that is unique to a patient within an Assigning Authority.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("PI")

    @classproperty
    def PersonNumber(cls) -> "IdentifierTypeCode":
        """
        A number that is unique to a living subject within an Assigning Authority.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("PN")

    @classproperty
    def PassportNumber(cls) -> "IdentifierTypeCode":
        """
        A unique number assigned to the document affirming that a person is a citizen of the country.
        In the US this number is issued only by the State Department.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("PPN")

    @classproperty
    def ProviderNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("PRN")

    @classproperty
    def PatientExternalIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("PT")

    @classproperty
    def ResourceIdentifier(cls) -> "IdentifierTypeCode":
        """
        A generalized resource identifier. Use Case: An identifier type is needed to accommodate
        what are commonly known as resources. The resources can include human (e.g. a respiratory therapist),
        non-human (e.g., a companion animal), inanimate object (e.g., an exam room),
        organization (e.g., diabetic education class) or any other physical or logical entity.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("RI")

    @classproperty
    def SocialBeneficiaryIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("SB")

    @classproperty
    def SpecimenId(cls) -> "IdentifierTypeCode":
        """
        Identifier for a specimen. Used when it is not known if the specimen ID is a unique specimen ID (USID)
        or an ancestor ID (ASID).
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("SID")

    @classproperty
    def StateLicense(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("SL")

    @classproperty
    def SubscriberNumber(cls) -> "IdentifierTypeCode":
        """
        Class: Insurance An identifier for a subscriber of an insurance policy which is unique for,
        and usually assigned by, the insurance carrier.
        Use Case: A person is the subscriber of an insurance policy.
        The person’s family may be plan members, but are not the subscriber.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("SN")

    @classproperty
    def SerialNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("SNO")

    @classproperty
    def StateRegistryId(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("SR")

    @classproperty
    def SocialSecurityNumber(cls) -> "IdentifierTypeCode":
        """
        Social Security number
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("SS")

    @classproperty
    def ShipmentTrackingNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("STN")

    @classproperty
    def TaxIdNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("TAX")

    @classproperty
    def TrainingLicenseNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("TRL")

    @classproperty
    def UnspecifiedIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("U")

    @classproperty
    def UniversalDeviceIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("UDI")

    @classproperty
    def UniversalPhysicianIdentificationNumber(cls) -> "IdentifierTypeCode":
        """
        Class: Insurance
        An identifier for a provider within the CMS/Medicare program.
        A globally unique identifier for the provider in the Medicare program.
        """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("UPIN")

    @classproperty
    def VisitNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("VN")

    @classproperty
    def WICIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("WC")

    @classproperty
    def WorkersCompNumber(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("WCN")

    @classproperty
    def HealthPlanIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("XV")

    @classproperty
    def OrganizationIdentifier(cls) -> "IdentifierTypeCode":
        """ """
        # noinspection PyCallingNonCallable
        return IdentifierTypeCode("XX")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/v2-0203"
