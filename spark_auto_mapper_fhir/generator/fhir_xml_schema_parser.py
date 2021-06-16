import dataclasses
from pathlib import Path
from typing import OrderedDict, Any, List, Union, Dict, Optional
import re
from xmltodict import parse


@dataclasses.dataclass
class SmartName:
    name: str
    snake_case_name: str


@dataclasses.dataclass
class FhirReferenceType:
    # parent_entity_name: str
    # property_name: str
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


@dataclasses.dataclass
class FhirEntity:
    fhir_name: str
    cleaned_name: str
    name_snake_case: str
    properties: List[FhirProperty]
    documentation: List[str]
    type_: Optional[str]
    is_back_bone_element: bool


class FhirXmlSchemaParser:
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
        fhir_xsd_all_file: Path = data_dir.joinpath("xsd").joinpath("fhir-all.xsd")
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
            resource_xsd_file: Path = data_dir.joinpath("xsd").joinpath(
                resource_xsd_file_name
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
                    print("foo")
                else:
                    fhir_property.fhir_type = property_type_mapping[fhir_property.type_]

        # and the target resources for references
        references: List[
            FhirReferenceType
        ] = FhirXmlSchemaParser.get_types_for_references()

        reference: FhirReferenceType
        for reference in references:
            name_parts: List[str] = reference.path.split(".")
            if len(name_parts) == 2:
                parent_entity_name: str = name_parts[0]
                property_name: str = name_parts[1]
                # find the corresponding fhir entity
                fhir_entity_list = [
                    f for f in fhir_entities if f.fhir_name == parent_entity_name
                ]
                if fhir_entity_list:
                    fhir_entity = fhir_entity_list[0]
                    fhir_property_list = [
                        p for p in fhir_entity.properties if p.name == property_name
                    ]

                    if fhir_property_list:
                        fhir_property = fhir_property_list[0]
                        fhir_property.reference_target_resources = [
                            SmartName(
                                name=c,
                                snake_case_name=FhirXmlSchemaParser.camel_to_snake(c),
                            )
                            for c in reference.target_resources
                        ]
                        fhir_property.reference_target_resources_names = [
                            c.name for c in fhir_property.reference_target_resources
                        ]

        return fhir_entities

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
                print("foo")
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
            else []
        )
        if isinstance(properties, OrderedDict):
            properties = [properties]
        fhir_properties: List[FhirProperty] = []
        property_: OrderedDict[str, Any]
        for property_ in properties:
            property_name: str = str(property_.get("@name"))
            min_occurs: str = str(property_.get("@minOccurs"))
            max_occurs: str = str(property_.get("@maxOccurs"))
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
            print(
                f"{property_name}: {property_type} [{min_occurs}..{max_occurs}] // {property_documentation}"
            )
            optional: bool = min_occurs == "0"
            is_list: bool = max_occurs == "unbounded"
            cleaned_type: str = property_type
            cleaned_type_mapping: Dict[str, str] = {
                "boolean": "FhirBoolean",
                "date": "FhirDate",
                "dateTime": "FhirDateTime",
                "integer": "FhirInteger",
                "string": "FhirString",
            }
            cleaned_type = cleaned_type.replace(".", "")
            print(
                f"{property_name}:"
                f"{'Optional[' if optional else ''}"
                f"{'FhirList[' if is_list else ''}"
                f"{cleaned_type}"
                f"{']' if is_list else ''}"
                f"{'] = None,' if optional else ','}"
            )
            if property_type and property_name and property_type != "None":
                fhir_properties.append(
                    FhirProperty(
                        name=property_name,
                        type_=property_type,
                        cleaned_type=cleaned_type
                        if cleaned_type not in cleaned_type_mapping
                        else cleaned_type_mapping[cleaned_type],
                        type_snake_case=FhirXmlSchemaParser.camel_to_snake(cleaned_type)
                        if cleaned_type not in cleaned_type_mapping
                        else cleaned_type,
                        optional=optional,
                        is_list=is_list,
                        documentation=[property_documentation],
                        fhir_type=None,
                        reference_target_resources=[],
                        reference_target_resources_names=[],
                        is_back_bone_element="." in property_type,
                    )
                )
        return fhir_properties

    @staticmethod
    def get_types_for_references() -> List[FhirReferenceType]:
        data_dir: Path = Path(__file__).parent.joinpath("./")

        # first read fhir-all.xsd to get a list of resources
        de_xml_file: Path = data_dir.joinpath("xsd").joinpath("dataelements.xml")

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
                            print("foo")
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
                            print("foo")
                            fhir_reference: FhirReferenceType = FhirReferenceType(
                                # parent_entity_name=name_parts[0],
                                # property_name=name_parts[1],
                                target_resources=target_resources,
                                path=snapshot_element["path"]["@value"],
                            )
                            fhir_references.append(fhir_reference)
                print(entry)
            return fhir_references
