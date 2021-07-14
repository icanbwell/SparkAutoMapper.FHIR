# TODO: we need a robust way to check for circular dependency


def test_condition_import_cycle() -> None:
    from spark_auto_mapper_fhir.resources.condition import Condition

    print(Condition.__name__)


def test_claim_import_cycle() -> None:
    from spark_auto_mapper_fhir.backbone_elements.claim_related import ClaimRelated
    from spark_auto_mapper_fhir.resources.claim import Claim

    print(ClaimRelated.__name__)
    print(Claim.__name__)


def test_explanation_of_benefits_import_cycle() -> None:
    from spark_auto_mapper_fhir.resources.explanation_of_benefit import (
        ExplanationOfBenefit,
    )

    print(ExplanationOfBenefit.__name__)
