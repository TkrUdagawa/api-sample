from enum import Enum
from typing import Union, Optional

from pydantic import BaseModel


class AnalyzeTask(str, Enum):
    classify = "classify"
    regression = "regression"


class ClassifierMethod(str, Enum):
    svm = "svm"
    random_fores = "random_forest"
    xgboost = "xgboost"
    logistic_regression = "logistic_regression"


class RegressionMethod(str, Enum):
    svm = "svm"
    random_forest = "random_forest"
    xgboost = "xgboost"


class AnalyzeParameter(BaseModel):
    task: AnalyzeTask
    method: Union[ClassifierMethod, RegressionMethod]


class APIResponse(BaseModel):
    message: str
    status_code: int


class Item(BaseModel):
    id: Optional[str]
    title: str
    body: str
