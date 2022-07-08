from collections import namedtuple



DataIngestionArtifact = namedtuple(" DataIngestionArtifact",
["train_file_path"," test_file_path","is_ingested","message"])  # DataIngestionArtifact is output. it use for next input datavalidation here it is used for two path(train and test)  is ingested is = we ingested is successfulk or not. we can write any message.
