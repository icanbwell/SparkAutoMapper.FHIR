from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class MeasurePopulationTypeCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-measure-population.html
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., "MeasurePopulationTypeCode"]) -> None:
            self.f: Callable[..., "MeasurePopulationTypeCode"] = f

        def __get__(
            self, obj: Any, owner: Type["MeasurePopulationTypeCode"]
        ) -> "MeasurePopulationTypeCode":
            return self.f(owner)

    @classproperty
    def InitialPopulation(cls) -> "MeasurePopulationTypeCode":
        """
        The initial population refers to all patients or events to be evaluated by a quality measure involving patients who share a common set of specified characterstics. All patients or events counted (for example, as numerator, as denominator) are drawn from the initial population.
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("initial-population")

    @classproperty
    def Numerator(cls) -> "MeasurePopulationTypeCode":
        """
        The upper portion of a fraction used to calculate a rate, proportion, or ratio. Also called the measure focus, it is the target process, condition, event, or outcome. Numerator criteria are the processes or outcomes expected for each patient, or event defined in the denominator. A numerator statement describes the clinical action that satisfies the conditions of the measure.
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("numerator")

    @classproperty
    def NumeratorExclusion(cls) -> "MeasurePopulationTypeCode":
        """
        Numerator exclusion criteria define patients or events to be removed from the numerator. Numerator exclusions are used in proportion and ratio measures to help narrow the numerator (for inverted measures).
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("numerator-exclusion")

    @classproperty
    def Denominator(cls) -> "MeasurePopulationTypeCode":
        """
        The lower portion of a fraction used to calculate a rate, proportion, or ratio. The denominator can be the same as the initial population, or a subset of the initial population to further constrain the population for the purpose of the measure.
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("denominator")

    @classproperty
    def DenominatorExclusion(cls) -> "MeasurePopulationTypeCode":
        """
        Denominator exclusion criteria define patients or events that should be removed from the denominator before determining if numerator criteria are met. Denominator exclusions are used in proportion and ratio measures to help narrow the denominator. For example, patients with bilateral lower extremity amputations would be listed as a denominator exclusion for a measure requiring foot exams.
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("denominator-exclusion")

    @classproperty
    def DenominatorException(cls) -> "MeasurePopulationTypeCode":
        """
        Denominator exceptions are conditions that should remove a patient or event from the denominator of a measure only if the numerator criteria are not met. Denominator exception allows for adjustment of the calculated score for those providers with higher risk populations. Denominator exception criteria are only used in proportion measures.
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("denominator-exception")

    @classproperty
    def MeasurePopulation(cls) -> "MeasurePopulationTypeCode":
        """
        Measure population criteria define the patients or events for which the individual observation for the measure should be taken. Measure populations are used for continuous variable measures rather than numerator and denominator criteria.
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("measure-population")

    @classproperty
    def MeasurePopulationExclusion(cls) -> "MeasurePopulationTypeCode":
        """
        Measure population criteria define the patients or events that should be removed from the measure population before determining the outcome of one or more continuous variables defined for the measure observation. Measure population exclusion criteria are used within continuous variable measures to help narrow the measure population.
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("measure-population-exclusion")

    @classproperty
    def MeasureObservation(cls) -> "MeasurePopulationTypeCode":
        """
        Defines the individual observation to be performed for each patient or event in the measure population. Measure observations for each case in the population are aggregated to determine the overall measure score for the population.
        """
        # noinspection PyCallingNonCallable
        return MeasurePopulationTypeCode("measure-observation")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/measure-population
        """
        return "http://terminology.hl7.org/CodeSystem/measure-population"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.765
        """
        return "2.16.840.1.113883.4.642.3.765"
