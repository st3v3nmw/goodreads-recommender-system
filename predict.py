import csv
import os
from random import shuffle

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from libreco.algorithms import NCF
from libreco.data import DataInfo

MY_USER_ID = 16777216

data_info = DataInfo.load("model")
model = NCF.load(path="model", model_name="model", data_info=data_info, manual=True)

to_read_shelf = []
with open("data/goodreads_library_export.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["My Rating"] == "0":
            row["Predicted Rating"] = model.predict(user=MY_USER_ID, item=row["Title"])[
                0
            ]
            to_read_shelf.append(row)
    shuffle(to_read_shelf)
    to_read_shelf.sort(key=lambda x: x["Predicted Rating"], reverse=True)

print("\n\nRESULTS")
for book in to_read_shelf:
    print(
        f"{book['Title']} by {book['Author']} [{book['Publisher']}] @ {book['Predicted Rating']:.4f}"
    )

print("\n\nRECOMMENDATIONS")
print("Top 3")
for book in to_read_shelf[:3]:
    print(
        f"{book['Title']} by {book['Author']} [{book['Publisher']}] @ {book['Predicted Rating']:.4f}"
    )

print("\nMid")
mid = to_read_shelf[int(len(to_read_shelf) / 2)]
print(
    f"{mid['Title']} by {mid['Author']} [{mid['Publisher']}] @ {mid['Predicted Rating']:.4f}"
)

print("\nLast")
last = to_read_shelf[-1]
print(
    f"{last['Title']} by {last['Author']} [{last['Publisher']}] @ {last['Predicted Rating']:.4f}"
)
