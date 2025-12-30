import os
from typing import List
from dotenv import load_dotenv

load_dotenv()


class Config:
    PORT: int = int(os.getenv('PORT', '3001'))
    HOST: str = os.getenv('HOST', '0.0.0.0')
    FRONTEND_URL: str = os.getenv('FRONTEND_URL', 'http://localhost:3000')
    DEBUG: bool = os.getenv('DEBUG', 'False').lower() == 'true'
    FLASK_ENV: str = os.getenv('FLASK_ENV', 'production')
    
    @classmethod
    def get_cors_origins(cls) -> List[str]:
        origins = cls.FRONTEND_URL.split(',') if ',' in cls.FRONTEND_URL else [cls.FRONTEND_URL]
        return [origin.strip() for origin in origins]
