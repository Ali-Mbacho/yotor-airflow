from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


def fetch_data_from_telegram():
    bot = telegram.Bot(token = "xxxxx")
    messages = bot.get_chat_messages(chat_id= "https://t.me/kenyamovieclub")
    return messages



def format_telegram_data(messages):
    formated_data = []
    for message in messages:
        formated_message = {
            "text": message.text,
            "date":message.date.strftime('%Y-%m-%d %H:%M:%S'),
        }
        formated_data.append(formated_message)
    return formated_message

def store_data():
    pass

default_args = {
    'owner': 'sparta',
    'retries': 5, 
    'retry_delay':timedelta(minutes=2)
}


#define the dag
dag = DAG (
    "Telegram to database",
    description= "fetch data from telegram store and stores in database",
    schedule_interval="@daily",
    # choose this start date based on the specific dates you want to run the script
    start_date=datetime(2023, 5, 21),
    default_args=default_args,
    catchup=False

)

fetch_task = PythonOperator(
    task_id = "fetch-data",
    python_callable=fetch_data_from_telegram,
    dag = dag
)

format_task = PythonOperator(
    task_id = "format_data",
    python_callable=format_telegram_data,
    dag = dag
)

store_task = PythonOperator(
    task_id = "store_data",
    python_callable=store_data,
    dag= dag
 
)

fetch_task >> format_task >> store_task


