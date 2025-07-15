from sqlalchemy.orm import declarative_base

Base = declarative_base()

def import_models():
    # Dynamically import models only when needed (avoids circular imports)
    from .models import user
    from .models import project
    from .models import task