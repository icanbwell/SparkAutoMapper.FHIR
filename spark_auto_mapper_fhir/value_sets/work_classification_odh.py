from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class WorkClassificationODH(GenericTypeCode):
    """
    v3.WorkClassificationODH
    From: http://terminology.hl7.org/ValueSet/v3-WorkClassificationODH in v3-codesystems.xml
         Code system of concepts representing a person's job type as defined by
    compensation and sector (e.g. paid vs. unpaid, self-employed vs. not self-
    employed, government vs. private, etc.).
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH"


class WorkClassificationODHValues:
    """
    A situation in which an individual serves in a government-sponsored military
    force.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """

    PaidWork_ArmedForces = WorkClassificationODH("PWAF")
    """
    A situation in which an individual works for a national government
    organization, not including armed forces, and receives a paid salary or wage.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """
    PaidWork_NationalGovernment_NotArmedForces = WorkClassificationODH("PWFG")
    """
    A situation in which an individual works for a government organization with
    jurisdiction below the level of state/provincial/territorial/tribal government
    (e.g., city, town, township), not armed forces, and receives a paid salary or
    wage.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """
    PaidWork_LocalGovernment_NotArmedForces = WorkClassificationODH("PWLG")
    """
    A situation in which an individual works for a business (not government) that
    they do not own and receives a paid salary or wage.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """
    PaidNon_governmentalWork_NotSelf_employed = WorkClassificationODH("PWNSE")
    """
    A situation in which an individual earns a salary or wage working for himself
    or herself instead of working for an employer.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """
    PaidWork_Self_employed = WorkClassificationODH("PWSE")
    """
    A situation in which an individual works for a government organization with
    jurisdiction immediately below the level of national government (between
    national government and local government), not armed forces and receives a
    paid salary or wage.  Often called a state, provincial, territorial, or tribal
    government.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """
    PaidWork_StateGovernment_NotArmedForces = WorkClassificationODH("PWSG")
    """
    A situation in which an individual works for a business (not government) that
    they do not own without receiving a paid salary or wage.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """
    UnpaidNon_governmentalWork_NotSelf_employed = WorkClassificationODH("UWNSE")
    """
    A situation in which an individual works for himself or herself without
    receiving a paid salary or wage.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """
    UnpaidWork_Self_employed = WorkClassificationODH("UWSE")
    """
    A situation in which an individual chooses to do something, especially for
    other people or for an organization, willingly and without being forced or
    compensated to do it.  This can include formal activity undertaken through
    public, private and voluntary organizations as well as informal community
    participation.
    From: http://terminology.hl7.org/CodeSystem/v3-WorkClassificationODH in v3-codesystems.xml
    """
    VoluntaryWork = WorkClassificationODH("VW")
