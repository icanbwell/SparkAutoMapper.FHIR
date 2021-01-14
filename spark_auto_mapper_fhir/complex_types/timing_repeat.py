from typing import Optional

from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt

from spark_auto_mapper_fhir.fhir_types.time import FhirTime

from spark_auto_mapper_fhir.valuesets.days_of_week import DaysOfWeekCode

from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal

from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.complex_types.duration import Duration
from spark_auto_mapper_fhir.complex_types.range import Range

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.complex_types.fhir_complex_type_base import FhirComplexTypeBase
from spark_auto_mapper_fhir.valuesets.event_timing import EventTimingCode
from spark_auto_mapper_fhir.valuesets.units_of_time import UnitsOfTimeCode


class TimingRepeat(FhirComplexTypeBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        boundsDuration: Optional[Duration] = None,
        boundsRange: Optional[Range] = None,
        boundsPeriod: Optional[Period] = None,
        count: Optional[FhirPositiveInt] = None,
        countMax: Optional[FhirPositiveInt] = None,
        duration: Optional[FhirDecimal] = None,
        durationMax: Optional[FhirDecimal] = None,
        durationUnit: Optional[UnitsOfTimeCode] = None,
        frequency: Optional[FhirPositiveInt] = None,
        frequencyMax: Optional[FhirPositiveInt] = None,
        period: Optional[FhirDecimal] = None,
        periodMax: Optional[FhirDecimal] = None,
        periodUnit: Optional[UnitsOfTimeCode] = None,
        dayOfWeek: Optional[FhirList[DaysOfWeekCode]] = None,
        timeOfDay: Optional[FhirList[FhirTime]] = None,
        when: Optional[FhirList[EventTimingCode]] = None,
        offset: Optional[FhirUnsignedInt] = None
    ) -> None:
        """
        TimingRepeat Complex Type in FHIR
        https://www.hl7.org/fhir/datatypes-definitions.html#Timing.repeat
        When the event is to occur
            + Rule: if there's a duration, there needs to be duration units
            + Rule: if there's a period, there needs to be period units
            + Rule: duration SHALL be a non-negative value
            + Rule: period SHALL be a non-negative value
            + Rule: If there's a periodMax, there must be a period
            + Rule: If there's a durationMax, there must be a duration
            + Rule: If there's a countMax, there must be a count
            + Rule: If there's an offset, there must be a when (and not C, CM, CD, CV)
            + Rule: If there's a timeOfDay, there cannot be a when, or vice versa


        :param boundsDuration: Length/Range of lengths, or (Start and/or end) limits
        :param boundsRange: Length/Range of lengths, or (Start and/or end) limits
        :param boundsPeriod: Length/Range of lengths, or (Start and/or end) limits
        :param count: Number of times to repeat
        :param countMax: Maximum number of times to repeat
        :param duration: How long when it happens
        :param durationMax: How long when it happens (Max)
        :param durationUnit: s | min | h | d | wk | mo | a - unit of time (UCUM)
        :param frequency: Event occurs frequency times per period
        :param frequencyMax: Event occurs up to frequencyMax times per period
        :param period: Event occurs frequency times per period
        :param periodMax: Upper limit of period (3-4 hours)
        :param periodUnit: s | min | h | d | wk | mo | a - unit of time (UCUM)
        :param dayOfWeek: mon | tue | wed | thu | fri | sat | sun
        :param timeOfDay: Time of day for action
        :param when: Code for time period of occurrence
        :param offset: Minutes from event (before or after)
        """
        super().__init__(
            id_=id_,
            extension=extension,
            boundsDuration=boundsDuration,
            boundsRange=boundsRange,
            boundsPeriod=boundsPeriod,
            count=count,
            countMax=countMax,
            duration=duration,
            durationMax=durationMax,
            durationUnit=durationUnit,
            frequency=frequency,
            frequencyMax=frequencyMax,
            period=period,
            periodMax=periodMax,
            periodUnit=periodUnit,
            dayOfWeek=dayOfWeek,
            timeOfDay=timeOfDay,
            when=when,
            offset=offset
        )
