import requests
import toml

from pathlib import Path

from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import input_file_name, substring

vocabulary_schema = StructType([
    StructField("Phrase",StringType(),False),
    StructField("Grammar",StringType(),True),
    StructField("Transcription",StringType(),True),
    StructField("Translation",StringType(),False),
    StructField("Notes",StringType(),True),
    StructField("FileName",StringType(),True)
])

def download_vocabulary(local_store, github_store, github_user, github_token):
    Path(local_store).mkdir(parents=True, exist_ok=True)
    cfgdata = requests.get(f'{github_store}/jdp-apkg.toml', auth=(github_user, github_token))
    cfg = toml.loads(cfgdata.text)
    for i in cfg['data']:
        datafile = Path(f'{local_store}/{i["filename"]}')
        datafile.parent.mkdir(parents=True, exist_ok=True)
        if not datafile.is_file():
            with requests.get(f'{github_store}/{i["filename"]}', stream=True, auth=(github_user, github_token)) as r:
                r.raise_for_status()
                with datafile.open(mode='wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)

def read_vocabulary(spark_session, data_folder, schema):
    len_data_folder = len(data_folder) + 9
    len_file_name = len_data_folder + 32
    return \
        spark_session.read \
            .format("csv") \
            .option("header",True) \
            .option("recursiveFileLookup", "true") \
            .options(delimiter="\t") \
            .schema(schema) \
            .load(data_folder) \
            .withColumn("FileName", substring(input_file_name(), len_data_folder, len_file_name))

def get_vocabulary_duplicates(vocabulary):
    vocabulary_distinct = vocabulary.drop("FileName").distinct()
    indexDuplicates = vocabulary_distinct \
        .groupBy("Phrase") \
        .count() \
        .where("count > 1") \
        .drop("count")
    duplicates = vocabulary \
        .join(indexDuplicates, ["Phrase"],"left_semi") \
        .sort("Phrase")
    return duplicates

def save_vocabulary(vocabulary, data_folder):
    vocabulary \
        .coalesce(1) \
        .write.mode('overwrite') \
        .options(header='True', delimiter="\t") \
        .option("emptyValue", "") \
        .csv(data_folder)