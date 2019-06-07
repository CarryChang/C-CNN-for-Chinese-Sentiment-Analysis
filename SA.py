# coding: utf-8
# from __future__ import print_function
import os
import tensorflow as tf
import numpy as np
import tensorflow.contrib.keras as kr
from cnn_model import TCNNConfig, TextCNN
from data.cnews_loader import read_category, read_vocab
try:
    bool(type(unicode))
except NameError:
    unicode = str
base_dir = 'data/data'
vocab_dir = os.path.join(base_dir, 'vocab.txt')
save_dir = 'checkpoints/textcnn'
save_path = os.path.join(save_dir, 'best_validation')  # 最佳验证结果保存路径
class CnnModel:
    def __init__(self):
        self.config = TCNNConfig()
        self.categories, self.cat_to_id = read_category()
        self.words, self.word_to_id = read_vocab(vocab_dir)
        self.config.vocab_size = len(self.words)
        self.model = TextCNN(self.config)
        self.session = tf.Session()
        self.session.run(tf.global_variables_initializer())
        saver = tf.train.Saver()
        # 读取保存的模型
        saver.restore(sess=self.session, save_path=save_path)
    def emotion_score(self, message):
        # 支持不论在python2还是python3下训练的模型都可以在2或者3的环境下运行
        content = unicode(message)
        data = [self.word_to_id[x] for x in content if x in self.word_to_id]
        feed_dict = {
            self.model.input_x: kr.preprocessing.sequence.pad_sequences([data], self.config.seq_length),
            self.model.keep_prob: 1.0
        }
        # 类别概率的输出
        predictions = self.session.run(self.model.softmax_tensor1, feed_dict=feed_dict)
        # 只输出积极的情绪就行
        return np.squeeze(predictions)[1]
if __name__ == '__main__':
    #  解决办法：https://www.jianshu.com/p/fc11f32800f9
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