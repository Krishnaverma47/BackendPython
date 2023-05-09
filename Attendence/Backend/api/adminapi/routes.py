from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm


from .models import Admin, Student,Book
from database import db
from passwordHashing import get_password_hash
from .schemas import authenticate_admin
from .auth import create_access_token, get_current_admin


router = APIRouter()


@router.get('/',tags=["Root"])
def root():
    return {'hello': 'You are all welcome this fantasict app.'}


@router.post("/admin_register", tags=["Admin"])
async def create_admin(admin_data: Admin)->dict: 
    admin_data = jsonable_encoder(admin_data)

    admin_found = db['admin_collection'].find_one(
        {"email": admin_data['email']})
    if admin_found:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exist. ")
    else:
        db.admin_collection.insert_one({
            'name': admin_data['name'],
            'email': admin_data['email'],
            'dob': admin_data['dob'],
            'hashed_password': get_password_hash(admin_data['hashed_password']),
            'isActive': admin_data['isActive']
        })
        return ({
            'status_code': status.HTTP_200_OK,
            'detail': "Username created successfully."
        })
            
@router.post('/admin_login', tags=["Admin"])
def admin_login(form_data: OAuth2PasswordRequestForm = Depends())->dict:
    admin_found = authenticate_admin(
        db, form_data.username, form_data.password)
    if admin_found:
        access_token = create_access_token({'username': admin_found['email']})
        return {
            "status_code": status.HTTP_200_OK,
            "access_token": access_token,
            "token_type": "bearer"
        }
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect Username or Password",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
        
#Add Student
@router.post("/add_student", tags=["Student"])
async def add_student(student_data: Student,current_admin: Admin = Depends(get_current_admin))->dict: 
    student_data = jsonable_encoder(student_data)

    student_found = db['student_collection'].find_one(
        {"email": student_data['email']})
    if student_found:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Student already exist. ")
    else:
        if db['student_collection'].find_one({'roll_number':student_data['roll_number']}):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Rollnumber can not be same.")
        else:
            db.student_collection.insert_one({
                'name': student_data['name'],
                'email': student_data['email'],
                'roll_number': student_data['roll_number'],
                'dob': student_data['dob'],
                'isActive': student_data['isActive']
            })
            return ({
                'status_code': status.HTTP_200_OK,
                'detail': "Student added successfully."
            })
            
#add book list

@router.post("/add_book", tags=["Book"])
async def add_book(book_data: Book,current_admin: Admin = Depends(get_current_admin))->dict: 
    book_data = jsonable_encoder(book_data)

    book_found = db['book_collection'].find_one(
        {"author_name": book_data['author_name']})
    if book_found and db['book_collection'].find_one({"book_name": book_data['book_name']}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Same author name and same book name are not allowed.")
    else:
        db.book_collection.insert_one({
            "book_name": book_data['book_name'],
            "author_name": book_data['author_name'],
            "publication": book_data['publication']
        })
        return ({
            'status_code': status.HTTP_200_OK,
            'detail': "Book added successfully."
        })
        


                   
