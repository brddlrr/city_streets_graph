import xml.etree.cElementTree as ET
import urllib.request
from src.node import Node
legalWays = {"motorway", "motorway_link", "trunk", "trunk_link", "primary",
             "primary_link", "secondary", "secondary_link", "tertiary", "tertiary_link",
             "unclassified", "road", "residential"}


def parse_xml(xml_file):
    tree = ET.ElementTree(file=xml_file)
    root = tree.getroot()
    nodesInWays = list()
    ways = list()
    count = 0
    for way in root.iter("way"):
        flag = False
        for tag in way.iter("tag"):
            atr = tag.attrib
            if (atr.get("k") == "highway") and (atr.get("v") in legalWays):
                flag = True
        if flag:
            nodes = list()
            for i in way.iter("nd"):
                nodes.append(int(i.attrib.get("ref")))
            fromID = nodes[0]
            fromNode = None
            for i in nodesInWays:
                if i.ndID == fromID:
                    fromNode = i
                    break
            if fromNode is None:
                fromNode = get_node(fromID)
                count += 1
                fromNode.set_id(count)
                nodesInWays.append(fromNode)

            for j in nodes[1:]:
                toID = j
                toNode = None
                for i in nodesInWays:
                    if toID == i.ndID:
                        toNode = i
                        break
                if toNode is None:
                    toNode = get_node(toID)
                    count += 1
                    toNode.set_id(count)
                    nodesInWays.append(toNode)
                ways.append((fromNode.id, toNode.id))
                ways.append((toNode.id, fromNode.id))
                fromNode = toNode
    return sorted(nodesInWays, key=sort_by_id), ways


def get_node(node_id):
    response = urllib.request.urlopen('https://www.openstreetmap.org/api/0.6/node/'+str(node_id))
    xml = str(response.read().decode('utf-8'))
    xml = xml[xml.index('lat'):]
    l = xml.split(" ")
    lat = l[0]
    lon = l[1]
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.'}
    res = ""
    for i in lat:
        if i in digits:
            res += i
    lat = float(res)
    res = ""
    for i in lon:
        if i in digits:
            res += i
    lon = float(res)
    print(str(node_id)+" "+str(lat)+" "+str(lon))
    return Node(node_id, lat, lon)


def sort_by_id(node):
    return node.id



