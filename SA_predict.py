# coding: utf-8
import os
import tensorflow as tf
import numpy as np
import tensorflow.contrib.keras as kr
from model.cnn_model import TCNNConfig, TextCNN
from model.data_processing import read_category, read_vocab
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
base_dir = 'data'
vocab_dir = os.path.join(base_dir, 'vocab.txt')
save_dir = 'checkpoints/textcnn'
save_path = os.path.join(save_dir, 'best_validation')
class CnnModel:
    def __init__(self):
        self.config = TCNNConfig()
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_dir)
        self.config.vocab_size = len(self.words)
        self.model = TextCNN(self.config)
        self.session = tf.Session()
        self.session.run(tf.global_variables_initializer())
        # 加载模型
        saver = tf.train.Saver()
        saver.restore(sess=self.session, save_path=save_path)
    def emotion_score(self, message):
        data = [self.word_to_id[x] for x in message if x in self.word_to_id]
        feed_dict = {
            self.model.input_x: kr.preprocessing.sequence.pad_sequences([data], self.config.seq_length),
            self.model.keep_prob: 1.0
        }
        # 类别概率的输出
        predictions = self.session.run(self.model.softmax_tensor1, feed_dict=feed_dict)
        return np.squeeze(predictions)[1]
# if __name__ == '__main__':
#     import time
#     for i in open('data/demo_predict.txt', 'r', encoding='utf-8'):
#         st = time.clock()
#         tf.reset_default_graph()
#         test_text = i.strip()
#         predict_score = CnnModel().emotion_score(test_text)
#         print('{}，情感分析结果：{}'.format(test_text, predict_score))
#         print('time used:{}'.format(time.clock()-st))