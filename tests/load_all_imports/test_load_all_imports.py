import importlib
import pkgutil
from typing import Any, Dict, Tuple, Union


def import_submodules(
    package: Union[Any, str], recursive: bool = True
) -> Tuple[Dict[str, Any], Dict[str, Any]]:
    """Import all submodules of a module, recursively, including subpackages
    from https://stackoverflow.com/questions/3365740/how-to-import-all-submodules

    :param recursive:
    :param package: package (name or actual module)
    :type package: str | module
    :rtype: dict[str, types.ModuleType]
    """
    if isinstance(package, str):
        package = importlib.import_module(package)
    results = {}
    errors = {}
    # noinspection Mypy
    for loader, name, is_pkg in pkgutil.walk_packages(package.__path__):  # type: ignore
        full_name = package.__name__ + "." + name
        try:
            results[full_name] = importlib.import_module(full_name)
        except Exception as e:
            print(f"{full_name}: {e}")
            errors[full_name] = e
        if recursive and is_pkg:
            submodules, errors_in_submodules = import_submodules(full_name)
            results.update(submodules)
            errors.update(errors_in_submodules)
    return results, errors


def test_load_all_imports() -> None:
    import spark_auto_mapper_fhir

    submodules, errors_in_submodules = import_submodules(spark_auto_mapper_fhir)

    print(submodules)

    assert len(errors_in_submodules) == 0, f"{errors_in_submodules!r}"
