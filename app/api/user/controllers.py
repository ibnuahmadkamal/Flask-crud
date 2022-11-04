import app.repository.postgres as repo_postgre

def create(payload):
    user_id = repo_postgre.create_user(payload)
    return user_id
    
def get_user_by_id(user_id):
    user = repo_postgre.get_user_by_id(user_id)

    return {
        "id" : user.id,
        "name": user.user_name,
        "score": user.score
    }

def update(payload,user_id):
    repo_postgre.update_user(payload,user_id)

def delete(user_id):
    repo_postgre.delete_user(user_id)