from __future__ import annotations
from typing import Optional, TYPE_CHECKING

from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase

from spark_auto_mapper_fhir.base_types.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)

if TYPE_CHECKING:
    pass
    # id_ (string)
    # extension (Extension)
    # modifierExtension (Extension)
    # operation (TestScript.Operation)
    from spark_auto_mapper_fhir.backbone_elements.test_script_operation import (
        TestScriptOperation,
    )

    # assert_ (TestScript.Assert)
    from spark_auto_mapper_fhir.backbone_elements.test_script_assert import (
        TestScriptAssert,
    )


# This file is auto-generated by generate_classes so do not edit manually
# noinspection PyPep8Naming
class TestScriptAction1(FhirBackboneElementBase):
    """
    TestScript.Action1
        A structured set of tests against a FHIR server or client implementation to determine compliance against the FHIR specification.
    """

    # noinspection PyPep8Naming
    def __init__(
        self,
        *,
        id_: Optional[FhirString] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
        modifierExtension: Optional[FhirList[ExtensionBase]] = None,
        operation: Optional[TestScriptOperation] = None,
        assert_: Optional[TestScriptAssert] = None,
    ) -> None:
        """
            A structured set of tests against a FHIR server or client implementation to
        determine compliance against the FHIR specification.

            :param id_: None
            :param extension: May be used to represent additional information that is not part of the basic
        definition of the element. To make the use of extensions safe and manageable,
        there is a strict set of governance  applied to the definition and use of
        extensions. Though any implementer can define an extension, there is a set of
        requirements that SHALL be met as part of the definition of the extension.
            :param modifierExtension: May be used to represent additional information that is not part of the basic
        definition of the element and that modifies the understanding of the element
        in which it is contained and/or the understanding of the containing element's
        descendants. Usually modifier elements provide negation or qualification. To
        make the use of extensions safe and manageable, there is a strict set of
        governance applied to the definition and use of extensions. Though any
        implementer can define an extension, there is a set of requirements that SHALL
        be met as part of the definition of the extension. Applications processing a
        resource are required to check for modifier extensions.

        Modifier extensions SHALL NOT change the meaning of any elements on Resource
        or DomainResource (including cannot change the meaning of modifierExtension
        itself).
            :param operation: An operation would involve a REST request to a server.
            :param assert_: Evaluates the results of previous operations to determine if the server under
        test behaves appropriately.
        """
        super().__init__(
            id_=id_,
            extension=extension,
            modifierExtension=modifierExtension,
            operation=operation,
            assert_=assert_,
        )
