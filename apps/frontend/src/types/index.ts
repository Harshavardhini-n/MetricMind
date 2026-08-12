export interface ChatRequest {
  message: string;
}

export interface ChatResponse {
  response: string;
}

export interface ChatMessage {
  id: string;
  role: "user" | "assistant";
  content: string;
  timestamp: Date;
}
