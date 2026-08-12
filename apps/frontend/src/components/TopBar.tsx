"use client";

import React from "react";

export default function TopBar() {
  return (
    <header className="topbar">
      <div className="topbar-left">
        <div className="topbar-brand">
          MetricMind
        </div>

        <div className="topbar-title">
          AI Business Analyst
        </div>
      </div>

      <div className="topbar-right">
        <div className="connection-status">
          <span className="status-dot" />
          Snowflake Connected
        </div>

        <div className="user-avatar">
          U
        </div>
      </div>
    </header>
  );
}