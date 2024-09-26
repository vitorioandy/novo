from datetime import datetime
import pytz

print(datetime.today())

data = datetime.now(pytz.utc)
data2 = datetime.now(pytz.timezone('America/Sao_Paulo'))
print (data)
print (data2)