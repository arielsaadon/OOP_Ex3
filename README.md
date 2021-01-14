# Directed weighted graph
> - Authers [Yakov Elkobi](https://github.com/yakovElkobi) && [Ariel Saadon](https://github.com/arielsaadon)

![](https://hackernoon.com/hn-images/1*qq0sgd0Kny9QTaD-UT8LbQ.png)

The project is about Directed weighted graph.<br>
This project hes been done for assignment in course OOP in Ariel university.<br>
The assignment is translate from java to python.<br>
* [The assignment in java](https://github.com/yakovElkobi/OOP_ex2)<br>

## Simple example   
Find the shortest path between two nodes in an undirected graph:

```python
>>> from DiGraph import DiGraph
>>> from GraphAlgo import GraphAlgo
>>> g = DiGraph()
>>> g.add_node(0)
>>> g.add_node(1)
>>> g.add_node(2)
>>> g.add_node(3)
>>> g.add_edge(0,1,4)
>>> g.add_edge(1,2,2)
>>> g.add_edge(0,3,3)
>>> g.add_edge(3,2,4)
# now to make the algorithms:
>>> g_algo = GraphAlgo(g)
>>> print(g_algo.shortest_path(0,2))
(6, [0, 1, 2])
```

## Install:
```
$ git clone https://github.com/arielsaadon/OOP_Ex3     
```
Clone the repository to your project in Python.

See our [Wiki](https://github.com/arielsaadon/OOP_Ex3/wiki) for full documentation, examples, operational details and other information.
