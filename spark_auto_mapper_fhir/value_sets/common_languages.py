from __future__ import annotations


from spark_auto_mapper_fhir.base_types.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class CommonLanguages(FhirValueSetBase):
    """ """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)


class CommonLanguagesValues:
    Arabic = CommonLanguages("ar")
    Bengali = CommonLanguages("bn")
    Czech = CommonLanguages("cs")
    Danish = CommonLanguages("da")
    German = CommonLanguages("de")
    German_Austria_ = CommonLanguages("de-AT")
    German_Switzerland_ = CommonLanguages("de-CH")
    German_Germany_ = CommonLanguages("de-DE")
    Greek = CommonLanguages("el")
    English = CommonLanguages("en")
    English_Australia_ = CommonLanguages("en-AU")
    English_Canada_ = CommonLanguages("en-CA")
    English_GreatBritain_ = CommonLanguages("en-GB")
    English_India_ = CommonLanguages("en-IN")
    English_NewZeland_ = CommonLanguages("en-NZ")
    English_Singapore_ = CommonLanguages("en-SG")
    English_UnitedStates_ = CommonLanguages("en-US")
    Spanish = CommonLanguages("es")
    Spanish_Argentina_ = CommonLanguages("es-AR")
    Spanish_Spain_ = CommonLanguages("es-ES")
    Spanish_Uruguay_ = CommonLanguages("es-UY")
    Finnish = CommonLanguages("fi")
    French = CommonLanguages("fr")
    French_Belgium_ = CommonLanguages("fr-BE")
    French_Switzerland_ = CommonLanguages("fr-CH")
    French_France_ = CommonLanguages("fr-FR")
    Frysian = CommonLanguages("fy")
    Frysian_Netherlands_ = CommonLanguages("fy-NL")
    Hindi = CommonLanguages("hi")
    Croatian = CommonLanguages("hr")
    Italian = CommonLanguages("it")
    Italian_Switzerland_ = CommonLanguages("it-CH")
    Italian_Italy_ = CommonLanguages("it-IT")
    Japanese = CommonLanguages("ja")
    Korean = CommonLanguages("ko")
    Dutch = CommonLanguages("nl")
    Dutch_Belgium_ = CommonLanguages("nl-BE")
    Dutch_Netherlands_ = CommonLanguages("nl-NL")
    Norwegian = CommonLanguages("no")
    Norwegian_Norway_ = CommonLanguages("no-NO")
    Punjabi = CommonLanguages("pa")
    Polish = CommonLanguages("pl")
    Portuguese = CommonLanguages("pt")
    Portuguese_Brazil_ = CommonLanguages("pt-BR")
    Russian = CommonLanguages("ru")
    Russian_Russia_ = CommonLanguages("ru-RU")
    Serbian = CommonLanguages("sr")
    Serbian_Serbia_ = CommonLanguages("sr-RS")
    Swedish = CommonLanguages("sv")
    Swedish_Sweden_ = CommonLanguages("sv-SE")
    Telegu = CommonLanguages("te")
    Chinese = CommonLanguages("zh")
    Chinese_China_ = CommonLanguages("zh-CN")
    Chinese_HongKong_ = CommonLanguages("zh-HK")
    Chinese_Singapore_ = CommonLanguages("zh-SG")
    Chinese_Taiwan_ = CommonLanguages("zh-TW")