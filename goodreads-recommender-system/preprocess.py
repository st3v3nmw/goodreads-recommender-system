import csv


RATINGS_CSVS = [
    "data/original/user_rating_0_to_1000.csv",
    "data/original/user_rating_1000_to_2000.csv",
    "data/original/user_rating_2000_to_3000.csv",
    "data/original/user_rating_3000_to_4000.csv",
    "data/original/user_rating_4000_to_5000.csv",
    "data/original/user_rating_5000_to_6000.csv",
    "data/original/user_rating_6000_to_11000.csv",
]
GOODREADS_EXPORT_PATH = "data/goodreads_library_export.csv"
GOODREADS_OFFICIAL_RATING_SYSTEM = {
    "did not like it": 1,
    "it was ok": 2,
    "liked it": 3,
    "really liked it": 4,
    "it was amazing": 5,
}
RATINGS_OUT = "data/ratings.csv"
MY_USER_ID = 16777216


with open(RATINGS_OUT, "w") as out:
    writer = csv.DictWriter(out, fieldnames=["user", "item", "label"])
    writer.writeheader()
    for file_path in RATINGS_CSVS:
        print(file_path)
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row["Rating"] == "This user doesn't have any rating":
                    continue

                writer.writerow(
                    {
                        "user": row["ID"],
                        "item": row["Name"],
                        "label": GOODREADS_OFFICIAL_RATING_SYSTEM[row["Rating"]],
                    }
                )

    with open(GOODREADS_EXPORT_PATH, "r") as f:
        print(GOODREADS_EXPORT_PATH)
        reader = csv.DictReader(f)
        for row in reader:
            if row["My Rating"] != "0":
                writer.writerow(
                    {
                        "user": MY_USER_ID,
                        "item": row["Title"],
                        "label": row["My Rating"],
                    }
                )
