from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
import logging
from app.core.dependencies import get_current_user_id
from app.services.ai_service import AIService

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    reply: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    current_user_id: str = Depends(get_current_user_id)
):
    """
    Chat endpoint that accepts user messages and returns AI responses
    """
    try:
        # Log the incoming message for debugging
        logging.info(f"Received chat message from user {current_user_id}: {request.message}")

        # Create an instance of the AI service
        ai_service = AIService()

        # Get AI response using the AI service
        ai_reply = await ai_service.get_chat_response(request.message)

        return ChatResponse(reply=ai_reply)

    except Exception as e:
        logging.error(f"Error processing chat request: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")