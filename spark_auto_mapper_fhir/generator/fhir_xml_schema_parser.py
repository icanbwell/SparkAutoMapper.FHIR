import dataclasses
from pathlib import Path
from typing import OrderedDict, Any, List, Union, Dict, Optional
import re

from spark_pipeline_framework.utilities.flattener import flatten  # type: ignore
from xmltodict import parse


@dataclasses.dataclass
class SmartName:
    name: str
    cleaned_name: str
    snake_case_name: str


@dataclasses.dataclass
class FhirValueSetConcept:
    code: str
    display: Optional[str]
    cleaned_display: Optional[str]
    definition: Optional[str]


@dataclasses.dataclass
class FhirValueSet:
    id_: str
    name: str
    name_snake_case: str
    cleaned_name: str
    concepts: List[FhirValueSetConcept]
    url: str
    value_set_url: str


@dataclasses.dataclass
class FhirCodeableType:
    codeable_type: str
    path: str
    codeable_type_url: str
    is_codeable_concept: bool = False


@dataclasses.dataclass
class FhirReferenceType:
    target_resources: List[str]
    path: str


@dataclasses.dataclass
class FhirProperty:
    name: str
    type_: str
    cleaned_type: str
    type_snake_case: str
    optional: bool
    is_list: bool
    documentation: List[str]
    fhir_type: Optional[str]
    reference_target_resources: List[SmartName]
    reference_target_resources_names: List[str]
    is_back_bone_element: bool
    is_basic_type: bool
    codeable_type: Optional[SmartName]
    is_code: bool = False


@dataclasses.dataclass
class FhirEntity:
    fhir_name: str
    cleaned_name: str
    name_snake_case: str
    properties: List[FhirProperty]
    documentation: List[str]
    type_: Optional[str]
    is_back_bone_element: bool
    is_value_set: bool = False
    value_set_concepts: Optional[List[FhirValueSetConcept]] = None
    value_set_url: Optional[str] = None
    is_basic_type: bool = False


