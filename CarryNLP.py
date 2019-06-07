from SA import CnnModel
import tensorflow as tf
import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
for i in open('data/data/1.txt', 'r', encoding='utf-8'):
    tf.reset_default_graph()
    test_text = i.strip().split('\t')[1]
    print(test_text)
    # # test_text = '这家的体验非常好'
    # test_text = i
    # # test_text = '这家的体验非常垃圾'
    predict_score = CnnModel().emotion_score(test_text)
    print(predict_score)