"use client";

import React, { useState } from "react";

import { ChatMessage } from "../types";
import QueryInput from "./QueryInput";
import QuickQueries from "./QuickQueries";
import { sendChatMessage } from "../lib/api";

function nowId() {
  return `${Date.now()}-${Math.random().toString(36).slice(2, 9)}`;
}

export default function ChatPanel() {
  const [messages, setMessages] = useState<ChatMessage[]>([
    {
      id: nowId(),
      role: "assistant",
      content:
        "Hello. I'm MetricMind, your AI business analyst. Ask me about revenue, profit, cost, margin, regions, or quarterly performance.",
      timestamp: new Date(),
    },
  ]);

  const [loading, setLoading] = useState(false);

  const send = async (text: string) => {
    const trimmed = text.trim();

    if (!trimmed || loading) {
      return;
    }

    const userMessage: ChatMessage = {
      id: nowId(),
      role: "user",
      content: trimmed,
      timestamp: new Date(),
    };

    const loadingId = nowId();

    const loadingMessage: ChatMessage = {
      id: loadingId,
      role: "assistant",
      content: "Analyzing your business data...",
      timestamp: new Date(),
    };

    setMessages((current) => [
      ...current,
      userMessage,
      loadingMessage,
    ]);

    setLoading(true);

    try {
      const answer = await sendChatMessage(trimmed);

      setMessages((current) =>
        current.map((message) =>
          message.id === loadingId
            ? {
                ...message,
                content: answer,
                timestamp: new Date(),
              }
            : message
        )
      );
    } catch (error) {
      console.error("MetricMind chat error:", error);

      let errorMessage =
        "Unable to connect to the MetricMind backend.";

      if (error instanceof Error) {
        errorMessage = error.message;
      }

      setMessages((current) =>
        current.map((message) =>
          message.id === loadingId
            ? {
                ...message,
                content: `Backend error: ${errorMessage}`,
                timestamp: new Date(),
              }
            : message
        )
      );
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-panel card">
      <div className="chat-header">
        <div>
          <div className="chat-title">
            AI Analyst
          </div>

          <div className="chat-subtitle">
            Ask questions about your business data using natural language.
          </div>
        </div>

        <div className="chat-status">
          <span className="status-dot" />
          Live
        </div>
      </div>

      <div className="chat-messages">
        {messages.map((message) => (
          <div
            key={message.id}
            className={`message ${
              message.role === "assistant"
                ? "assistant"
                : "user"
            }`}
          >
            <div className="message-content">
              {message.content.split("\n").map((line, index) => (
                <div key={index}>
                  {line || "\u00A0"}
                </div>
              ))}
            </div>

            <div className="meta">
              {message.timestamp.toLocaleTimeString([], {
                hour: "2-digit",
                minute: "2-digit",
              })}
            </div>
          </div>
        ))}
      </div>

      <div className="chat-footer">
        <QuickQueries
          onQuick={(query) => {
            void send(query);
          }}
        />

        <QueryInput
          onSend={async (message) => {
            await send(message);
          }}
          disabled={loading}
        />
      </div>
    </div>
  );
}