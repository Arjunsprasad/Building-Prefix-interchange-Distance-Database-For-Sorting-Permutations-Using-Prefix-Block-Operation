# Building Prefix interchange Distance Database For Sorting Permutations Using Prefix Block Interchange Operation
## ABSTRACT
Sorting by prefix block interchange is a combinatorial optimization problem in which a given permutation is to be sorted with minimum number of prefix block interchanges. The minimum number of prefix block interchanges required to sort a permutation is called the prefix block interchange distance of the permutation . The complexity class of this problem is unknown. As part of this project we build a database of prefix block interchange distances for permutations with length at most 7.

Building such a database is useful in multiple ways. This could help understand the distribution of prefix block interchange distances, or it could help partition the symmetric group into various classes with same distance, or it could be used as a benchmark data for studying the optimality of various algorithms.

## BACKGROUND
The problem of transforming a given sequence into another using a specified set of operations is a fundamental algorithmic problem that has received a lot of attention in the last decades dues to its multiple applications various fields such ascomputational biology interconnection network design, and quantum computing. 

The problem is formulated as follows. A permutation of n objects is a bijection form the set to itself. The objects we consider are {1, 2, . . . , n}. The set of all permutations of these objects, along with function composition operation defines the symmetric group Sn. A generating set of Sn, denoted by G is a subset of Sn such that any permutation can be expressed as a finite composition of permutations in G. A generating set is also called an operation. 

Given two permutation, say α, β ∈ Sn and an operation G, the problem of transforming α to β using the generators in G is a combinatorial optimization problem that reduces to a sorting problem. A sequence of generators g1, g2. . . . gt that transforms a given permutation to I is called a sorting sequence, where It is the identity permutation in Sn. The problem that we study in this work is to compute a shortest sequence of generators in G that sorts a given permutation π. The length of shortest sequence is called the distance. 

The problem is known to be NP-hard in general , but for some of operations, it can be solved in polynomial time (e.g. block-interchanges and signed reversals ), while other families yield hard problems that admit good approximations (e.g. 11/8 for reversals and for block-transpositions ).Several restrictions of these families have also been studied, one of which stands out in the field of interconnection network design: the so-called prefix constraint, which forces operations to act on a prefix of the permutation rather than on an arbitrary interval. Those restrictions were introduced as a way of reducing the size of the generated network while maintaining a low value for its diameter, thereby guaranteeing a low maximum communication delay . The most famous example is perhaps the restriction of reversals (which reverse the order of elements along an interval) to prefix reversals, and the corresponding problem known as pancake flipping, introduced in and whose complexity was only settled thirty years later.

A permutation is an ordering/arrangement of elements in a set. For example, consider a set S = {1,2,3}. The permutations are 123,132,213,231,312,321. For a set containing n elements there are n! permutations. For example, the set S contains 3 elements and 3! = 6 permutations are there. We denote a permutation by the symbol π. And a permutation along with the elements are generally represented as π = π1 π2 π3 π4.... πi... πin where i is the index/position in the permutation.

#### Prefix block Interchange operation
Consider a permutation π = 43251, a prefix block is a sub-permutation containing the first element of the permutation. The following examples shows the prefixes of the permutation π.

a. **4**3251

b. **43**251

c. **432**51

d. **4325**1

e. **43251**

The following examples show some blocks that are not prefixes.

a. 4**3**251

b. 4**325**1

c. 43**25**1

d. 43**251**

A prefix block interchange operation interchanges two blocks in a permutation in which one block is a prefix block. The following examples show someprefix block interchange operation.

