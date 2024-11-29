import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.lines import Line2D, lineMarkers
import numpy as np

Interchange_Station_Color = "#ffffff"
Piccadilly_Circus_Color = "#001aff" # deep blue
Central_Color = "#ff4f4f" # red
Bakerloo_Color = "#a85b02" # yellow brown
Northern_Color = "#000000" # black

TransportGraph = nx.Graph()

def add_stations(stations):
    for i in stations:
        x = stations[i][0]
        y = stations[i][1]
        color = stations[i][2]
        TransportGraph.add_node(i, npos=(x, y), ccn=color)

def add_routes(routes):
    for i in routes:
        start_station = i
        end_station = routes[i][0]
        distance = routes[i][1]
        color = routes[i][2]
        TransportGraph.add_edge(start_station, end_station, cce=color, weight=distance)

def add_stations_name(stations):
    for i in stations:
        x = stations[i][3]
        y = stations[i][4]
        plt.text(x, y, s=i, fontsize='12')


# Key pair is node name, value pair is the position x, y, and the color
Piccadilly_Circus_Nodes = {
        "Hyde Park Corner":[32, 18, Piccadilly_Circus_Color, 33, 17],
        "Green Park":[39, 25, Piccadilly_Circus_Color, 36, 27],
        "Piccadilly Circus":[52, 25, Interchange_Station_Color, 52, 27],
        "Leicester Square":[62, 25, Interchange_Station_Color, 63, 24],
        "Convent Garden":[68, 30, Piccadilly_Circus_Color, 69, 29],
        "Holborn":[75, 35, Interchange_Station_Color, 73, 37]
    }
add_stations(Piccadilly_Circus_Nodes)

Central_Nodes = {
        "Bond Street":[35, 40, Central_Color, 32, 42],
        "Oxford Circus":[46, 40, Interchange_Station_Color, 47, 41],
        "Tottenham Court Road":[58, 35, Interchange_Station_Color, 59, 37],
        "Chancery Lane":[82, 33, Central_Color, 79, 35],
        "St Paul's":[100, 33, Central_Color, 98, 35],
    }
add_stations(Central_Nodes)

Bakerloo_Nodes = {
        "Baker Street":[33, 60, Bakerloo_Color, 30, 62],
        "Regent's Park": [40, 50, Bakerloo_Color, 41, 51],
        "Charing Cross":[58, 15, Interchange_Station_Color, 59, 15],
        "Embankment":[64, 10, Bakerloo_Color, 65, 10],
    }
add_stations(Bakerloo_Nodes)

Northern_Node = {
        "Warren Street":[58, 75, Northern_Color, 55, 77],
        "Goodge Street":[58, 50, Northern_Color, 59, 50],
        "Waterloo":[58, -5, Northern_Color, 59, -5],
    }
add_stations(Northern_Node)

# -----------------------------------------------------------------------------------------

# Key pair is a start station, value pair is a list contain end station, a distance (weight), and the color
# Piccadilly Circus key (from Hyde Park Corner to Holborn)
Piccadilly_Circus_Edge = {
    "Hyde Park Corner":[ "Green Park",0.74, Piccadilly_Circus_Color],
    "Green Park":["Piccadilly Circus",0.86, Piccadilly_Circus_Color],
    "Piccadilly Circus":["Leicester Square",0.53, Piccadilly_Circus_Color],
    "Leicester Square":["Convent Garden",0.26, Piccadilly_Circus_Color],
    "Convent Garden":["Holborn",0.57, Piccadilly_Circus_Color],
}
add_routes(Piccadilly_Circus_Edge)

# Central way (from Marble arch to St Paul's)
Central_Edge = {
    "Bond Street":["Oxford Circus",0.65, Central_Color],
    "Oxford Circus":["Tottenham Court Road",0.57, Central_Color],
    "Tottenham Court Road":["Holborn",0.91, Central_Color],
    "Holborn":["Chancery Lane",0.42, Central_Color],
    "Chancery Lane":["St Paul's",1.01, Central_Color],
}
add_routes(Central_Edge)

