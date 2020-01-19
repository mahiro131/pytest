import subprocess
from subprocess import PIPE
import json


def get_sqs_url(SQS_QUEUE_NAME):
	'''
	Queueの名前を引数で受け取り,shellに渡し
	URLを返す.
	'''
	result = subprocess.run(["sh","get_sqs_url.sh",SQS_QUEUE_NAME],stdout=PIPE,text=True)
	return result.stdout


def get_msg_num(SQS_QUEUE_URL):
	'''
	QueueのURLを引数で受け取り,shellに渡し
	数字として返す
	'''
	# resultにはjson形式の文字列が入る
	result = subprocess.run("sh get_msg_num.sh",shell=True,input=SQS_QUEUE_URL,stdout=PIPE,text=True)
	
	# 辞書型に変換
	as_dict = json.lodas(result.stdout)

	return 


url = get_sqs_url("Orders")

print(url)
# msg_num = int(get_msg_num())
# print("msg_num:",msg_num)

# [print(number) for number in range(0,msg_num)] 