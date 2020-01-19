
import subprocess
from subprocess import PIPE
import json

url = "https://ap-northeast-1.queue.amazonaws.com/975328831561/Orders"

result = subprocess.run(["sh","get_msg_num.sh",url],stdout=PIPE,text=True)

tmp_json = result.stdout

a = json.loads(tmp_json)

print(type(a))
print(a['Attributes']['ApproximateNumberOfMessages'])
