import os
from pathlib import Path
import shutil
from os import path

from spark_auto_mapper_fhir.generator.fhir_xml_schema_parser import FhirXmlSchemaParser


def main() -> int:
    data_dir: Path = Path(__file__).parent.joinpath("./")

    # clean out old stuff
    resources_folder = data_dir.joinpath("resources")
    if os.path.exists(resources_folder):
        shutil.rmtree(resources_folder)
    os.mkdir(resources_folder)
    resources_folder.joinpath("__init__.py").touch()

    complex_types_folder = data_dir.joinpath("complex_types")
    if os.path.exists(complex_types_folder):
        shutil.rmtree(complex_types_folder)
    os.mkdir(complex_types_folder)
    complex_types_folder.joinpath("__init__.py").touch()

    backbone_elements_folder = data_dir.joinpath("backbone_elements")
    if os.path.exists(backbone_elements_folder):
        shutil.rmtree(backbone_elements_folder)
    os.mkdir(backbone_elements_folder)
    backbone_elements_folder.joinpath("__init__.py").touch()

    simple_types_folder = data_dir.joinpath("simple_types")
    if os.path.exists(simple_types_folder):
        shutil.rmtree(simple_types_folder)
    os.mkdir(simple_types_folder)
    simple_types_folder.joinpath("__init__.py").touch()

    fhir_entities = FhirXmlSchemaParser.generate_classes()

    # now print the result
    for fhir_entity in fhir_entities:
        # use template to generate new code files
        resource_name: str = fhir_entity.cleaned_name
        entity_file_name = FhirXmlSchemaParser.camel_to_snake(resource_name)
        if fhir_entity.type_ == "DomainResource":
            with open(data_dir.joinpath("template.resource.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )

            file_path = resources_folder.joinpath(f"{entity_file_name}.py")
            print(f"Writing resource: {entity_file_name} to {file_path}...")
            # print(result)
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif fhir_entity.type_ == "Resource":
            with open(data_dir.joinpath("template.resource.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )

            file_path = resources_folder.joinpath(f"{entity_file_name}.py")
            print(f"Writing resource: {entity_file_name} to {file_path}...")
            # print(result)
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif fhir_entity.type_ == "BackboneElement":
            with open(data_dir.joinpath("template.complex_type.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )

            file_path = backbone_elements_folder.joinpath(f"{entity_file_name}.py")
            print(
                f"Writing backbone_elements_folder: {entity_file_name} to {file_path}..."
            )
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif fhir_entity.type_ == "Element":  # valueset
            with open(data_dir.joinpath("template.complex_type.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )

            file_path = complex_types_folder.joinpath(f"{entity_file_name}.py")
            print(f"Writing complex_type: {entity_file_name} to {file_path}...")
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        elif fhir_entity.type_ in ["Quantity"]:  # valueset
            with open(data_dir.joinpath("template.complex_type.jinja2"), "r") as file:
                template_contents = file.read()
                from jinja2 import Template

                template = Template(
                    template_contents, trim_blocks=True, lstrip_blocks=True
                )
                result = template.render(
                    fhir_entity=fhir_entity,
                )

            file_path = complex_types_folder.joinpath(f"{entity_file_name}.py")
            print(f"Writing complex_type: {entity_file_name} to {file_path}...")
            if not path.exists(file_path):
                with open(file_path, "w") as file2:
                    file2.write(result)
        else:
            assert False, f"{resource_name}: {fhir_entity.type_} is not supported"
        # print(result)
    return 0


if __name__ == "__main__":
    exit(main())
