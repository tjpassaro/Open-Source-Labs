import networkx as nx
from string import ascii_lowercase as lowercase

def edit_distance_one(word,words): 
        """
        for i in range(len(word)):
            left, c, right = word[0:i], word[i], word[i+1:]
            j = lookup[c] # lowercase.index(c)
            for cc in lowercase[j+1:]:
                yield left + cc + right"""
        adjs= set()
        for w in words:
            if dif_by_one(word,w):
                adjs.add(w)
        return adjs
def dif_by_one(word, word2): 
    for i in range(len(word)):
        if word[i] in word2:
            word2=word2.replace(word[i],"",1)
    return len(word2) is 1


def generate_graph(words): 
    G = nx.Graph(name="words")
    lookup = dict((c,lowercase.index(c)) for c in lowercase)
    candgen = ((word, cand) for word in sorted(words)
               for cand in edit_distance_one(word,words))
    G.add_nodes_from(words)
    for word, cand in candgen:
        G.add_edge(word, cand)
    return G

def words_graph(isFour):
    """Return the words example graph from the Stanford GraphBase"""
    words=set()
    filename = 'words.dat'
    if isFour:
        filename = 'words4.dat'
    for line in open(filename, 'r'):
        w=""
        for c in line:
            if c in lowercase:
                w = w + c
            else:
                break
        if len(w.strip()) is not 0:
            words.add(w)
    return generate_graph(words)

if __name__ == '__main__':
    from networkx import *
    length=input('4 or 5? ')
    isFour=False
    if length is 4:
        isFour=True
    G=words_graph(isFour)
    print("Loaded words_dat.txt containing 5757 five-letter English words.")
    print("Two words are connected if they differ in one letter.")
    print("Graph has %d nodes with %d edges"
          %(number_of_nodes(G),number_of_edges(G)))
    print("%d connected components" % number_connected_components(G))
    if isFour:
        for (start,end) in [('cold','warm'),
                                ('love','hate')]:
            print("Shortest path between %s and %s is"%(start,end))
            try:
                sp=shortest_path(G, start, end)
                for n in sp:
                    print(n)
            except nx.NetworkXNoPath:
                print("None")
    else:
        for (start,end) in [('chaos','order'),
                                ('nodes','graph'),
                                ('moron','start'),
                                ('pound','marks')]:
            print("Shortest path between %s and %s is"%(start,end))
            try:
                sp=shortest_path(G, start, end)
                for n in sp:
                    print(n)
            except nx.NetworkXNoPath:
                print("None")



