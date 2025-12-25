from simple_elmo import ElmoModel

model = ElmoModel()
# der Order elmo muss die options.json und die Gewichte 
# enthalten diese müsst ihr vor der Ausführung des MWE 
# herunterladen wie auf dem Blatt beschrieben 
model.load("./model")
s = ["I", "ate", "an", "apple"]
target_word = "apple"
target_word_position = 3

vectors = model.get_elmo_vectors([s])
print(vectors) # 3d tensor shape [1, 4. 1024], batch size 1, sequence length = 4
print("=="*42)
target_tensor = vectors[0, target_word_position, :]
print(target_tensor)
