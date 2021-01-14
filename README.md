# Directed weighted graph
> - Authers [Yakov Elkobi](https://github.com/yakovElkobi) && [Ariel Saadon](https://github.com/arielsaadon)

The project is about Directed weighted graph.<br>
This project hes been done for assignment in course OOP in Ariel university.<br>
The assignment is translate from java to python.<br>
* The assignment in java.<br>
https://github.com/yakovElkobi/OOP_ex2<br>
It has the following class.<br>

# Class NodeData:<br>
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
               <td>key</td>
               <td>int</td>
      </tr> 
      <tr>
            <td>weight</td>
            <td>floot</td>
      </tr> 
      <tr>
            <td>tag</td>
            <td>boolean</td>
      </tr> 
      <tr>  
            <td>pos</td>
            <td>tuple</td>
       </tbody> 
       </table>
         
# Class DiGraph:
This class repesnt graph.<br>
In this class you can do the following:<br>
add/remove Node in the graph, add/remove edge in the graph.<br>
Also you can get the following:<br>
All Nodes, edges out/in, node size, edge size, mc.<br>
The Node are stored in a Dict, The edgs and weight are stored in a double Dict one for out edge and one for in edge.<br>
edge_size counts edges in the graph, mc counts actions in the graph.<br>

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
               <td>nodes</td>
               <td>Dict</td>
      </tr> 
      <tr>
            <td>out_edge</td>
            <td>double Dict</td>
      </tr> 
      <tr>
            <td>in_edges</td>
            <td>double Dict</td>
      </tr> 
      <tr>  
            <td>edge_size</td>
            <td>int</td>
      </tr> 
      <tr> 
            <td>mc</td>
            <td>int</td>
       </tbody> 
       </table>

# Class GraphAlgo:
In this class you can get graph and do some algorithms.<br>
The following methods:<br>
* connected_component:<br>
Finds the Strongly Connected Component(SCC) that node id1 is a part of.<br>
In this method we use BFS algorithm.<br>
Return The list of nodes in the SCC.<br>

![](https://en.wikipedia.org/wiki/Breadth-first_search#/media/File:Animated_BFS.gif)

* BFS algorithm:<br>
https://en.wikipedia.org/wiki/Breadth-first_search
* connected_components:<br>
Finds all the Strongly Connected Component(SCC) in the graph.<br>
In this method we use method connected_component.<br>
The list all SCC.<br>
* shortest_path:<br>
Returns the shortest path from node id1 to node id2 and a list of the nodes ids that the path goes through using Dijkstra's Algorithm.<br>
https://upload.wikimedia.org/wikipedia/commons/5/57/Dijkstra_Animation.gif.<br>
* Dijkstra's Algorithm:<br>
https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
* save_to_json and load_from_json:<br>
Saves the graph in JSON format to a file.<br>
Loads a graph from a json file.<br>
True if the seve/loading was successful, False o.w.<br>
* plot_graph:<br>
A show graph for example.<br>


