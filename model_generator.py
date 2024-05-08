import argparse
from core.parser import DBMLDiagramParser
from core.utils import JinjaTemplateDiscovery
from core.handlers import DBMLToDjango

def main(dbml_file, root_directory):
    """
    Main function to convert a DBML file to Django models using specified templates.

    Args:
        dbml_file (str): Path to the DBML file to be converted.
        root_directory (str): Root directory where the converted files will be placed.
    """
    try:
        dbml_parser = DBMLDiagramParser()
        diagram = dbml_parser.read_diagram(dbml_file)
        discovery = JinjaTemplateDiscovery()
        dbml = DBMLToDjango(diagram, discovery)
        dbml.run_conversion(root_directory)
    except Exception as e:
        print(f"Error processing file: {e}")
        return 1

    return 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert DBML to Django models.")
    parser.add_argument("-f", "--dbml_file", type=str, required=True, help="The path of the DBML file to process")
    parser.add_argument("-d", "--root_directory", type=str, required=True, help="The root directory name for the output")

    args = parser.parse_args()

    main(args.dbml_file, args.root_directory)