![image](https://user-images.githubusercontent.com/72243394/200158015-f95a8411-6674-4383-a77b-5dd0378cb7fd.png)

#### How to specify a prefix block interchange operation?
We will place first number the gaps between the elements in the permutation. See the example.

![image](https://user-images.githubusercontent.com/72243394/200158085-9cf62ca5-61aa-4ccb-9818-452efeb57fdd.png)

A prefix block interchange operation is specified by 4 indices (or gaps). For example, β(1,3,5,6) is the prefix block interchange that interchanges the blocks [43]with [1]. Then the resultant permutation is 12543.

#### The sorting problem
Sort the given permutation with minimum number of moves. For example,the permutation 43251 can be sorted with 2 moves. The sequence of moves isshown below. 43251 β(1,2,3,4) → 23451 β(1,5,5,6) → 12345

#### Cayley Graph
Cayley graphs were originally proposed as a generic theoretical model for analyzing symmetric interconnection networks. The most notable feature of theCayley graph is its universality. The Cayley graph represents a class of high performance interconnection network with a small degree and diameter, goodconnectivity and simple routing algorithms.

Some attractive properties of this Cayley graph interconnection network include:vertex symmetry, small degree, a sub-logarithmic diameter, extendibility, high connectivity (robustness), easy routing, regularity of topology, fault tolerance, extensibility and embeddability of other topologies.

## Motivation
Sorting permutations with various operations has applications in macro rearrangement of genes in a genome and the design of computer interconnection networks.
### 1. Application in computational biology - GENOME REARRANGEMENT
Various global rearrangements of permutations, such as reversals and transpositions have recently become of interest because of their applications in computational molecular biology.These various problems are of interest because the permutations can be used to represent sequences of genes in chromosomes, andthe global rearrangements then represent evolutionary events. As a result, we call these problems genome rearrangement problems.Genome rearrangement problems seem to be unlike previously studied algorithmic problems on sequences, so new methods have had to be developed to deal with them.we study several genome rearrangement problems as interesting and challenging algorithmicproblems in their own right, including some problems for which the global rearrangement has no immediate biological equivalent. For example, we define a block-interchange to be a rearrangement that swaps any two substrings of the permutation Understanding how different two organisms are is one question addressed by the comparative genomics field. A well-accepted way to estimate the evolutionary distance between genomes of two organisms is finding the rearrangement distance, which is the smallest number of rearrangements needed to transform one genome into another. By representing genomes as permutations,one of them can be represented as the identity permutation, and, so, we reducethe problem of transforming one permutation into another to the problem of sorting a permutation using the minimum number of rearrangements.

### APPLICATION IN INTERCONNECTION OF NETWORK DESIGN
In the field of interconnection network design: the so-called prefix block interchange operation, which forces operations to act on a prefix of the permutation rather than on an arbitrary interval. This is introduced as a way of reducing the size of the generated network while maintaining a low value for its diameter, thereby guaranteeing a low maximum communication delay . The diameter of a network represents the maximum communication delay between two nodes inthe network.

## LITERATURE SURVEY
The first approximation algorithm to solve SBT (SORTING BY TRANSPOSITIONS)was devised in 1998 by Bafna and Pevzer , with a 1.5 ratio, based on the properties of a structure called the cycle graph. In 2006, Elias and Hartman presented a 1.375-approximation algorithm (EH algorithm) with time complexity O(n2)O(n2), the best known approximation solution so far for SBT. In 2012, Bulteau, Fertin and Rusu demonstrated that SBT is NPNP- hard.In a later study, the time complexity of the EH algorithm was improved to O(nlogn)O(nlogn) byCunha et al. Improvements to the EH algorithm, including heuristics, were proposed by Dias and Dias.

### Known Algorithm

![image](https://user-images.githubusercontent.com/72243394/200158386-df8b50fa-a3c6-4210-9fb1-807a3a2d32ee.png)

### Various Approaches

![image](https://user-images.githubusercontent.com/72243394/200158428-ed9c0de2-332f-420b-b6c1-d94b861bd50c.png)

The problem is known to be NP-hard in general and W-hard when parameterised by the length of a solution , but some families of operations that are important in applications lead to problems that can be solved in polynomial time (e.g. exchanges , block-interchanges and signed reversals ), while other families yield hard problems that admit good approximations (e.g. 11/8 for reversals and for block-transpositions ). Write known results. Who proposed these problems. Which are the known algorithms,various approaches etc.

## Our Approach
In our approach, we have done three algorithms to build Prefix interchange distance database for sorting permutation using Prefix block interchange operation.

In First approach, Manually each moves for permutations having length 2,3,4 and5 were written using separate functions. And then these functions were invoked recursively.

In Second approach, there is a function which will automatically creates moves for particular permutation of length. Then using tree data structure, moves were implemented recursively.

In Third approach, there is a function which will automatically creates moves for particular permutation of length. Then using graph data structure and with the help of the in-built functions in package NetworkX, moves were implemented.

## Implementation and Analysis
First Approach was using Recursive function, manually typed moves were applied. Recursion is the method of solving a computational problem where the solution depends on solutions to smaller instances of the same problem. Recursion solves such recursive problems by using functions that call themselves from within their own code. Here, In our approach we have written different functions which are manually written moves for each permutation of lengths 2,3,4 and 5. Then, these moves were applied recursively. A part of algorithm is given below:

![image](https://user-images.githubusercontent.com/72243394/200158585-de6b5360-2df0-4049-b0e7-554d45e9c8be.png)

The result for this type of implementation was limited,because we have written moves as functions manually. So, we have got the sorting sequences from length 2 to 5. The table which shows the data after implementation is shown below:

![image](https://user-images.githubusercontent.com/72243394/200158614-e4d93bb4-2604-4206-87d5-84c9cd59b84f.png)

Second approach was using tree data structure. Tree is a non-linear data structure because it does notstore in a sequential manner. It is a hierarchical structure as elements in a Tree are arranged in multiple levels. In tree data structure, the topmost node is called a root node. Each node contains some data, and data can be of any type. Here moves were generated using a special function and implemented using a nested for loop. The Algorithm is given below:

![image](https://user-images.githubusercontent.com/72243394/200158660-b88e021d-1083-401d-bae8-69f0f8d54887.png)

For applying the generated moves, a separate function is designed. This function slices the string i.e., permutation using the moves and replaces the block and finally the resultant permutation will be returned. The algorithm for this function is mentioned below:

![image](https://user-images.githubusercontent.com/72243394/200158673-73d658e4-b5fb-4563-8bc6-d43324ef13ea.png)

The main part of the implementation comes under the function named tree. Through the theory and application, we know that the maximum depth will be half the length of permutation. So, maximum depth will be assigned as n/2. And for each moves, it will apply moves using the function applymoves. Then in each depths,sorting will be checked and suppose sorting happens then it will be appended to the respective list. Here also this function is a recursive function. After 6 steps of checking Depth will be incremented and checks it is less than or equal to the condition where maximum depth is n/2. Then again it invokes its own function. The algorithm for the tree function is mentioned below:

![image](https://user-images.githubusercontent.com/72243394/200158708-5c4033aa-8c79-44c6-81ae-a5eaa6f5ac7f.png)

The result of this approach comes to an end with the shortest distance to sort permutation of length up to 6. The result is shown below:

![image](https://user-images.githubusercontent.com/72243394/200158723-e977b9e7-aa50-4c78-88e5-7b18ac8ccea5.png)

Third approach was using graph data structure. Graph is a non-linear data structure consisting of nodes and edges. The nodes are some times also reffered to as vertices and the edges are lines or arcs that connect any two nodes in the graph. Here, In this implementation, we had implemented using NetworkX package of Python. It has so many built-in functions to solve the various problems related to graph. Here, nodes are permutation and edges or vertices are the moves. Here moves were generated using a special function and implemented using a nested for loop. The Algorithm is given below:

![image](https://user-images.githubusercontent.com/72243394/200158747-6b96339a-c83a-4bf9-99f5-132b28f49620.png)

For applying the generated moves, a separate function is designed. This function slices the string i.e., permutation using the moves and replaces the block andfinally the resultant permutation will be added as an ege in the graph. The algorithm for this function is mentioned below:

![image](https://user-images.githubusercontent.com/72243394/200158765-2ac86c99-6b09-4bdc-b69e-3389e87f9236.png)

The main part of the implementation comes under the function named graphfunction. Through the theory and application, we know that the maximum depth will be half the length of permutation. So, maximum depth will be assigned as n/2. And for each moves, it will apply moves using the function applymoves. Then checks depth with maximum depth and if it is true recursively the function calls itself. The algorithm for the tree function is mentioned below:

![image](https://user-images.githubusercontent.com/72243394/200158801-5cbf082d-d478-40ce-a13b-409a7c5c524f.png)

The result of this approach comes to an end with the shortest distance to sort permutation of length up to 7. After 7 it takes more than 10 hours time to get the result. The result is shown below:

![image](https://user-images.githubusercontent.com/72243394/200158834-9f3b5188-e46c-47aa-b767-4f3b0b61e679.png)

## Conclusion
We initiated in this work the study of sorting permutations by prefix block-interchanges, an operation that generalises several well-studied operations in genome rearrangements and interconnection network design. through the three implementations we got same results.

