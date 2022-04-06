import datetime
from json import loads, dumps
from os import path, makedirs
from pathlib import Path
from shutil import rmtree
from typing import Any, Union

from pyspark.sql.dataframe import DataFrame
from pyspark.sql.session import SparkSession
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper_fhir.value_sets.participant_type import ParticipantTypeCode

from spark_auto_mapper_fhir.complex_types.codeable_concept import CodeableConcept

from spark_auto_mapper_fhir.resources.practitioner import Practitioner

from spark_auto_mapper_fhir.backbone_elements.encounter_participant import (
    EncounterParticipant,
)

from spark_auto_mapper_fhir.fhir_types.list import FhirList

from spark_auto_mapper_fhir.complex_types.period import Period

from spark_auto_mapper_fhir.fhir_types.fhir_reference import FhirReference

from spark_auto_mapper_fhir.complex_types.reference import Reference

from spark_auto_mapper_fhir.value_sets.act_encounter_code import ActEncounterCode

from spark_auto_mapper_fhir.complex_types.coding import Coding

from spark_auto_mapper_fhir.value_sets.encounter_status import EncounterStatusCode


from spark_auto_mapper_fhir.fhir_types.id import FhirId

from spark_auto_mapper_fhir.resources.encounter import Encounter
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A


def test_auto_mapper_hir_period_uses_date(spark_session: SparkSession) -> None:
    data_dir: Path = Path(__file__).parent.joinpath("./")

    temp_folder = data_dir.joinpath("./temp")
    if path.isdir(temp_folder):
        rmtree(temp_folder)

    encounter_test_folder: Path = data_dir.joinpath("test_files").joinpath(
        "encounter.json"
    )

    minified_json_path: Path = create_jsonl_files(
        src_file=encounter_test_folder,
        dst_folder=temp_folder.joinpath("minified_period"),
        dst_file_name="1.json",
    )

    df = spark_session.read.json(str(minified_json_path))
    df.createOrReplaceTempView("encounters")

    mapper = AutoMapper(
        view="fhir_encounters",
        source_view="encounters",
        copy_all_unmapped_properties=True,
    ).complex(
        Encounter(
            use_date_for=["encounter.period.start", "encounter.period.end"],
            id_=FhirId(A.concat("pat", A.column("id"))),
            status=EncounterStatusCode(A.column("status")),
            class_=Coding(
                system=A.column("class.system"),
                code=ActEncounterCode(A.column("class.code")),
                display=A.column("class.display"),
            ),
            subject=Reference(
                display=A.column("subject.display"),
                reference=FhirReference(
                    resource="Patient",
                    column=A.concat(
                        "pat",
                        A.string_after_delimiter(A.column("subject.reference"), "/"),
                    ),
                ),
            ),
            period=Period(start=A.column("period.start"), end=A.column("period.end")),
            participant=FhirList(
                A.column("participant").select(  # type: ignore
                    EncounterParticipant(
                        individual=Reference[Union[Practitioner]](  # type: ignore
                            display=A.field("individual.display"),
                            reference=FhirReference(
                                resource="Practitioner",
                                column=A.concat(
                                    "pat",
                                    A.string_after_delimiter(
                                        A.field("individual.reference"), "/"
                                    ),
                                ),
                            ),
                        ),
                        type_=FhirList(
                            A.field("type").select(  # type: ignore
                                CodeableConcept(
                                    coding=FhirList(  # type: ignore
                                        A.field("coding").select(  # type: ignore
                                            Coding(
                                                system=A.field("system"),
                                                code=ParticipantTypeCode(
                                                    A.field("code")
                                                ),
                                                display=A.field("display"),
                                            )
                                        )
                                    ),
                                    text=A.field("text"),
                                ),
                            )
                        ),
                        period=Period(
                            start=A.field("period.start"),
                        ),
                    ),
                ),
            ),
        )
    )

    assert isinstance(mapper, AutoMapper)
    result_df: DataFrame = mapper.transform(df=df)
    assert result_df
    fhir_encounters_df = df.sql_ctx.table("fhir_encounters")
    assert isinstance(
        fhir_encounters_df.select(fhir_encounters_df.period.start).collect()[0][0],
        datetime.date,
    )
    assert isinstance(
        fhir_encounters_df.select(fhir_encounters_df.period.end).collect()[0][0],
        datetime.date,
    )


def create_jsonl_files(src_file: Path, dst_folder: Path, dst_file_name: str) -> Path:
    with open(src_file, "r") as file:
        json_object: Any = loads(file.read())
    json_text: str = dumps(obj=json_object, separators=(",", ":"))
    makedirs(dst_folder)
    minified_json_path: Path = dst_folder.joinpath(dst_file_name)
    with open(minified_json_path, "w+") as file:
        file.write(json_text)
    return minified_json_path
