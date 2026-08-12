"use client";

import React, { useState, useCallback, useRef } from "react";

export default function QueryInput({ onSend, disabled }: { onSend: (m: string) => Promise<void> | void; disabled?: boolean }) {
  const [text, setText] = useState("");
  const taRef = useRef<HTMLTextAreaElement | null>(null);

  const submit = useCallback(async () => {
    const trimmed = text.trim();
    if (!trimmed) return;
    setText("");
    await onSend(trimmed);
  }, [text, onSend]);

  return (
    <div>
      <label style={{ display: "none" }} htmlFor="query">Ask MetricMind</label>
      <div className="query-input">
        <textarea
          id="query"
          ref={taRef}
          placeholder="Ask MetricMind about your business data..."
          value={text}
          onChange={(e) => setText(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !e.shiftKey) {
              e.preventDefault();
              void submit();
            }
          }}
          disabled={disabled}
        />
        <button onClick={() => void submit()} disabled={disabled} aria-label="Send">
          Send
        </button>
      </div>
    </div>
  );
}
