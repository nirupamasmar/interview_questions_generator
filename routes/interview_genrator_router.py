from fastapi import APIRouter
from models.ques_schema import job_role_r
from services.question_generator import qa_generator_agent

router = APIRouter()


@router.post("/generate")
async def inter_generator(request:job_role_r):
    questions = qa_generator_agent(request.job_role)
    return {"interview questions":questions}
    