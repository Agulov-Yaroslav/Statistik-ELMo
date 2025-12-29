import itertools
from collections import defaultdict
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import wordnet
from simple_elmo import ElmoModel
import os


f = open("match_sense_examples.txt")

examples = f.readlines() # List mit den Sätzen

f.close()

def get_vectors(examples, cache_file="vectors_cache.npy"):

    if os.path.exists(cache_file):
        print(f"Lade Vektoren aus dem Cache: {cache_file}...")
        return np.load(cache_file, allow_pickle=True)


    model = ElmoModel()
    # der Order elmo muss die options.json und die Gewichte
    # enthalten diese müsst ihr vor der Ausführung des MWE
    # herunterladen wie auf dem Blatt beschrieben
    model.load("./model")

    all_sentences = []
    metadata = []

    vectors = []
    for example in examples:
        id, pos, satz = example.split("    ") # Alle Elemente sind durch 4 Leerzeichen getrennt.
        words = satz.split(" ")
        all_sentences.append(words)
        metadata.append((id, int(pos)))

    all_elmo_out = model.get_elmo_vectors(all_sentences)

    final_results = []
    for i in range(len(metadata)):
        sense_id, pos_idx = metadata[i]
        # Extrahiere den Vektor aus dem großen Ergebnis-Block
        target_tensor = all_elmo_out[i, pos_idx, :]
        final_results.append({sense_id: target_tensor})

    np.save(cache_file, final_results)
    return final_results


def calculate_sense_centroids(vectors_list):
    sense_groups = defaultdict(list)

    for entry in vectors_list:
        for full_id, vector in entry.items():
            # Wir trennen am Unterstrich und nehmen den ersten Teil
            sense_key = full_id.split("_")[0]
            sense_groups[sense_key].append(vector)

    # 2. Zentroide berechnen
    centroids = {}
    for sense, v_list in sense_groups.items():
        centroids[sense] = np.mean(v_list, axis=0)

    return centroids


def compare_and_sort(centroids):
    results = []
    sense_names = list(centroids.keys())

    for s1, s2 in itertools.combinations(sense_names, 2):
        vec1 = centroids[s1].reshape(1, -1)
        vec2 = centroids[s2].reshape(1, -1)

        # Kosinusähnlichkeit
        sim = cosine_similarity(vec1, vec2)[0][0]
        results.append((s1, s2, sim))

    # Absteigend sortieren nach Ähnlichkeit (Index 2)
    results.sort(key=lambda x: x[2], reverse=True)
    return results

print(compare_and_sort(calculate_sense_centroids(get_vectors(examples))))
