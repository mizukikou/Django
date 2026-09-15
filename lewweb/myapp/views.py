import pickle
from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render


MODEL_PATH = Path(__file__).resolve().parent.parent / "LinearRegressionModel.pkl"
DISTRICTS = (
    "台北市信義區",
    "台北市大安區",
    "台南市東區",
    "新北市新店區",
    "新北市板橋區",
    "桃園市中壢區",
    "高雄市左營區",
)


def _load_model():
    with MODEL_PATH.open("rb") as model_file:
        return pickle.load(model_file)


def index(request):
    return HttpResponse('<b>Welcome to the Index Page!</b><br><a href="/predict/">房價預測</a>')


def predict(request):
    context = {"districts": DISTRICTS}

    if request.method == "POST":
        try:
            features = [
                float(request.POST["area"]),
                float(request.POST["age"]),
                float(request.POST["rooms"]),
                float(request.POST["floor"]),
                float(request.POST["metro_distance"]),
                float(request.POST["school_distance"]),
                float(request.POST["parking"]),
            ]
            district = request.POST["district"]
            if district not in DISTRICTS:
                raise ValueError("無效的行政區")

            features.extend(float(district == selected) for selected in DISTRICTS)
            model = _load_model()
            import pandas as pd

            input_data = pd.DataFrame([features], columns=model.feature_names_in_)
            raw_prediction = float(model.predict(input_data)[0])
            prediction = max(0.0, raw_prediction)
            context["prediction"] = f"{prediction:,.0f}"
            if raw_prediction < 0:
                context["prediction_notice"] = "此組條件已超出模型可解釋範圍，結果已以 0 萬元顯示。"
        except (KeyError, TypeError, ValueError, OSError, ImportError) as error:
            context["error"] = f"請確認輸入資料正確：{error}"

    return render(request, "linear_regression.html", context)


