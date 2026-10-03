
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression


def build_model():

    trf = ColumnTransformer(
        transformers=[
            ("encoder",
             OneHotEncoder(drop="first"),
             ["batting_team","bowling_team","city"])
        ],
        remainder="passthrough"
    )

    pipe = Pipeline([
        ("preprocess", trf),
        ("model", LogisticRegression(solver="liblinear"))
    ])

    return pipe