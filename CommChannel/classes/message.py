class Message:
  def __init__(self, sender, timestamp,text):
    self.sender = sender
    self.timestamp = timestamp
    self.text = text

  def show(self):
    return "sender: " + self.sender + ". At:" +  self.timestamp.strftime("%d-%b-%Y (%H:%M:%S.%f)") + ". Text: " + self.text
