
- the contribution mainly comes towarsd tackling the diagonal point, and this is important (seen in experiments with W2 on the graph page 8 that sucks)
- lemma 2 is strong
- a line of math research for them is to try to get same approx rate with more realistic assumption than lower bound of EPD  density
- the algorithm is online so new data coming through (like change of regime) is tackled well
- there is 2 theorem : the EPD converge and its quantized counterpart also !! in fact this is not a TDA paper but more a computationnal geometry paper in general
- a very good TDA contribution could be to link those theorems in practice with 1 tda workflow (with the code i got)


POC : vincent divol, theo lacombe, mathieu carriere

so there is 3 things to do :
- implement a TDA workflow that utilizes the algorithm to solve a particular problem, where a sequence of persistence diagram is observed online, especially case p = infty 'central in tda' : finance (stooq.com) & temporal graph or https://giotto-ai.github.io/gtda-docs/0.5.1/notebooks/gravitational_waves_detection.html
- trying to get better assumptions that can lead to convergence and see what are the practical ones, REMARK 1 in the paper
- this is a minimax theorem : find the worst case and see empirical minimax bounds for in practice problems (network 2d random graphs that expand, time series also lol)

"The problem of finding the graph genus is NP-hard'  wikipedia 'graph embedding"

this paper is realted in general : https://geometrica.saclay.inria.fr/team/Fred.Chazal/papers/cd-depd-18/p26-chazal.pdf