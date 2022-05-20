from fastapi import APIRouter, File, UploadFile

from ..types import AnalyzeParameter, APIResponse


router = APIRouter()


@router.post("/analyze/{obj_id}", tags=["analyze"], response_model=APIResponse)
async def post_analyze(obj_id: str, parameters: AnalyzeParameter):
    """分析を実行します
    """
    print(obj_id)
    print(AnalyzeParameter)
    return APIResponse(message="ok", status_code=0)
