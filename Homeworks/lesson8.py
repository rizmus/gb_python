from datetime import datetime

import less

a = datetime.now()
print(a.strftime('%d.%m.%Y'))

b = datetime.strptime('22.02.1998', '%d.%m.%Y')
print(b)