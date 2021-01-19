# TODO: we need a robust way to check for circular dependency


def test_condition_import_cycle() -> None:
    from spark_auto_mapper_fhir.resources.condition import Condition

    print(Condition.__name__)
