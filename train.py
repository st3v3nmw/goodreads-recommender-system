import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import pandas as pd
from libreco.algorithms import NCF
from libreco.data import DatasetPure, random_split


data = pd.read_csv("data/ratings.csv")
train_data, eval_data = random_split(data, multi_ratios=[0.7, 0.3])

train_data, data_info = DatasetPure.build_trainset(train_data)
eval_data = DatasetPure.build_evalset(eval_data)

model = NCF(
    "rating",
    data_info,
    embed_size=16,
    n_epochs=64,
    lr=0.01,
    lr_decay=True,
    reg=None,
    batch_size=256,
    num_neg=1,
    use_bn=True,
    dropout_rate=None,
    hidden_units="128,64,32",
    tf_sess_config=None,
)
model.fit(
    train_data,
    verbose=2,
    eval_data=eval_data,
    shuffle=True,
    metrics=["rmse", "mae", "r2"],
)

data_info.save(path="model")
model.save(path="model", model_name="model", manual=True, inference_only=True)
