Wir wollen die Ähnlichkeit von Senses des Wortes match auf verschiedene Arten untersuchen.

#### 1. Anhand der Ähnlichkeit von Zentroiden 
(die wir auf Basis aller uns zur Verfügung stehenden Sätze für einen Sense berechnen)
#### 2. Anhand von WordNet Pfaden

### Auflistung aller WordNet-Senses des Wortes match:

- match.n.01 lighter consisting of a thin piece of wood or cardboard tipped with combustible chemical; ignites with friction
- match.n.02 a formal contest in which two or more persons or teams compete
- match.n.03 a burning piece of wood or cardboard
- match.n.04 an exact duplicate
- match.n.05 the score needed to win a match
- match.v.01 be compatible, similar or consistent; coincide in their characteristics
- match.v.02 provide funds complementary to
- match.v.03 bring two objects, ideas, or people together
- match.v.05 make correspond or harmonize
- match.v.07 give or join in marriage

# TODO
### 1. Für jeden Satz ein kontextualisiertes ELMo-basiertes Word Embedding für match


Dafür betten wir jeden Satz in ELMo ein und erhalten den Wortvektor für match im jeweiligen Satz mit Hilfe der ebenfalls angegebenen Position.

#### Ergebnis:
Kontextualisierter ELMo Vektor für match aus jedem Satz

### 2. auf Basis aller zu einem Sense gehörigen Vektoren einen Zentroiden für diesen Sense berechnen


### 3. die Kosinusähnlichkeit zwischen den Zentroiden berechnen und die Paare absteigend von höchster zu niedrigster Kosinusähnlichkeit ordnen. 

## Teil 2:

### 1. jedes Paar von Synsets die Ähnlichkeit mit Hilfe der WordNet path_similarity Ermitteln

Kosinusähnlichkeit und WordNet path similarity können beide Werte zwischen 0 und 1
annehmen. Die Ähnlichkeit von Senses/Synsets ist hoch, wenn die Kosinusähnlichkeit
(der Zentroiden) hoch ist und/oder wenn die WordNet path similarity hoch ist.

### 2. die Information der path similarity jedem Paar von Synsets in dem Ranking beifügen.
Die Paare bleiben dabei weiterhin nach Kosinusähnlichkeit der Zentroiden geordnet.


