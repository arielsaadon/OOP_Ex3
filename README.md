# Directed weighted graph
The project is about Directed weighted graph.<br>




It has the following class.<br>
# Class NodeData:
This class repesnt Node in graph.<br>
In each Node has the following:<br>



   <table>
     <thead>
       <tr>
       <th>Fields</th>
              <th>Type</th>
     </tr>
    <thead>
      <tr>
       <tbody>
          <tr>
             <td rowspan=4><picture>
               <td>key</td>
      </tr> 
      <tr>
            <td>weight</td>
      </tr> 
      <tr>
            <td>tag</td>
            <td>pos</td>
      </picture></td>
             <td>int</td>
      </tr> 
      <tr>
            <td>floot</td>
      </tr> 
      <tr>
            <td>boolean</td>
      </tr> 
      <tr>
        <td>tuple</td>
      </tr> 
      <tr>
       </tr>
       </tbody> 
       </table>
            



|Fields |  Type |
|---------------|               
|  key  |  int  |<raw=true">
|               |
|weight | floot |<raw=true">
|               |
|  tag  |boolean|<raw=true">
|               |
|  pos  | tuple |<raw=true">
|-------|--------

# Class DiGraph:
This class repesnt graph.<br>
In this class you can do the following:
add/remove Node in the graph.<br>
add/remove edge in the graph.<br>
Also you can get the following:
All Nodes, edges out/in, node size, edge size, mc.<br>
The Node are stored in a Dict.<br>
The edgs and weight are stored in a double Dict.<br>
one for out edge and one for in edge.<br>
edge_size counts edges in the graph.<br>
mc counts actions in the graph.<br>


|-----------|------------|
|  Fields   |    Type    |
|-----------|------------|
|  nodes    |    Dict    |
|-----------|------------|
| out_edges | double Dict|
|-----------|------------|
| in_edges  | double Dict|
|-----------|------------|
| edge_size |     int    |
|---------- |------------|
|     mc    |     int    |
|-----------|------------|

# Class GraphAlgo:
In this class you can get graph and do some algorithms.<br>
The following methods:
*connected_component:
Finds the Strongly Connected Component(SCC) that node id1 is a part of.<br>
In this method we use BFS algorithm.<br>
Return The list of nodes in the SCC.<br>
https://en.wikipedia.org/wiki/Breadth-first_search#/media/File:Animated_BFS.gif.<br>
#BFS algorithm:
https://en.wikipedia.org/wiki/Breadth-first_search
connected_component:
Finds all the Strongly Connected Component(SCC) in the graph.<br>
In this method we use method connected_component.<br>
The list all SCC.<br>
*shortest_path:
Returns the shortest path from node id1 to node id2 and a list of the nodes ids that the path goes through using Dijkstra's Algorithm.<br>
https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif.<br>
#Dijkstra's Algorithm
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
*save_to_json and load_from_json:
Saves the graph in JSON format to a file.<br>
Loads a graph from a json file.<br>
True if the seve/loading was successful, False o.w.?<br>
*plot_graph:
A show graph for example.<br>