class FhirXmlSchemaParser:
    cleaned_type_mapping: Dict[str, str] = {
        "boolean": "FhirBoolean",
        "date": "FhirDate",
        "dateTime": "FhirDateTime",
        "time": "FhirTime",
        "instant": "FhirInstant",
        "integer": "FhirInteger",
        "positiveInt": "FhirPositiveInt",
        "decimal": "FhirDecimal",
        "string": "FhirString",
        "DataType": "FhirDataType",
        "markdown": "FhirMarkdown",
        "canonical": "FhirCanonical",
        "List": "List_",
        "uri": "FhirUri",
    }

    @staticmethod
    def camel_to_snake(name: str) -> str:
        name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
        return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()

    @staticmethod
    def generate_classes(filter_to_resource: Optional[str] = None) -> List[FhirEntity]:
        data_dir: Path = Path(__file__).parent.joinpath("./")
        # schema = XMLSchema(str(resource_xsd_file))
        # pprint(schema.to_dict)
        fhir_entities: List[FhirEntity] = []

        # first read fhir-all.xsd to get a list of resources
        fhir_xsd_all_file: Path = (
            data_dir.joinpath("xsd")
            .joinpath("definitions.xml")
            .joinpath("fhir-all-xsd")
            .joinpath("fhir-all.xsd")
        )
        resources: List[str] = ["fhir-base.xsd"]

        with open(fhir_xsd_all_file, "r") as file:
            contents = file.read()
            result: OrderedDict[str, Any] = parse(contents)
            resource_item: OrderedDict[str, Any]
            for resource_item in result["xs:schema"]["xs:include"]:
                resources.append(resource_item["@schemaLocation"])

        resource_xsd_file_name: str
        for resource_xsd_file_name in resources:
            if (
                filter_to_resource
                and not resource_xsd_file_name.startswith(filter_to_resource)
                and not resource_xsd_file_name == "fhir-base.xsd"
            ):
                continue
            resource_xsd_file: Path = (
                data_dir.joinpath("xsd")
                .joinpath("definitions.xml")
                .joinpath("fhir-all-xsd")
                .joinpath(resource_xsd_file_name)
            )
            fhir_entities.extend(
                FhirXmlSchemaParser._generate_classes_for_resource(resource_xsd_file)
            )

        # now set the types in each property
        property_type_mapping: Dict[str, str] = {
            fhir_entity.fhir_name: fhir_entity.type_
            for fhir_entity in fhir_entities
            if fhir_entity.type_
        }

        for fhir_entity in fhir_entities:
            print(f"2nd pass: checking {fhir_entity.fhir_name}")
            for fhir_property in fhir_entity.properties:
                print(f"---- {fhir_property.name}: {fhir_property.type_} ----")
                if fhir_property.type_ not in property_type_mapping.keys():
                    print(
                        f"WARNING: 2nd pass: {fhir_property.type_} not found in property_type_mapping"
                    )
                else:
                    fhir_property.fhir_type = property_type_mapping[fhir_property.type_]

        # and the target resources for references
        FhirXmlSchemaParser.process_types_for_references(fhir_entities)

        value_sets: List[FhirValueSet] = FhirXmlSchemaParser.get_value_sets()

        # and the target types for codeable concepts
        FhirXmlSchemaParser.process_types_for_codeable_concepts(
            fhir_entities, value_sets
        )

        # value_set: FhirValueSet
        # for value_set in value_sets:
        #     for fhir_entity in fhir_entities:
        #         if value_set.name == fhir_entity.fhir_name:
        #             fhir_entity.is_value_set = True

        # remove any entities that are already in value_sets
        fhir_entities = [
            c
            for c in fhir_entities
            if c.fhir_name not in [b.name for b in value_sets]
            or c.cleaned_name in ["PractitionerRole", "ElementDefinition"]
        ]
        fhir_entities.extend(
            [
                FhirEntity(
                    type_="ValueSet",
                    fhir_name=c.name,
                    name_snake_case=c.name_snake_case,
                    cleaned_name=c.cleaned_name,
                    documentation=[],
                    properties=[],
                    is_back_bone_element=False,
                    is_value_set=True,
                    value_set_concepts=c.concepts,
                    value_set_url=c.value_set_url or c.url,
                )
                for c in value_sets
            ]
        )

        # update types
        # cleaned_type_mapping: Dict[str, str] = {
        #     "boolean": "FhirBoolean",
        #     "date": "FhirDate",
        #     "dateTime": "FhirDateTime",
        #     "integer": "FhirInteger",
        #     "string": "FhirString",
        # }
        # for fhir_entity in fhir_entities:
        #     if fhir_entity.fhir_name in cleaned_type_mapping.keys():
        #         fhir_entity.fhir_name = cleaned_type_mapping[fhir_entity.fhir_name]

        exclude_entities: List[str] = [
            "Resource",
            "DomainResource",
            "Element",
        ]

        fhir_entities = [
            f for f in fhir_entities if f.cleaned_name not in exclude_entities
        ]

        # cleaned names
        for fhir_entity in fhir_entities:
            if fhir_entity.fhir_name in FhirXmlSchemaParser.cleaned_type_mapping:
                fhir_entity.cleaned_name = FhirXmlSchemaParser.cleaned_type_mapping[
                    fhir_entity.fhir_name
                ]
                fhir_entity.is_basic_type = True

        # replace any lists
        value_set_names: List[str] = [c.name for c in value_sets]
        for fhir_entity in fhir_entities:
            for fhir_property in fhir_entity.properties:
                if not fhir_property.is_code and fhir_property.type_ in value_set_names:
                    fhir_property.is_code = True
                    fhir_property.cleaned_type = [
                        c.cleaned_name
                        for c in value_sets
                        if c.name == fhir_property.type_
                    ][0]

        # find all codeable concepts that are not mapped

        return fhir_entities

    @staticmethod
    def process_types_for_codeable_concepts(
        fhir_entities: List[FhirEntity], value_sets: List[FhirValueSet]
    ) -> None:
        codeable_types: List[
            FhirCodeableType
        ] = FhirXmlSchemaParser.get_types_for_codeable_concepts()
        codeable_type: FhirCodeableType
        for codeable_type in codeable_types:
            name_parts: List[str] = codeable_type.path.split(".")
            # find the entity corresponding to the name parts
            entity_name_parts: List[str] = name_parts[0:-1]
            fhir_entity_list: List[FhirEntity] = []
            parent_fhir_entity: Optional[FhirEntity] = None
            # parent_entity_name: Optional[str] = None
            for entity_name_part in entity_name_parts:
                if not parent_fhir_entity:
                    # entity_name = entity_name_part
                    fhir_entity_list = [
                        f for f in fhir_entities if f.fhir_name == entity_name_part
                    ]
                    if not fhir_entity_list:
                        print(
                            f"WARNING: {entity_name_part} not found in fhir_entity_list"
                        )
                    else:
                        parent_fhir_entity = fhir_entity_list[0]
                else:
                    # find the property under the above entity
                    fhir_property_list = [
                        p
                        for p in parent_fhir_entity.properties
                        if p.name == entity_name_part
                    ]
                    if not fhir_property_list:
                        print(
                            f"WARNING: {entity_name_part} not found in properties of {parent_fhir_entity.fhir_name}"
                        )
                    else:
                        fhir_property = fhir_property_list[0]
                        parent_entity_name = fhir_property.cleaned_type
                        fhir_entity_list = [
                            f
                            for f in fhir_entities
                            if f.cleaned_name == parent_entity_name
                        ]
                        if not fhir_entity_list:
                            print(
                                f"WARNING: No FHIR entity list for {parent_entity_name}"
                            )
                        else:
                            parent_fhir_entity = fhir_entity_list[0]
            property_name: str = name_parts[-1]
            # find the corresponding fhir entity
            if fhir_entity_list:
                fhir_entity = fhir_entity_list[0]
                fhir_property_list = [
                    p
                    for p in fhir_entity.properties
                    if p.name == FhirXmlSchemaParser.fix_python_keywords(property_name)
                ]

                if not fhir_property_list:
                    print(
                        f"WARNING: property {property_name} not found in {fhir_entity.fhir_name}"
                    )
                if fhir_property_list:
                    fhir_property = fhir_property_list[0]
                    value_set_matching = [
                        c
                        for c in value_sets
                        if (
                            c.url
                            and codeable_type.codeable_type_url
                            and c.url.split("|")[0]
                            == codeable_type.codeable_type_url.split("|")[0]
                        )
                        or (
                            c.value_set_url
                            and codeable_type.codeable_type_url
                            and (
                                c.value_set_url.split("|")[0]
                                == codeable_type.codeable_type_url.split("|")[0]
                            )
                        )
                    ]
                    if value_set_matching:
                        value_set = value_set_matching[0]
                        if codeable_type.is_codeable_concept:
                            fhir_property.codeable_type = SmartName(
                                name=value_set.name,
                                cleaned_name=value_set.cleaned_name,
                                snake_case_name=value_set.name_snake_case,
                            )
                        else:
                            fhir_property.type_ = value_set.name
                            fhir_property.type_snake_case = value_set.name_snake_case
                            fhir_property.cleaned_type = value_set.cleaned_name
                            fhir_property.is_code = True

        # set generic type for everything else
        for fhir_entity in fhir_entities:
            for property_ in fhir_entity.properties:
                if (
                    property_.cleaned_type in ["CodeableConcept", "Coding"]
                    and not property_.codeable_type
                ):
                    property_.codeable_type = SmartName(
                        name="generic_type",
                        cleaned_name="GenericTypeCode",
                        snake_case_name="generic_type",
                    )

    @staticmethod
    def process_types_for_references(fhir_entities: List[FhirEntity]) -> None:
        references: List[
            FhirReferenceType
        ] = FhirXmlSchemaParser.get_types_for_references()
        reference: FhirReferenceType
        for reference in references:
            name_parts: List[str] = reference.path.split(".")
            # find the entity corresponding to the name parts
            entity_name_parts: List[str] = name_parts[0:-1]
            fhir_entity_list: List[FhirEntity] = []
            parent_fhir_entity: Optional[FhirEntity] = None
            # parent_entity_name: Optional[str] = None
            for entity_name_part in entity_name_parts:
                if not parent_fhir_entity:
                    # entity_name = entity_name_part
                    fhir_entity_list = [
                        f for f in fhir_entities if f.fhir_name == entity_name_part
                    ]
                    if not fhir_entity_list:
                        print(
                            f"WARNING: References: {entity_name_part} not found in fhir_entities"
                        )
                    else:
                        parent_fhir_entity = fhir_entity_list[0]
                else:
                    # find the property under the above entity
                    fhir_property_list = [
                        p
                        for p in parent_fhir_entity.properties
                        if p.name == entity_name_part
                    ]
                    if not fhir_property_list:
                        print(
                            f"WARNING: References: {entity_name_part} not found in properties of {parent_fhir_entity.fhir_name}"
                        )
                    else:
                        fhir_property = fhir_property_list[0]
                        parent_entity_name = fhir_property.cleaned_type
                        fhir_entity_list = [
                            f
                            for f in fhir_entities
                            if f.cleaned_name == parent_entity_name
                        ]
                        if not fhir_entity_list:
                            print(
                                f"WARNING: References: {parent_entity_name} not found in fhir_entities"
                            )
                        else:
                            parent_fhir_entity = fhir_entity_list[0]
            property_name: str = name_parts[-1]
            # find the corresponding fhir entity
            if fhir_entity_list:
                fhir_entity = fhir_entity_list[0]
                if property_name.endswith("[x]"):  # handle choice properties
                    property_name_prefix = property_name.split("[")[0]
                    fhir_property_list = [
                        p
                        for p in fhir_entity.properties
                        if p.name.startswith(property_name_prefix)
                        and p.type_ == "Reference"
                    ]
                else:
                    fhir_property_list = [
                        p
                        for p in fhir_entity.properties
                        if p.name
                        == FhirXmlSchemaParser.fix_python_keywords(property_name)
                    ]
                if fhir_property_list:
                    fhir_property = fhir_property_list[0]
                    fhir_property.reference_target_resources = [
                        SmartName(
                            name=c,
                            cleaned_name=FhirXmlSchemaParser.cleaned_type_mapping[c]
                            if c in FhirXmlSchemaParser.cleaned_type_mapping
                            else c,
                            snake_case_name=FhirXmlSchemaParser.camel_to_snake(c),
                        )
                        for c in reference.target_resources
                    ]
                    fhir_property.reference_target_resources_names = [
                        FhirXmlSchemaParser.cleaned_type_mapping[c.name]
                        if c.name in FhirXmlSchemaParser.cleaned_type_mapping
                        else c.name
                        for c in fhir_property.reference_target_resources
                    ]

        # set generic type for everything else
        for fhir_entity in fhir_entities:
            for property_ in fhir_entity.properties:
                if (
                    property_.cleaned_type in ["Reference"]
                    and not property_.reference_target_resources
                ):
                    property_.reference_target_resources = [
                        SmartName(
                            name="Resource",
                            cleaned_name="Resource",
                            snake_case_name="resource",
                        )
                    ]
                    property_.reference_target_resources_names = ["Resource"]

    @staticmethod
    def _generate_classes_for_resource(resource_xsd_file: Path) -> List[FhirEntity]:
        print(f"++++++ PROCESSING FILE {resource_xsd_file.name} +++++++++ ")
        with open(resource_xsd_file, "r") as file:
            contents = file.read()
            result = parse(contents)
            # pprint(result)
        fhir_entities: List[FhirEntity] = []
        complex_types: List[OrderedDict[str, Any]] = result["xs:schema"][
            "xs:complexType"
        ]
        # if there is only one entry, then xml_to_dict makes it an object instead of a list
        if isinstance(complex_types, OrderedDict):
            complex_types = [complex_types]
        complex_type: OrderedDict[str, Any]
        for complex_type in complex_types:
            if not isinstance(complex_type, OrderedDict):
                print(f"ASSERT: complex_type is not OrderedDict.  {type(complex_type)}")
            assert isinstance(complex_type, OrderedDict), type(complex_type)
            complex_type_name: str = complex_type["@name"]
            cleaned_complex_type_name: str = complex_type_name.replace(".", "")
            complex_type_name_snake_case: str = FhirXmlSchemaParser.camel_to_snake(
                cleaned_complex_type_name
            )
            print(f"========== {complex_type_name} ===========")
            documentation_items: List[OrderedDict[str, Any]] = (
                complex_type["xs:annotation"]["xs:documentation"]
                if "x:annotation" in complex_type
                else []
            )
            if isinstance(documentation_items, OrderedDict):
                documentation_items = [documentation_items]
            documentation_item_dict: Union[OrderedDict[str, Any], str]
            documentation_entries: List[str] = []
            for documentation_item_dict in documentation_items:
                if isinstance(documentation_item_dict, OrderedDict):
                    documentation: str = documentation_item_dict["#text"]
                elif isinstance(documentation_item_dict, str):
                    documentation = documentation_item_dict
                else:
                    documentation = "Error"
                    assert isinstance(documentation_item_dict, OrderedDict), type(
                        documentation_item_dict
                    )
                print(f"// {documentation}")
                documentation_entries.append(documentation)

            inner_complex_type: Optional[OrderedDict[str, Any]] = (
                complex_type.get("xs:complexContent").get("xs:extension")  # type: ignore
                if complex_type.get("xs:complexContent")
                else None
            )
            entity_type: Optional[str] = None
            if inner_complex_type:
                entity_type = str(inner_complex_type.get("@base"))
                print(f"type={entity_type}")
                fhir_properties = FhirXmlSchemaParser.generate_properties_for_class(
                    inner_complex_type
                )
            elif "xs:sequence" in complex_type:
                entity_type = "Element"
                fhir_properties = FhirXmlSchemaParser.generate_properties_for_class(
                    complex_type
                )
            else:
                fhir_properties = []
            # now create the entity
            fhir_entity: FhirEntity = FhirEntity(
                fhir_name=complex_type_name,
                cleaned_name=cleaned_complex_type_name,
                name_snake_case=complex_type_name_snake_case,
                type_=entity_type,
                documentation=documentation_entries,
                properties=fhir_properties,
                is_back_bone_element="." in entity_type if entity_type else False,
            )
            fhir_entities.append(fhir_entity)
        return fhir_entities

    @staticmethod
    def generate_properties_for_class(
        inner_complex_type: OrderedDict[str, Any]
    ) -> List[FhirProperty]:
        properties: List[OrderedDict[str, Any]] = (
            inner_complex_type.get("xs:sequence").get("xs:element")  # type: ignore
            if inner_complex_type.get("xs:sequence")
            and inner_complex_type.get("xs:sequence").get("xs:element")  # type: ignore
            else []
        )
        if isinstance(properties, OrderedDict):
            properties = [properties]
        # combine element properties with choice properties
        choice_properties: List[OrderedDict[str, Any]] = (
            inner_complex_type.get("xs:sequence").get("xs:choice")  # type: ignore
            if inner_complex_type.get("xs:sequence")
            and inner_complex_type.get("xs:sequence").get("xs:choice")  # type: ignore
            else []
        )
        if isinstance(choice_properties, OrderedDict):
            choice_properties = [choice_properties]
        choice_properties = flatten([c["xs:element"] for c in choice_properties])
        properties.extend(choice_properties)

        fhir_properties: List[FhirProperty] = []
        property_: OrderedDict[str, Any]
        for property_ in properties:
            property_name: str = str(property_.get("@name"))
            min_occurs: str = str(
                property_.get("@minOccurs") if "@minOccurs" in property_ else 0
            )
            max_occurs: str = str(
                property_.get("@maxOccurs") if "@maxOccurs" in property_ else 1
            )
            property_type: str = str(property_.get("@type"))
            property_documentation_dict: Optional[OrderedDict[str, Any]] = (
                property_.get("xs:annotation").get("xs:documentation")  # type: ignore
                if property_.get("xs:annotation")
                else None
            )
            property_documentation: str = str(
                property_documentation_dict.get("#text")
                if property_documentation_dict
                else None
            )
            # print(
            #     f"{property_name}: {property_type} [{min_occurs}..{max_occurs}] // {property_documentation}"
            # )
            optional: bool = min_occurs == "0"
            is_list: bool = max_occurs == "unbounded"
            cleaned_type: str = property_type
            cleaned_type = cleaned_type.replace(".", "")
            if property_type and property_name and property_type != "None":
                fhir_properties.append(
                    FhirProperty(
                        name=FhirXmlSchemaParser.fix_python_keywords(property_name),
                        type_=property_type,
                        cleaned_type=cleaned_type
                        if cleaned_type not in FhirXmlSchemaParser.cleaned_type_mapping
                        else FhirXmlSchemaParser.cleaned_type_mapping[cleaned_type],
                        type_snake_case=FhirXmlSchemaParser.camel_to_snake(cleaned_type)
                        if cleaned_type not in FhirXmlSchemaParser.cleaned_type_mapping
                        else FhirXmlSchemaParser.camel_to_snake(cleaned_type),
                        optional=optional,
                        is_list=is_list,
                        documentation=[property_documentation],
                        fhir_type=None,
                        reference_target_resources=[],
                        reference_target_resources_names=[],
                        is_back_bone_element="." in property_type,
                        is_basic_type=cleaned_type
                        in FhirXmlSchemaParser.cleaned_type_mapping,
                        codeable_type=None,
                    )
                )
        return fhir_properties

    @staticmethod
    def fix_python_keywords(name: str) -> str:
        result: str = (
            name
            if name
            not in [
                "False",
                "None",
                "True",
                "and",
                "as",
                "assert",
                "async",
                "await",
                "break",
                "class",
                "continue",
                "def",
                "del",
                "elif",
                "else",
                "except",
                "finally",
                "for",
                "from",
                "global",
                "if",
                "import",
                "in",
                "is",
                "lambda",
                "nonlocal",
                "not",
                "or",
                "pass",
                "raise",
                "return",
                "try",
                "while",
                "with",
                "yield",
                "id",
                "type",
                "List",
            ]
            else f"{name}_"
        )
        if result and result[0].isdigit():
            result = "_" + result
        return result

    @staticmethod
    def get_all_property_types() -> List[FhirProperty]:
        data_dir: Path = Path(__file__).parent.joinpath("./")

        # first read fhir-all.xsd to get a list of resources
        de_xml_file: Path = (
            data_dir.joinpath("xsd")
            .joinpath("definitions.xml")
            .joinpath("dataelements.xml")
        )

        with open(de_xml_file, "r") as file:
            contents = file.read()
            result: OrderedDict[str, Any] = parse(contents)
            entries: List[OrderedDict[str, Any]] = result["Bundle"]["entry"]

            fhir_properties: List[FhirProperty] = []
            entry: OrderedDict[str, Any]
            for entry in entries:
                structure_definition: OrderedDict[str, Any] = entry["resource"][
                    "StructureDefinition"
                ]
                name: str = structure_definition["name"]["@value"]
                documentation: List[str] = structure_definition["description"]["@value"]
                # if isinstance(documentation, OrderedDict):
                #     documentation = [documentation]
                snapshot_element: OrderedDict[str, Any] = structure_definition[
                    "snapshot"
                ]["element"]
                types: List[OrderedDict[str, Any]] = snapshot_element["type"]
                if isinstance(types, OrderedDict):
                    types = [types]

                # There are 3 main cases:
                # 1. A simple scalar type
                # 2. A complex type
                # 3. A reference
                # 4. A codeable type
                # 5. A value set
                type_ = types[0]["code"]["@value"] if types else ""

                fhir_properties.append(
                    FhirProperty(
                        name=name,
                        type_=type_,
                        cleaned_type=type_,
                        type_snake_case=type_,
                        documentation=documentation,
                        is_back_bone_element=False,
                        codeable_type=None,
                        fhir_type=type_,
                        is_basic_type=False,
                        is_list=False,
                        optional=False,
                        reference_target_resources_names=[],
                        reference_target_resources=[],
                    )
                )

            return fhir_properties

    @staticmethod
    def get_types_for_references() -> List[FhirReferenceType]:
        data_dir: Path = Path(__file__).parent.joinpath("./")

        # first read fhir-all.xsd to get a list of resources
        de_xml_file: Path = (
            data_dir.joinpath("xsd")
            .joinpath("definitions.xml")
            .joinpath("dataelements.xml")
        )

        with open(de_xml_file, "r") as file:
            contents = file.read()
            result: OrderedDict[str, Any] = parse(contents)
            entries: List[OrderedDict[str, Any]] = result["Bundle"]["entry"]

            fhir_references: List[FhirReferenceType] = []
            entry: OrderedDict[str, Any]
            for entry in entries:
                structure_definition: OrderedDict[str, Any] = entry["resource"][
                    "StructureDefinition"
                ]
                # name: str = structure_definition["name"]["@value"]
                snapshot_element: OrderedDict[str, Any] = structure_definition[
                    "snapshot"
                ]["element"]
                types: List[OrderedDict[str, Any]] = snapshot_element["type"]
                if isinstance(types, OrderedDict):
                    types = [types]
                type_: OrderedDict[str, Any]
                for type_ in types:
                    type_code_obj = type_["code"]
                    type_code: str = type_code_obj["@value"]
                    if type_code.endswith("Reference"):
                        if "targetProfile" not in type_:
                            print(
                                f'ASSERT: targetProfile not in {type_} for {snapshot_element["path"]["@value"]}'
                            )
                        if "targetProfile" in type_:
                            target_profile_list: List[OrderedDict[str, Any]] = type_[
                                "targetProfile"
                            ]
                            if isinstance(target_profile_list, OrderedDict):
                                target_profile_list = [target_profile_list]
                            target_profiles: List[str] = [
                                c["@value"] for c in target_profile_list
                            ]
                            target_resources: List[str] = [
                                c.split("/")[-1] for c in target_profiles
                            ]
                            fhir_reference: FhirReferenceType = FhirReferenceType(
                                # parent_entity_name=name_parts[0],
                                # property_name=name_parts[1],
                                target_resources=target_resources,
                                path=snapshot_element["path"]["@value"],
                            )
                            fhir_references.append(fhir_reference)
            return fhir_references

    @staticmethod
    def get_types_for_codeable_concepts() -> List[FhirCodeableType]:
        data_dir: Path = Path(__file__).parent.joinpath("./")

        # first read fhir-all.xsd to get a list of resources
        de_xml_file: Path = (
            data_dir.joinpath("xsd")
            .joinpath("definitions.xml")
            .joinpath("dataelements.xml")
        )

        with open(de_xml_file, "r") as file:
            contents = file.read()
            result: OrderedDict[str, Any] = parse(contents)
            entries: List[OrderedDict[str, Any]] = result["Bundle"]["entry"]

            fhir_codeable_types: List[FhirCodeableType] = []
            entry: OrderedDict[str, Any]
            for entry in entries:
                structure_definition: OrderedDict[str, Any] = entry["resource"][
                    "StructureDefinition"
                ]
                # name: str = structure_definition["name"]["@value"]
                snapshot_element: OrderedDict[str, Any] = structure_definition[
                    "snapshot"
                ]["element"]
                if "binding" in snapshot_element:
                    types: List[OrderedDict[str, Any]] = snapshot_element["type"]
                    if isinstance(types, OrderedDict):
                        types = [types]
                    type_: OrderedDict[str, Any]
                    if types:
                        type_ = types[0]
                        if type_["code"]["@value"] in [
                            "Coding",
                            "CodeableConcept",
                            "code",
                        ]:
                            bindings: List[OrderedDict[str, Any]] = snapshot_element[
                                "binding"
                            ]
                            if isinstance(bindings, OrderedDict):
                                bindings = [bindings]
                            binding: OrderedDict[str, Any]
                            for binding in bindings:
                                extension_code_list = binding["extension"]
                                if isinstance(extension_code_list, OrderedDict):
                                    extension_code_list = [extension_code_list]
                                field_name: str = "@url"
                                url: str = "http://hl7.org/fhir/StructureDefinition/elementdefinition-bindingName"
                                value_set_url = (
                                    binding["valueSet"]["@value"]
                                    if "valueSet" in binding
                                    else None
                                )
                                codeable_type_list: List[OrderedDict[str, Any]] = [
                                    bind
                                    for bind in extension_code_list
                                    if bind[field_name] == url
                                ]
                                if codeable_type_list:
                                    codeable_type_obj: OrderedDict[
                                        str, Any
                                    ] = codeable_type_list[0]
                                    codeable_type: str = codeable_type_obj[
                                        "valueString"
                                    ]["@value"]
                                    fhir_codeable_types.append(
                                        FhirCodeableType(
                                            path=snapshot_element["path"]["@value"],
                                            codeable_type=codeable_type,
                                            codeable_type_url=value_set_url,
                                            is_codeable_concept=type_["code"]["@value"]
                                            in ["Coding", "CodeableConcept"],
                                        )
                                    )
            return fhir_codeable_types

    @staticmethod
    def get_value_sets() -> List[FhirValueSet]:
        data_dir: Path = Path(__file__).parent.joinpath("./")

        fhir_value_sets: List[FhirValueSet] = []

        fhir_v3_code_systems: List[
            FhirValueSet
        ] = FhirXmlSchemaParser.get_v3_code_systems(data_dir)

        value_sets_file: Path = (
            data_dir.joinpath("xsd")
            .joinpath("definitions.xml")
            .joinpath("valuesets.xml")
        )
        with open(value_sets_file, "r") as file:
            contents: str = file.read()
            result: OrderedDict[str, Any] = parse(contents)
            entries: List[OrderedDict[str, Any]] = result["Bundle"]["entry"]

        entry: OrderedDict[str, Any]
        for entry in entries:
            value_set_resource = entry["resource"]
            is_code_system = "CodeSystem" in value_set_resource
            value_set = (
                value_set_resource["CodeSystem"]
                if is_code_system
                else value_set_resource["ValueSet"]
            )
            id_ = value_set["id"]["@value"]
            name: str = value_set["name"]["@value"].replace("v3.", "")
            url = value_set["url"]["@value"]
            value_set_url = (
                value_set["valueSet"]["@value"] if "valueSet" in value_set else None
            )
            fhir_concepts: List[FhirValueSetConcept] = []
            if "concept" in value_set:
                concepts: List[OrderedDict[str, Any]] = value_set["concept"]
                if isinstance(concepts, OrderedDict):
                    concepts = [concepts]
                concept: OrderedDict[str, Any]
                for concept in concepts:
                    fhir_concepts.append(FhirXmlSchemaParser.create_concept(concept))
            if "compose" in value_set:
                compose_includes: List[OrderedDict[str, Any]] = value_set["compose"][
                    "include"
                ]
                if isinstance(compose_includes, OrderedDict):
                    compose_includes = [compose_includes]
                compose_include: OrderedDict[str, Any]
                for compose_include in compose_includes:
                    is_code_system = "system" in compose_include
                    # is_value_set = "valueSet" in compose_include
                    if is_code_system:
                        compose_include_code_system: str = compose_include["system"][
                            "@value"
                        ]
                        # find the corresponding item in code systems
                        code_systems: List[FhirValueSet] = [
                            c
                            for c in fhir_v3_code_systems
                            if c.url == compose_include_code_system
                        ]
                        if code_systems:
                            for code_system in code_systems:
                                fhir_concepts.extend(code_system.concepts)
                    if "concept" in compose_include:
                        concepts = compose_include["concept"]
                        if isinstance(concepts, OrderedDict):
                            concepts = [concepts]
                        for concept in concepts:
                            fhir_concepts.append(
                                FhirXmlSchemaParser.create_concept(concept)
                            )
            if "/" in name:
                name = name.replace("/", "_or_")
            if "/" not in name:
                fhir_value_sets.append(
                    FhirValueSet(
                        id_=id_,
                        name=name,
                        name_snake_case=FhirXmlSchemaParser.camel_to_snake(
                            FhirXmlSchemaParser.clean_name(name)
                        ),
                        cleaned_name=FhirXmlSchemaParser.clean_name(name) + "Code",
                        concepts=fhir_concepts,
                        url=url,
                        value_set_url=value_set_url,
                    )
                )
            else:
                print(f"WARNING: value set {name} contains /")

        fhir_v2_code_systems: List[
            FhirValueSet
        ] = FhirXmlSchemaParser.get_v2_code_systems(data_dir)

        fhir_value_sets.extend(
            [
                c
                for c in fhir_v2_code_systems
                if c.cleaned_name not in [b.cleaned_name for b in fhir_value_sets]
            ]
        )
        fhir_value_sets.extend(
            [
                c
                for c in fhir_v3_code_systems
                if c.cleaned_name not in [b.cleaned_name for b in fhir_value_sets]
            ]
        )

        return fhir_value_sets

    @staticmethod
    def create_concept(concept: OrderedDict[str, Any]) -> FhirValueSetConcept:
        code: str = concept["code"]["@value"]
        display: str = concept["display"]["@value"] if "display" in concept else code
        cleaned_display: str = FhirXmlSchemaParser.clean_name(display)
        definition: Optional[str] = (
            concept["definition"]["@value"] if "definition" in concept else None
        )
        return FhirValueSetConcept(
            code=code,
            display=display,
            cleaned_display=cleaned_display,
            definition=definition,
        )

    @staticmethod
    def clean_name(display: str) -> str:
        cleaned_display: str = "".join(
            [c[:1].upper() + c[1:] for c in display.split(" ")]
        )
        cleaned_display = re.sub("[^0-9a-zA-Z]+", "_", cleaned_display)
        cleaned_display = FhirXmlSchemaParser.fix_python_keywords(cleaned_display)
        return cleaned_display

    @staticmethod
    def get_v3_code_systems(data_dir: Path) -> List[FhirValueSet]:
        fhir_value_sets: List[FhirValueSet] = []

        value_sets_json_file: Path = (
            data_dir.joinpath("xsd")
            .joinpath("definitions.xml")
            .joinpath("v3-codesystems.xml")
        )
        with open(value_sets_json_file, "r") as file:
            contents: str = file.read()
            result: OrderedDict[str, Any] = parse(contents)
            entries: List[OrderedDict[str, Any]] = result["Bundle"]["entry"]

        value_set_entry: Dict[str, Any]
        for value_set_entry in entries:
            value_set_entry_resource: OrderedDict[str, Any] = value_set_entry[
                "resource"
            ]
            is_code_system: bool = "CodeSystem" in value_set_entry_resource
            is_value_set: bool = "ValueSet" in value_set_entry_resource
            value_set: Dict[str, Any] = (
                value_set_entry_resource["ValueSet"]
                if is_value_set
                else value_set_entry_resource["CodeSystem"]
                if is_code_system
                else value_set_entry["resource"]
            )
            id_: str = value_set["id"]["@value"]
            name: str = value_set["name"]["@value"].replace("v3.", "")
            url = value_set["url"]["@value"]
            fhir_concepts: List[FhirValueSetConcept] = []
            # value_set_url = None  # value_set["valueSet"]
            if "concept" in value_set:
                concepts_list: List[OrderedDict[str, Any]] = value_set["concept"]
                if isinstance(concepts_list, OrderedDict):
                    concepts_list = [concepts_list]
                concept: OrderedDict[str, Any]
                for concept in concepts_list:
                    code: str = str(concept["code"]["@value"])
                    display: str = str(
                        concept["display"]["@value"]
                        if "display" in concept
                        else concept["code"]["@value"]
                    )
                    cleaned_display: str = (
                        "".join([c.capitalize() for c in display.split(" ")])
                        .replace("-", "")
                        .replace(".", "")
                        .replace("&", "")
                        .replace("'", "")
                        .replace("(", "")
                        .replace(",", "")
                        .replace(")", "")
                        .replace("/", "")
                        .replace("+", "")
                    )
                    cleaned_display = FhirXmlSchemaParser.fix_python_keywords(
                        cleaned_display
                    )
                    definition: Optional[str] = (
                        concept["definition"]["@value"]
                        if "definition" in concept
                        else None
                    )
                    fhir_concepts.append(
                        FhirValueSetConcept(
                            code=code,
                            display=display,
                            cleaned_display=cleaned_display,
                            definition=definition,
                        )
                    )
            fhir_value_sets.append(
                FhirValueSet(
                    id_=id_,
                    name=name,
                    name_snake_case=FhirXmlSchemaParser.camel_to_snake(name),
                    cleaned_name=FhirXmlSchemaParser.clean_name(name),
                    concepts=fhir_concepts,
                    url=url,
                    value_set_url="",
                )
            )
        return fhir_value_sets

    @staticmethod
    def get_v2_code_systems(data_dir: Path) -> List[FhirValueSet]:
        fhir_value_sets: List[FhirValueSet] = []

        value_sets_json_file: Path = (
            data_dir.joinpath("xsd")
            .joinpath("definitions.xml")
            .joinpath("v2-tables.xml")
        )
        with open(value_sets_json_file, "r") as file:
            contents: str = file.read()
            result: OrderedDict[str, Any] = parse(contents)
            entries: List[OrderedDict[str, Any]] = result["Bundle"]["entry"]

        value_set_entry: Dict[str, Any]
        for value_set_entry in entries:
            value_set_entry_resource: OrderedDict[str, Any] = value_set_entry[
                "resource"
            ]
            is_code_system: bool = "CodeSystem" in value_set_entry_resource
            is_value_set: bool = "ValueSet" in value_set_entry_resource
            value_set: Dict[str, Any] = (
                value_set_entry_resource["ValueSet"]
                if is_value_set
                else value_set_entry_resource["CodeSystem"]
                if is_code_system
                else value_set_entry["resource"]
            )
            id_: str = value_set["id"]["@value"]
            name: str = value_set["name"]["@value"].replace(".", "_")
            url = value_set["url"]["@value"]
            fhir_concepts: List[FhirValueSetConcept] = []
            # value_set_url = None  # value_set["valueSet"]
            if "concept" in value_set:
                concepts_list: List[OrderedDict[str, Any]] = value_set["concept"]
                if isinstance(concepts_list, OrderedDict):
                    concepts_list = [concepts_list]
                concept: OrderedDict[str, Any]
                for concept in concepts_list:
                    code: str = str(concept["code"]["@value"])
                    display: str = str(
                        concept["display"]["@value"]
                        if "display" in concept
                        else concept["code"]["@value"]
                    )
                    cleaned_display: str = (
                        "".join([c.capitalize() for c in display.split(" ")])
                        .replace("-", "")
                        .replace(".", "")
                        .replace("&", "")
                        .replace("'", "")
                        .replace("(", "")
                        .replace(",", "")
                        .replace(")", "")
                        .replace("/", "")
                        .replace("+", "")
                    )
                    cleaned_display = FhirXmlSchemaParser.fix_python_keywords(
                        cleaned_display
                    )
                    definition: Optional[str] = (
                        concept["definition"]["@value"]
                        if "definition" in concept
                        else None
                    )
                    fhir_concepts.append(
                        FhirValueSetConcept(
                            code=code,
                            display=display,
                            cleaned_display=cleaned_display,
                            definition=definition,
                        )
                    )
            fhir_value_sets.append(
                FhirValueSet(
                    id_=id_,
                    name=name,
                    name_snake_case=FhirXmlSchemaParser.camel_to_snake(name),
                    cleaned_name=FhirXmlSchemaParser.clean_name(name),
                    concepts=fhir_concepts,
                    url=url,
                    value_set_url="",
                )
            )
        return fhir_value_sets
