class Category:

  def __init__(self, category):
        self.ledger = []
        self.category = category
        self.total = 0.0

  def deposit(self, amount, description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.total += float(amount)

  def withdraw(self, amount, description=""):
    if self.total >= amount:    
      self.ledger.append({"amount": -1 * amount, "description": description})
      self.total -= float(amount)
      return True

    return False

  def get_balance(self):
    return self.total

  def check_funds(self, amount):
    if (self.total >= amount):
      return True
  
    return False

  def transfer(self, amount, obj):
    string = "Transfer to " + obj.category
    if self.withdraw(amount, string) == False:
      return False
    else:
      string = "Transfer from " + self.category
      obj.deposit(amount, string)
      return True

  def __repr__(self):
    title = self.category.center(30, '*')
    line = ""
    for i in self.ledger:
      description = "{:<23}".format(i["description"]) 
      amount = '{:7.2f}'.format(i["amount"])
      right_aligned = f"{amount:<7}"
      line += '\n' + description[:23] + right_aligned
    total = '\n' + "Total: {:.2f}".format(self.total)

    return title + line + total

def create_spend_chart(categories):
  string = ""
  tmp = ""
  scale = ""
  withdrawl = dict()
  percent = dict()
  line = ""
  cat_list = ""

  heading = 'Percentage spent by category'
  if len(categories) == 0:
    return "empty category"
  
  cat_total = 0.0
  for category in categories:
    spent = 0.0
 
    for withdraw in category.ledger:
      if withdraw['amount'] < 0:
        spent += withdraw['amount']
    withdrawl[category.category] = abs(spent)
    cat_total += withdrawl[category.category]
  
    #print("spent", withdrawl[category.category])
    #print("category total =", cat_total)
    #total_data += abs(category.total)
  #print("total", cat_total)
  #print("total_data", total_data)
  #print("Final total =", cat_total)

  for item, value in withdrawl.items():
    percent[item] = (value/cat_total)*100
    #print("percent", percent[item])     

  length = max(withdrawl.keys(), key=len)

  for i in reversed(range(11)):
    tmp = str(i * 10)
    scale += (tmp.rjust(3) + '|')

    for j in percent.values():
      if j > (i * 10):
        scale += ' o '
      else:
        scale += '   '
    scale += ' \n'

  line = '    -'
  for i in range(len(categories)):
    line+= '---'
  
  for i in range(len(length)):
    cat_list += '\n    '
    for key in withdrawl.keys():
      if i < len(key):
        cat_list += ' ' + key[i] + ' '
      else:
        cat_list += '   '
    cat_list += ' '

  string = heading + '\n'
  string += scale
  string += line
  string += cat_list + '\n'

  string = string.rstrip() + '  '

  return string