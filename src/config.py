import os

class Config:
    """Central configuration class for Scout with image support"""
    
    # Cache setup
    CACHE_DIR = os.getcwd() + '\\caches'
    LOG_DIR = os.getcwd() + '\\logs'
    # Cache file names
    CACHE_FILES = {
        'text': 'text_features_cache.pkl',
        'content': 'content_cache.pkl',
        'object': 'object_features_cache.pkl',
        'face': 'face_features_cache.pkl',
    }
    
    # Exclusion lists
    DEFAULT_EXCLUDE_KEYWORDS = [
        "venv", "env", "node_modules", "__pycache__",
        "dist-info", "macosx", "_vendor", "thirdpartynotices"
    ]
    
    DEFAULT_EXCLUDE_FILENAMES = [
        "lgpl.txt", "vendor.txt", "thirdpartysoftwarenotice.txt", "entry_points.txt"
    ]
    
    # Extensions
    IMAGE_EXTENSIONS = [".png", ".jpg", ".jpeg"]
    FILE_EXTENSIONS = [".pdf", ".txt", ".docx"] + IMAGE_EXTENSIONS
    
    # OCR Configuration
    TESSERACT_CONFIG = os.environ.get('TESSERACT_CONFIG', '')
    OCR_DPI = int(os.environ.get('OCR_DPI', '300'))
    
    # Processing limits
    MAX_CHARS = 15000
    DEFAULT_TIMEOUT = 600  # seconds
    DEFAULT_BATCH_SIZE = 100
    SAVE_INTERVAL = 50  # Save cache every N items
    
    # Preview settings
    PREVIEW_LENGTH = 200  # Maximum length of preview snippet in characters
    
    # Models configuration
    DEFAULT_MODEL = "BAAI/bge-m3"
    MODEL_ALIASES = {
        "bgem3": "BAAI/bge-m3",
    }
    
    # YOLO model settings
    YOLO_WEIGHTS = os.environ.get('YOLO_WEIGHTS', 'models/yolov4.weights')
    YOLO_CONFIG = os.environ.get('YOLO_CONFIG', 'models/yolov4.cfg')
    YOLO_CLASSES = os.environ.get('YOLO_CLASSES', 'models/coco.names')
    YOLO_CONFIDENCE = float(os.environ.get('YOLO_CONFIDENCE', '0.8'))
    
    # Face recognition settings
    FACE_SIMILARITY_THRESHOLD = float(os.environ.get('FACE_SIMILARITY', '0.4'))
    
    @classmethod
    def initialize(cls):
        """Initialize configuration and create necessary directories"""
        os.makedirs(cls.CACHE_DIR, exist_ok=True)
        os.makedirs(cls.LOG_DIR, exist_ok=True) 

        for cache_file in cls.CACHE_FILES.values():
            cache_path = os.path.join(cls.CACHE_DIR, cache_file)
            cache_dir = os.path.dirname(cache_path)
            os.makedirs(cache_dir, exist_ok=True)

    
    @classmethod
    def get_cache_path(cls, cache_type):
        """Get the full path for a cache file"""
        if cache_type in cls.CACHE_FILES:
            return os.path.join(cls.CACHE_DIR, cls.CACHE_FILES[cache_type])
        # Default fallback
        return os.path.join(cls.CACHE_DIR, f"{cache_type}_cache.pkl")