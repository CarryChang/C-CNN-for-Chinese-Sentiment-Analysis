import requests
import time
# 使用注意，在初始化的时候（第一次使用的时候速度较慢，在第二次使用则恢复正常，在400ms左右）
if __name__ == '__main__':
	api_url = 'http://127.0.0.1:5000/cnn_sa_api/{}'
	for content in ["这家酒店真差劲", '这家酒店真不错']:
		st = time.clock()
		api_ = api_url.format(content.strip())
		model_result = requests.get(api_).json()
		print(model_result)
		print('time used:{}'.format(time.clock() - st))