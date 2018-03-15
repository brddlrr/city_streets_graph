from src.parseXML import parse_xml
from src.output import output_to_csv

def main():
    nodes, ways = parse_xml("../xml/saratov.osm")
    output_to_csv(nodes, ways)


if __name__ == '__main__':
    main()
