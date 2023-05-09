
def create_todo(db: Session, current_user: models.User, todo_data: schemas.TODOCreate):
   todo = models.TODO(text=todo_data.text,
                   	completed=todo_data.completed)
   todo.owner = current_user
   db.add(todo)
   db.commit()
   db.refresh(todo)
   return todo
def update_todo(db: Session, todo_data: schemas.TODOUpdate):
   todo = db.query(models.TODO).filter(models.TODO.id == id).first()
   todo.text = todo_data.text
   todo.completed = todo.completed
   db.commit()
   db.refresh(todo)
   return todo
def delete_todo(db: Session, id: int):
   todo = db.query(models.TODO).filter(models.TODO.id == id).first()
   db.delete(todo)
   db.commit()
 
def get_user_todos(db: Session, userid: int):
   return db.query(models.TODO).filter(models.TODO.owner_id == userid).all()