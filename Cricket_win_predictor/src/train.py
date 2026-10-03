
import pickle
from sklearn.model_selection import train_test_split

from data_pipeline import load_data, merge_data
from feature_engineering import create_features
from model import build_model


matches, deliveries = load_data()

match_df = merge_data(matches, deliveries)

final_df = create_features(match_df, deliveries)

X = final_df.drop("result",axis=1)
y = final_df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,y,test_size=0.2,random_state=1
)

model = build_model()

model.fit(X_train,y_train)

pickle.dump(model,open("models/pipe.pkl","wb"))

print("Model trained and saved")