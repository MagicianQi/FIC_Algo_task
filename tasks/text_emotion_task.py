# -*- coding: utf-8 -*-

import time
import json

from utils.KafkaUtils import KafkaConsumerRunner
from utils.Apiutils import request_emotion_api
from utils.MySqlUtils import MysqlClass
from settings import *

class TextEmotionTask(KafkaConsumerRunner):

    def __init__(self, bootstrap_servers, group_id, topics, max_workers):
        super().__init__(bootstrap_servers, group_id, topics, max_workers)
        self.mysql = MysqlClass(server=MYSQL_SERVER_IP,
                                port=MYSQL_SERVER_PORT,
                                user=MYSQL_USER_NAME,
                                password=MYSQL_USER_PWD,
                                db_name=MYSQL_DB_NAME)

    def process_records(self, topic, partition, offset, key, value):
        try:
            data = json.loads(value.decode())
            code = data["code"]
            time_str = data["time"]
            the_id = data["the_id"]
            created = data["created"]
            content = data["content"]

            pos_num, neg_num, bias = request_emotion_api(content)

            self.mysql.save(MYSQL_EMOTION_TABLE_NAME,
                            {
                                "the_id": the_id,
                                "code": code,
                                "time": time_str,
                                "created": created,
                                "Negative": neg_num,
                                "Positive": pos_num,
                                "Bias": bias
                            })

        except Exception as e:
            print("emotion | error : {}".format(e))



if __name__ == "__main__":
    text_emotion_task = TextEmotionTask(bootstrap_servers=BOOTSTRAP_SERVERS,
                                        group_id=STOCK_EMOTION_GROUP_ID,
                                        topics=STOCK_NEWS_TOPICS,
                                        max_workers=KAFKA_MAX_WORKERS)
    text_emotion_task.run()
