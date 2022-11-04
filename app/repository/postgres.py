from datetime import datetime
from app import app, db
from app.models.postgres import Users

def create_user(data):
    user = Users()
    user.user_name = data['name']
    user.score = data['score']

    try:
        db.session.add(user)
        db.session.flush()
        return user.id
    except Exception as e:
        app.logger.error(str(e))
        db.session.rollback()
        raise e
    finally:
        db.session.commit()
        db.session.close()

def delete_user(user_id):
    try:
        user = Users.query.filter_by(id=user_id).first_or_404(description='User {} not found'.format(user_id))
        
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        app.logger.error(str(e))
        db.session.rollback()
        raise e
    finally:
        db.session.close()

def get_user_by_id(user_id):
    try:
        user = Users.query.filter_by(
            id=user_id
        ).first_or_404(description='User {} not found'.format(user_id))
        return user
    except Exception as e:
        app.logger.error(str(e))
        db.session.rollback()
        raise e
    finally:
        db.session.close()

def update_user(data,user_id):
    try:
        user = Users.query.filter_by(
            id=user_id,
        ).first_or_404(description='User {} not found'.format(user_id))

        user.user_name = data['name']
        user.score = data['score']
        user.updated_at = datetime.now()
        db.session.commit()
    except Exception as e:
        app.logger.error(str(e))
        db.session.rollback()
        raise e
    finally:
        db.session.close()