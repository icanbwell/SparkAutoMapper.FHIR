from pyspark.sql import SparkSession, Column, DataFrame
from pyspark.sql.functions import lit, struct, col, array, coalesce, to_date

from spark_auto_mapper.automapper import AutoMapper
from spark_auto_mapper.automapper_helpers import AutoMapperHelpers as A
from spark_auto_mapper_fhir.automapper_fhir_helpers import AutoMapperFhirHelpers as F


def test_auto_mapper_fhir_patient(spark_session: SparkSession):
    # Arrange
    spark_session.createDataFrame(
        [
            (1, 'Qureshi', 'Imran', '1970-01-01'),
            (2, 'Vidal', 'Michael', '1970-02-02'),
        ],
        ['member_id', 'last_name', 'first_name', 'date_of_birth']
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapper(
        view="members",
        source_view="patients",
        keys=["member_id"]
    ).withColumn(
        dst_column="patient",
        value=F.patient(
            id_=A.column("a.member_id"),
            birthDate=A.date(
                A.column("date_of_birth")
            ),
            name=A.list(
                F.human_name(
                    use="usual",
                    family=A.column("last_name")
                )
            )
        )
    )

    sql_expression: Column = mapper.get_column_spec()
    print(sql_expression)

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    assert str(sql_expression) == str(
        struct(
            col("a.member_id").alias("id"),
            coalesce(
                to_date(col("date_of_birth"), 'yyyy-MM-dd'),
                to_date(col("date_of_birth"), 'yyyyMMdd'),
                to_date(col("date_of_birth"), 'MM/dd/yy')
            ).alias("birthDate"),
            array(
                struct(
                    lit("usual").alias("use"),
                    col("last_name").alias("family"),
                )
            ).alias("name"),
        ).alias("patient")
    )

    result_df.printSchema()
    result_df.show()

    result_df.where("member_id == 1").select("patient").show()
    result_df.where("member_id == 1").select("patient").printSchema()

    assert result_df.where("member_id == 1").selectExpr("patient.name[0].use").collect()[0][0] == "usual"
    assert result_df.where("member_id == 1").selectExpr("patient.name[0].family").collect()[0][0] == "Qureshi"
