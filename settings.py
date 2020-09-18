# MySQL config
MYSQL_SERVER_IP = '10.8.28.128'
MYSQL_SERVER_PORT = 3306
MYSQL_DB_NAME = "stock"
MYSQL_USER_NAME = "stock"
MYSQL_USER_PWD = "mx6mCbZAwt5rB4L6"

MYSQL_SUMMARY_TABLE_NAME = "stock_news_summary"
MYSQL_EMOTION_TABLE_NAME = "stock_news_emotion"

# Kafka config
BOOTSTRAP_SERVERS = ["10.8.28.130:9091","10.8.28.130:9092","10.8.28.130:9093"]
KAFKA_MAX_WORKERS = 1

STOCK_NEWS_GROUP_ID = "summary_online"
STOCK_EMOTION_GROUP_ID = "emotion_online"
STOCK_NEWS_TOPICS = ["stockNews"]

# FIC Algorithm API
SUMMARY_SERVICE_API = "http://10.8.23.226:8000/api/summary/predict"
KEYWORDS_SERVICE_API = "http://10.8.23.226:8000/api/keywords/predict"
KNEE_LOCATOR_SERVICE_API = "http://10.8.23.226:8000/api/kneeLocator"
EMOTION_ANALYSIS_API = "http://10.8.23.226:8000/api/emotion/predict"