# Bakerloo way (from Baker Street to Embankment)
Bakerloo_Edge = {
    "Baker Street":["Regent's Park",0.88, Bakerloo_Color],
    "Regent's Park":["Oxford Circus",0.87, Bakerloo_Color],
    "Oxford Circus":["Piccadilly Circus",0.97, Bakerloo_Color],
    "Piccadilly Circus":["Charing Cross",0.55, Bakerloo_Color],
    "Charing Cross":["Embankment",0.37, Bakerloo_Color],
}
add_routes(Bakerloo_Edge)

# Northern way (from Warren Street to Waterloo)
Northern_Edge = {
    "Warren Street":["Goodge Street",1.68, Northern_Color],
    "Goodge Street":["Tottenham Court Road",0.64, Northern_Color],
    "Tottenham Court Road":["Leicester Square",0.39, Northern_Color],
    "Leicester Square":["Charing Cross",0.48, Northern_Color],
    "Charing Cross":["Waterloo",0.97, Northern_Color],
}
add_routes(Northern_Edge)

pos = nx.get_node_attributes(TransportGraph, 'npos')
nodeColor= nx.get_node_attributes(TransportGraph, 'ccn')
edgeColor= nx.get_edge_attributes(TransportGraph, 'cce')
edgeWeight= nx.get_edge_attributes(TransportGraph, 'weight')



nodeColorList = list(nodeColor.values())
edgeColorList = list(edgeColor.values())

# increase the node size of the interchange station
nodeSizeList = []
for index, value in enumerate(nodeColorList):
    if(value==Interchange_Station_Color):
        nodeSizeList.append(200)
    else:
        nodeSizeList.append(100)

plt.figure(figsize = (19.2,10.8))

# Piccadilly Circus
add_stations_name(Piccadilly_Circus_Nodes)

# Central
add_stations_name(Central_Nodes)

# Bakerloo
add_stations_name(Bakerloo_Nodes)

# Northern
add_stations_name(Northern_Node)


plt.text(50, 90, s='London underground railways map (km)', rotation=0, fontweight='bold', color=Piccadilly_Circus_Color, fontsize='20')
plt.text(100, 3, s='Key', rotation=0, fontweight='bold', fontsize='15')

route_distance_dict = nx.get_edge_attributes(TransportGraph, 'weight')
distance_route_list = list(route_distance_dict.values())

distance_route_array = np.array(distance_route_list, dtype=float)

# Calculate total length of the graph
total_length_distance_routes = round(distance_route_array.sum(), 2)

# Calculate average of total length of the graph
average_length_distance_routes = round(distance_route_array.mean(), 2)

# Calculate standard deviation total length of the graph
std_length_distance_routes = round(distance_route_array.std(), 2)


plt.text(26, 0, s=f'total length: {total_length_distance_routes} km', fontsize='15')
plt.text(26, -5, s=f'average length: {average_length_distance_routes} km ', fontsize='15')
plt.text(26, -10, s=f'standard deviation: {std_length_distance_routes} km', fontsize='15')

nx.draw_networkx_nodes(TransportGraph, pos, node_color= nodeColorList, edgecolors= "black", node_size=nodeSizeList)
nx.draw_networkx_edges(TransportGraph, pos, edge_color= edgeColorList, width=5)
nx.draw_networkx_edge_labels(TransportGraph, pos, edgeWeight, font_size=10)

Key = [
    Line2D([], [], color=Bakerloo_Color, label="Bakerloo", linewidth=3),
    Line2D([], [], color=Central_Color, label="Central", linewidth=3),
    Line2D([], [], color=Northern_Color, label="Northern", linewidth=3),
    Line2D([], [], color=Piccadilly_Circus_Color, label="Piccadilly", linewidth=3),
    Line2D([], [], color='black' ,markerfacecolor=Interchange_Station_Color, label="Inter station", linewidth=1, marker='o', markersize=15),
    ]

plt.legend(handles=Key, fontsize='15', loc='lower right')


plt.savefig('Images/TransportGraph_Task2_PhamQuocVi.png')

plt.show()







