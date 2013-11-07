from bson.objectid import ObjectId

class BoardData(object):
  def __init__(self,request):
    self.request = request
    self.db = request.db['board']

  def seed(self):
    message = "Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat. Ut wisi enim ad minim veniam, quis nostrud exerci tation ullamcorper suscipit lobortis nisl ut aliquip ex ea commodo consequat. Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. "
    for i in range(20):
      self.db.insert({'title':'my title', 'message': message, 'user_name': 'rafael', 'answers': [] })

  def find(self,id):
    return self.db.find_one({'_id': ObjectId(id)})
    

  def insert(self,post):
    pass
