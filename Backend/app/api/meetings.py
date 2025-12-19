import uuid
from fastapi import APIRouter, UploadFile, File, Depends

from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.storage import save_audio_file
from app.models.meeting import Meeting

router = APIRouter(prefix="/meetings", tags=["Meetings"])


@router.post("/upload")
def upload_meeting_audio(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    meeting_id = str(uuid.uuid4())

    audio_path = save_audio_file(file)

    meeting = Meeting(
        id=meeting_id,
        audio_path=audio_path,
        status="uploaded",
    )

    db.add(meeting)
    db.commit()

    return {
        "meeting_id": meeting_id,
        "status": "uploaded",
    }
