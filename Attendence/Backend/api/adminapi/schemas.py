from passwordHashing import verify_password 


def authenticate_admin(adminDatabase, username: str, password: str):
    admin_found = adminDatabase.admin_collection.find_one({'email':username})
    if not admin_found:
        return False
    if not verify_password(password, admin_found['hashed_password']):
        return False
    return admin_found