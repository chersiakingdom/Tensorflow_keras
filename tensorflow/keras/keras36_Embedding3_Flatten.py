from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np

docs = ['너무 재밌어요', '참 최고에요', '참 잘 만든 영화에요', '추천하고 싶은 영화입니다.', '한 번 더 보고 싶네요',
        '글쎄요', '별로에요', '생각보다 지루해요', '연기가 어색해요', '재미없어요', '너무 재미없다.', '참 재밌네요', 
        '배우가 잘 생기긴 했어요']

# 긍정 1, 부정 0
labels = np.array([1,1,1,1,1,0,0,0,0,0,0,1,1])

token = Tokenizer()
token.fit_on_texts(docs)
print(token.word_index)
x = token.texts_to_sequences(docs)
print(x)


from tensorflow.keras.preprocessing.sequence import pad_sequences
pad_x = pad_sequences(x, padding='pre', maxlen = 5)


print(pad_x)
print(pad_x.shape)  #13, 5

print(np.unique(pad_x)) 
print(len(np.unique(pad_x))) 

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Dense, LSTM, Flatten, Conv1D #학습하며 데이터 처리해줌.

model = Sequential()
model.add(Embedding(input_dim=280, output_dim=2, input_length=5)) 
# model.add(LSTM(32)) # 차원 1개 증가해서, 3차원으로 받음
# model.add(Conv1D(32, 3)) #filters, ?
# model.add(Embedding(28, 2))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))
model.summary()
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['acc'])

model.fit(pad_x, labels, epochs=100)

acc = model.evaluate(pad_x, labels)[1] #test 모델이 없어서 그냥 이렇게함.
print(acc)

y_pred = model.predict(["너무 재미없어요"])
print("y_pred :" , y_pred)

