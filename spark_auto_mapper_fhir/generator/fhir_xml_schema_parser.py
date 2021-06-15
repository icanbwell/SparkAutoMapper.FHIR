import dataclasses
from pathlib import Path
from typing import OrderedDict, Any, List, Union, Dict, Optional

from xmltodict import parse


@dataclasses.dataclass
class FhirProperty:
    name: str
    type_: str
    optional: bool
    is_list: bool
    documentation: List[str]


@dataclasses.dataclass
class FhirEntity:
    name: str
    properties: List[FhirProperty]
    documentation: List[str]
    type_: str


class FhirXmlSchemaParser:
    @staticmethod
    def generate_classes() -> List[FhirEntity]:
        data_dir: Path = Path(__file__).parent.joinpath("./")
        patient_xsd_file: Path = data_dir.joinpath("xsd").joinpath("patient.xsd")
        # schema = XMLSchema(str(patient_xsd_file))
        # pprint(schema.to_dict)
        with open(patient_xsd_file, "r") as file:
            contents = file.read()
            result = parse(contents)
            # pprint(result)
        fhir_entities: List[FhirEntity] = []
        complex_types: List[OrderedDict[str, Any]] = result["xs:schema"][
            "xs:complexType"
        ]
        complex_type: OrderedDict[str, Any]
        for complex_type in complex_types:
            complex_type_name: str = complex_type["@name"].replace(".", "")
            print(f"========== {complex_type_name} ===========")
            documentation_items: List[OrderedDict[str, Any]] = complex_type[
                "xs:annotation"
            ]["xs:documentation"]
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
            if inner_complex_type:
                inner_complex_type_type: str = str(inner_complex_type.get("@base"))
                print(f"type={inner_complex_type_type}")
                properties: List[OrderedDict[str, Any]] = (
                    inner_complex_type.get("xs:sequence").get("xs:element")  # type: ignore
                    if inner_complex_type.get("xs:sequence")
                    else []
                )

                fhir_properties: List[FhirProperty] = []
                property_: OrderedDict[str, Any]
                for property_ in properties:
                    property_name: str = str(property_.get("@name"))
                    min_occurs: str = str(property_.get("@minOccurs"))
                    max_occurs: str = str(property_.get("@maxOccurs"))
                    type_: str = str(property_.get("@type"))
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
                        f"{property_name}: {type_} [{min_occurs}..{max_occurs}] // {property_documentation}"
                    )
                    optional: bool = min_occurs == "0"
                    is_list: bool = max_occurs == "unbounded"
                    cleaned_type: str = type_
                    cleaned_type_mapping: Dict[str, str] = {
                        "boolean": "FhirBoolean",
                        "date": "FhirDate",
                        "dateTime": "FhirDateTime",
                        "integer": "FhirInteger",
                    }
                    if cleaned_type in cleaned_type_mapping.keys():
                        cleaned_type = cleaned_type_mapping[cleaned_type]
                    cleaned_type = cleaned_type.replace(".", "")
                    print(
                        f"{property_name}:"
                        f"{'Optional[' if optional else ''}"
                        f"{'FhirList[' if is_list else ''}"
                        f"{cleaned_type}"
                        f"{']' if is_list else ''}"
                        f"{'] = None,' if optional else ','}"
                    )
                    fhir_properties.append(
                        FhirProperty(
                            name=property_name,
                            type_=cleaned_type,
                            optional=optional,
                            is_list=is_list,
                            documentation=[property_documentation],
                        )
                    )
                fhir_entity: FhirEntity = FhirEntity(
                    name=complex_type_name,
                    type_=inner_complex_type_type,
                    documentation=documentation_entries,
                    properties=fhir_properties,
                )
                fhir_entities.append(fhir_entity)
        return fhir_entities
