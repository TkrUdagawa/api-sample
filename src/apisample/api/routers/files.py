from fastapi import APIRouter, File, UploadFile

from ..types import APIResponse


router = APIRouter()


@router.post("/files", tags=["file"], response_model=APIResponse)
async def post_upload_file(upload_file: UploadFile = File(...)):
    """ファイルをアップロードします
    """
    print(upload_file)
    return APIResponse(message="ok", status_code=0)
