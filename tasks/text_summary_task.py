# -*- coding: utf-8 -*-

import time
import json

from utils.KafkaUtils import KafkaConsumerRunner
from utils.Apiutils import request_summary_api
from utils.MySqlUtils import MysqlClass
from settings import *

class TextSummaryTask(KafkaConsumerRunner):

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

            summary = request_summary_api(content)["summary"]

            time_array = time.strptime(time_str, "%Y-%m-%d %H:%M:%S")
            timestamp = time.mktime(time_array)

            self.mysql.save(MYSQL_SUMMARY_TABLE_NAME,
                            {
                                "the_id": the_id,
                                "code": code,
                                "time": timestamp,
                                "created": created,
                                "summary": summary
                            })

        except Exception as e:
            print("summary | error : {}".format(e))


if __name__ == "__main__":
    text_summary_task = TextSummaryTask(bootstrap_servers=BOOTSTRAP_SERVERS,
                                        group_id=STOCK_NEWS_GROUP_ID,
                                        topics=STOCK_NEWS_TOPICS,
                                        max_workers=KAFKA_MAX_WORKERS)
    text_summary_task.run()
