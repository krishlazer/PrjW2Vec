import gensim

model = gensim.models.KeyedVectors.load_word2vec_format('F:/Downloads/googlenewsex/GoogleNews-vectors-negative300.bin', encoding='latin', binary=True)
print(type(model))
sim1 = model.most_similar('Verkhny')