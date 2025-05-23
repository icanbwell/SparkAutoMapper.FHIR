from __future__ import annotations

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri

from spark_auto_mapper_fhir.value_sets.generic_type import GenericTypeCode
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class ReligiousAffiliation(GenericTypeCode):
    """
    v3.ReligiousAffiliation
    From: http://terminology.hl7.org/ValueSet/v3-ReligiousAffiliation in v3-codesystems.xml
         Assigment of spiritual faith affiliation
    """

    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    """
    http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation
    """
    codeset: FhirUri = "http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation"


class ReligiousAffiliationValues:
    """
    Adventist
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """

    Adventist = ReligiousAffiliation("1001")
    """
    African Religions
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    AfricanReligions = ReligiousAffiliation("1002")
    """
    Afro-Caribbean Religions
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Afro_CaribbeanReligions = ReligiousAffiliation("1003")
    """
    Agnosticism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Agnosticism = ReligiousAffiliation("1004")
    """
    Anglican
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Anglican = ReligiousAffiliation("1005")
    """
    Animism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Animism = ReligiousAffiliation("1006")
    """
    Atheism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Atheism = ReligiousAffiliation("1007")
    """
    Babi & Baha'I faiths
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Babi_Baha_IFaiths = ReligiousAffiliation("1008")
    """
    Baptist
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Baptist = ReligiousAffiliation("1009")
    """
    Bon
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Bon = ReligiousAffiliation("1010")
    """
    Cao Dai
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    CaoDai = ReligiousAffiliation("1011")
    """
    Celticism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Celticism = ReligiousAffiliation("1012")
    """
    Christian (non-Catholic, non-specific)
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Christian_non_Catholic_Non_specific_ = ReligiousAffiliation("1013")
    """
    Confucianism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Confucianism = ReligiousAffiliation("1014")
    """
    Cyberculture Religions
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    CybercultureReligions = ReligiousAffiliation("1015")
    """
    Divination
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Divination = ReligiousAffiliation("1016")
    """
    Fourth Way
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    FourthWay = ReligiousAffiliation("1017")
    """
    Free Daism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    FreeDaism = ReligiousAffiliation("1018")
    """
    Gnosis
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Gnosis = ReligiousAffiliation("1019")
    """
    Hinduism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Hinduism = ReligiousAffiliation("1020")
    """
    Humanism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Humanism = ReligiousAffiliation("1021")
    """
    Independent
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Independent = ReligiousAffiliation("1022")
    """
    Islam
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Islam = ReligiousAffiliation("1023")
    """
    Jainism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Jainism = ReligiousAffiliation("1024")
    """
    Jehovah's Witnesses
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Jehovah_sWitnesses = ReligiousAffiliation("1025")
    """
    Judaism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Judaism = ReligiousAffiliation("1026")
    """
    Latter Day Saints
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    LatterDaySaints = ReligiousAffiliation("1027")
    """
    Lutheran
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Lutheran = ReligiousAffiliation("1028")
    """
    Mahayana
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Mahayana = ReligiousAffiliation("1029")
    """
    Meditation
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Meditation = ReligiousAffiliation("1030")
    """
    Messianic Judaism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    MessianicJudaism = ReligiousAffiliation("1031")
    """
    Mitraism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Mitraism = ReligiousAffiliation("1032")
    """
    New Age
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    NewAge = ReligiousAffiliation("1033")
    """
    non-Roman Catholic
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Non_RomanCatholic = ReligiousAffiliation("1034")
    """
    Occult
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Occult = ReligiousAffiliation("1035")
    """
    Orthodox
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Orthodox = ReligiousAffiliation("1036")
    """
    Paganism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Paganism = ReligiousAffiliation("1037")
    """
    Pentecostal
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Pentecostal = ReligiousAffiliation("1038")
    """
    Process, The
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Process_The = ReligiousAffiliation("1039")
    """
    Reformed/Presbyterian
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Reformed_Presbyterian = ReligiousAffiliation("1040")
    """
    Roman Catholic Church
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    RomanCatholicChurch = ReligiousAffiliation("1041")
    """
    Satanism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Satanism = ReligiousAffiliation("1042")
    """
    Scientology
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Scientology = ReligiousAffiliation("1043")
    """
    Shamanism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Shamanism = ReligiousAffiliation("1044")
    """
    Shiite (Islam)
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Shiite_Islam_ = ReligiousAffiliation("1045")
    """
    Shinto
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Shinto = ReligiousAffiliation("1046")
    """
    Sikism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Sikism = ReligiousAffiliation("1047")
    """
    Spiritualism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Spiritualism = ReligiousAffiliation("1048")
    """
    Sunni (Islam)
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Sunni_Islam_ = ReligiousAffiliation("1049")
    """
    Taoism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Taoism = ReligiousAffiliation("1050")
    """
    Theravada
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Theravada = ReligiousAffiliation("1051")
    """
    Unitarian-Universalism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Unitarian_Universalism = ReligiousAffiliation("1052")
    """
    Universal Life Church
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    UniversalLifeChurch = ReligiousAffiliation("1053")
    """
    Vajrayana (Tibetan)
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Vajrayana_Tibetan_ = ReligiousAffiliation("1054")
    """
    Veda
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Veda = ReligiousAffiliation("1055")
    """
    Voodoo
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Voodoo = ReligiousAffiliation("1056")
    """
    Wicca
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Wicca = ReligiousAffiliation("1057")
    """
    Yaohushua
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Yaohushua = ReligiousAffiliation("1058")
    """
    Zen Buddhism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    ZenBuddhism = ReligiousAffiliation("1059")
    """
    Zoroastrianism
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Zoroastrianism = ReligiousAffiliation("1060")
    """
    Assembly of God
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    AssemblyOfGod = ReligiousAffiliation("1061")
    """
    Brethren
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Brethren = ReligiousAffiliation("1062")
    """
    Christian Scientist
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    ChristianScientist = ReligiousAffiliation("1063")
    """
    Church of Christ
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    ChurchOfChrist = ReligiousAffiliation("1064")
    """
    Church of God
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    ChurchOfGod = ReligiousAffiliation("1065")
    """
    Congregational
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Congregational = ReligiousAffiliation("1066")
    """
    Disciples of Christ
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    DisciplesOfChrist = ReligiousAffiliation("1067")
    """
    Eastern Orthodox
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    EasternOrthodox = ReligiousAffiliation("1068")
    """
    Episcopalian
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Episcopalian = ReligiousAffiliation("1069")
    """
    Evangelical Covenant
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    EvangelicalCovenant = ReligiousAffiliation("1070")
    """
    Friends
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Friends = ReligiousAffiliation("1071")
    """
    Full Gospel
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    FullGospel = ReligiousAffiliation("1072")
    """
    Methodist
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Methodist = ReligiousAffiliation("1073")
    """
    Native American
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    NativeAmerican = ReligiousAffiliation("1074")
    """
    Nazarene
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Nazarene = ReligiousAffiliation("1075")
    """
    Presbyterian
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Presbyterian = ReligiousAffiliation("1076")
    """
    Protestant
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Protestant = ReligiousAffiliation("1077")
    """
    Protestant, No Denomination
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Protestant_NoDenomination = ReligiousAffiliation("1078")
    """
    Reformed
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    Reformed = ReligiousAffiliation("1079")
    """
    Salvation Army
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    SalvationArmy = ReligiousAffiliation("1080")
    """
    Unitarian Universalist
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    UnitarianUniversalist = ReligiousAffiliation("1081")
    """
    United Church of Christ
    From: http://terminology.hl7.org/CodeSystem/v3-ReligiousAffiliation in v3-codesystems.xml
    """
    UnitedChurchOfChrist = ReligiousAffiliation("1082")
