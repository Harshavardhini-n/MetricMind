"use client";

import React, { useState } from "react";

import Sidebar from "../components/Sidebar";
import TopBar from "../components/TopBar";
import ChatPanel from "../components/ChatPanel";

type DashboardTab =
  | "overview"
  | "analyst"
  | "regional"
  | "quarterly"
  | "profit"
  | "sources"
  | "settings";

const regionalRevenue = [
  { region: "West", value: 725457.93 },
  { region: "East", value: 678781.36 },
  { region: "Central", value: 501239.88 },
  { region: "South", value: 391721.9 },
];

const quarterlyRevenue = [
  { quarter: "Q1", value: 66551.8 },
  { quarter: "Q2", value: 127445.61 },
  { quarter: "Q3", value: 187768.81 },
  { quarter: "Q4", value: 297015.14 },
];

const totalRevenue = 2297201.07;
const totalProfit = 286397.79;
const totalCost = totalRevenue - totalProfit;

function formatCurrency(value: number) {
  return `$${value.toLocaleString("en-US", {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  })}`;
}

function formatCompactCurrency(value: number) {
  if (value >= 1_000_000) {
    return `$${(value / 1_000_000).toFixed(2)}M`;
  }

  if (value >= 1_000) {
    return `$${(value / 1_000).toFixed(2)}K`;
  }

  return formatCurrency(value);
}

/* =========================================================
   STAT CARD
========================================================= */

function StatCard({
  title,
  value,
  description,
  accent = false,
}: {
  title: string;
  value: string;
  description: string;
  accent?: boolean;
}) {
  return (
    <div className={`stat-card ${accent ? "stat-card-accent" : ""}`}>
      <div className="stat-card-title">{title}</div>

      <div className="stat-card-value">{value}</div>

      <div className="stat-card-description">{description}</div>
    </div>
  );
}

/* =========================================================
   SECTION HEADER
========================================================= */

function SectionHeader({
  eyebrow,
  title,
  description,
}: {
  eyebrow: string;
  title: string;
  description: string;
}) {
  return (
    <div className="section-header">
      <div className="section-eyebrow">{eyebrow}</div>

      <h1>{title}</h1>

      <p>{description}</p>
    </div>
  );
}

/* =========================================================
   OVERVIEW
========================================================= */

function OverviewDashboard({
  setTab,
}: {
  setTab: (tab: DashboardTab) => void;
}) {
  const maxRevenue = Math.max(
    ...regionalRevenue.map((item) => item.value)
  );

  return (
    <div className="dashboard-content">
      <SectionHeader
        eyebrow="BUSINESS INTELLIGENCE"
        title="Overview"
        description="Monitor key business metrics and performance."
      />

      {/* TOP METRICS */}

      <div className="stats-grid">
        <StatCard
          title="TOTAL REVENUE"
          value={formatCompactCurrency(totalRevenue)}
          description="Full year • All regions"
          accent
        />

        <StatCard
          title="TOTAL PROFIT"
          value={formatCompactCurrency(totalProfit)}
          description="Full year • All regions"
        />

        <StatCard
          title="PROFIT MARGIN"
          value={`${((totalProfit / totalRevenue) * 100).toFixed(2)}%`}
          description="Profit / Revenue"
        />

        <StatCard
          title="TOTAL COST"
          value={formatCompactCurrency(totalCost)}
          description="Full year • All regions"
        />
      </div>

      {/* MAIN DASHBOARD */}

      <div className="dashboard-grid">
        {/* REVENUE */}

        <div className="panel large-panel">
          <div className="panel-header">
            <div>
              <h2>Revenue by Region</h2>

              <p>Full-year revenue distribution</p>
            </div>

            <button
              className="panel-action"
              onClick={() => setTab("regional")}
            >
              View details →
            </button>
          </div>

          <div className="bar-chart">
            {regionalRevenue.map((item) => {
              const percentage =
                (item.value / maxRevenue) * 100;

              return (
                <div className="bar-row" key={item.region}>
                  <div className="bar-label">
                    <span>{item.region}</span>

                    <strong>
                      {formatCurrency(item.value)}
                    </strong>
                  </div>

                  <div className="bar-track">
                    <div
                      className="bar-fill"
                      style={{
                        width: `${percentage}%`,
                      }}
                    />
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* AI PREVIEW */}

        <div className="panel">
          <div className="panel-header">
            <div>
              <h2>AI Analyst</h2>

              <p>Ask questions in natural language</p>
            </div>

            <div className="chat-status">
              <span className="status-dot" />
              Live
            </div>
          </div>

          <div className="ai-preview">
            <div className="ai-icon">AI</div>

            <div>
              <strong>MetricMind Agent</strong>

              <p>
                Ask about revenue, profit, cost, regions,
                quarters and business performance.
              </p>
            </div>
          </div>

          <div className="example-question">
            “Which region has the highest revenue?”
          </div>

          <button
            className="primary-button full-width"
            onClick={() => setTab("analyst")}
          >
            Open AI Analyst
          </button>
        </div>
      </div>

      {/* QUARTERLY */}

      <div className="panel">
        <div className="panel-header">
          <div>
            <h2>Quarterly Revenue</h2>

            <p>Quarterly breakdown</p>
          </div>

          <button
            className="panel-action"
            onClick={() => setTab("quarterly")}
          >
            Full analysis →
          </button>
        </div>

        <div className="quarter-grid">
          {quarterlyRevenue.map((item) => (
            <div
              className="quarter-card"
              key={item.quarter}
            >
              <span>{item.quarter}</span>

              <strong>
                {formatCurrency(item.value)}
              </strong>
            </div>
          ))}
        </div>
      </div>

      {/* TRANSPARENCY */}

      <div className="panel transparency-panel">
        <div className="panel-header">
          <div>
            <h2>How MetricMind Works</h2>

            <p>
              Business questions are converted into
              governed metric queries instead of allowing
              the LLM to invent numbers.
            </p>
          </div>
        </div>

        <div className="pipeline">
          <div className="pipeline-step">
            <span>01</span>

            <strong>User Question</strong>

            <small>Natural language</small>
          </div>

          <div className="pipeline-arrow">→</div>

          <div className="pipeline-step">
            <span>02</span>

            <strong>MetricMind Agent</strong>

            <small>Intent detection</small>
          </div>

          <div className="pipeline-arrow">→</div>

          <div className="pipeline-step">
            <span>03</span>

            <strong>Semantic Layer</strong>

            <small>Governed metric</small>
          </div>

          <div className="pipeline-arrow">→</div>

          <div className="pipeline-step">
            <span>04</span>

            <strong>Snowflake</strong>

            <small>Verified data</small>
          </div>

          <div className="pipeline-arrow">→</div>

          <div className="pipeline-step">
            <span>05</span>

            <strong>Answer</strong>

            <small>Natural language</small>
          </div>
        </div>
      </div>
    </div>
  );
}

/* =========================================================
   AI ANALYST
========================================================= */

function AnalystDashboard() {
  return (
    <div className="dashboard-content analyst-page">
      <SectionHeader
        eyebrow="AI BUSINESS ANALYST"
        title="Ask MetricMind"
        description="Query governed business metrics using natural language."
      />

      <div className="analyst-layout">
        <div className="analyst-info">
          <div className="analyst-hero">
            <div className="ai-icon large">AI</div>

            <h2>MetricMind Agent</h2>

            <p>
              Ask questions about your business data.
            </p>

            <div className="question-list">
              <div>
                Which region has the highest revenue?
              </div>

              <div>
                What is the total revenue for Q1?
              </div>

              <div>
                Which region has the lowest revenue?
              </div>

              <div>
                Compare revenue across all regions.
              </div>
            </div>
          </div>
        </div>

        <ChatPanel />
      </div>
    </div>
  );
}

/* =========================================================
   REGIONAL
========================================================= */

function RegionalDashboard() {
  const maxRevenue = Math.max(
    ...regionalRevenue.map((item) => item.value)
  );

  const highest = regionalRevenue[0];

  const lowest =
    regionalRevenue[regionalRevenue.length - 1];

  return (
    <div className="dashboard-content">
      <SectionHeader
        eyebrow="ANALYTICS"
        title="Regional Revenue"
        description="Compare full-year revenue across business regions."
      />

      <div className="stats-grid three">
        <StatCard
          title="HIGHEST REGION"
          value={highest.region}
          description={formatCurrency(highest.value)}
          accent
        />

        <StatCard
          title="LOWEST REGION"
          value={lowest.region}
          description={formatCurrency(lowest.value)}
        />

        <StatCard
          title="TOTAL REVENUE"
          value={formatCompactCurrency(totalRevenue)}
          description="All regions"
        />
      </div>

      <div className="panel">
        <div className="panel-header">
          <div>
            <h2>Regional Performance</h2>

            <p>Revenue ranking</p>
          </div>
        </div>

        <div className="ranking-list">
          {regionalRevenue.map((item, index) => {
            const percentage =
              (item.value / maxRevenue) * 100;

            return (
              <div
                className="ranking-item"
                key={item.region}
              >
                <div className="rank-number">
                  #{index + 1}
                </div>

                <div className="ranking-main">
                  <div className="ranking-top">
                    <strong>{item.region}</strong>

                    <span>
                      {formatCurrency(item.value)}
                    </span>
                  </div>

                  <div className="bar-track">
                    <div
                      className="bar-fill"
                      style={{
                        width: `${percentage}%`,
                      }}
                    />
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

/* =========================================================
   QUARTERLY
========================================================= */

function QuarterlyDashboard() {
  const maxValue = Math.max(
    ...quarterlyRevenue.map((item) => item.value)
  );

  const highest = quarterlyRevenue.reduce(
    (a, b) => (a.value > b.value ? a : b)
  );

  const quarterlyTotal = quarterlyRevenue.reduce(
    (sum, item) => sum + item.value,
    0
  );

  return (
    <div className="dashboard-content">
      <SectionHeader
        eyebrow="TIME ANALYSIS"
        title="Quarterly Revenue"
        description="Drill down into revenue performance by quarter."
      />

      <div className="stats-grid three">
        <StatCard
          title="BEST QUARTER"
          value={highest.quarter}
          description={formatCurrency(highest.value)}
          accent
        />

        <StatCard
          title="TOTAL"
          value={formatCompactCurrency(quarterlyTotal)}
          description="Quarterly dataset"
        />

        <StatCard
          title="PERIOD"
          value="Q1 → Q4"
          description="Quarterly breakdown"
        />
      </div>

      <div className="panel">
        <div className="panel-header">
          <div>
            <h2>Quarterly Performance</h2>

            <p>Revenue by quarter</p>
          </div>
        </div>

        <div className="quarter-bars">
          {quarterlyRevenue.map((item) => {
            const height =
              (item.value / maxValue) * 100;

            return (
              <div
                className="quarter-column"
                key={item.quarter}
              >
                <div className="quarter-value">
                  {formatCurrency(item.value)}
                </div>

                <div className="column-track">
                  <div
                    className="column-fill"
                    style={{
                      height: `${height}%`,
                    }}
                  />
                </div>

                <strong>{item.quarter}</strong>
              </div>
            );
          })}
        </div>
      </div>
    </div>
  );
}

/* =========================================================
   PROFIT
========================================================= */

function ProfitDashboard() {
  const margin =
    (totalProfit / totalRevenue) * 100;

  return (
    <div className="dashboard-content">
      <SectionHeader
        eyebrow="FINANCIAL ANALYTICS"
        title="Profit Dashboard"
        description="Monitor business profitability using governed metrics."
      />

      <div className="stats-grid">
        <StatCard
          title="TOTAL PROFIT"
          value={formatCompactCurrency(totalProfit)}
          description="Full year"
          accent
        />

        <StatCard
          title="REVENUE"
          value={formatCompactCurrency(totalRevenue)}
          description="Full year"
        />

        <StatCard
          title="PROFIT MARGIN"
          value={`${margin.toFixed(2)}%`}
          description="Profit / Revenue"
        />

        <StatCard
          title="TOTAL COST"
          value={formatCompactCurrency(totalCost)}
          description="Full year"
        />
      </div>

      <div className="panel">
        <div className="panel-header">
          <div>
            <h2>Profitability Overview</h2>

            <p>
              Governed profitability metrics from
              MetricMind.
            </p>
          </div>
        </div>

        <div className="profit-summary">
          <div className="profit-ring">
            <span>{margin.toFixed(1)}%</span>
          </div>

          <div className="profit-details">
            <div>
              <span>Total revenue</span>

              <strong>
                {formatCurrency(totalRevenue)}
              </strong>
            </div>

            <div>
              <span>Total profit</span>

              <strong>
                {formatCurrency(totalProfit)}
              </strong>
            </div>

            <div>
              <span>Total cost</span>

              <strong>
                {formatCurrency(totalCost)}
              </strong>
            </div>

            <div>
              <span>Profit margin</span>

              <strong>
                {margin.toFixed(2)}%
              </strong>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

/* =========================================================
   DATA SOURCES
========================================================= */

function SourcesDashboard() {
  return (
    <div className="dashboard-content">
      <SectionHeader
        eyebrow="DATA INFRASTRUCTURE"
        title="Data Sources"
        description="Monitor the systems MetricMind uses to retrieve governed business data."
      />

      <div className="source-grid">
        <div className="source-card connected">
          <div className="source-status">
            <span />
            Connected
          </div>

          <h2>Snowflake</h2>

          <p>
            Primary analytical warehouse used by
            MetricMind for business metrics.
          </p>

          <div className="source-details">
            <div>
              <span>Database</span>
              <strong>METRICMIND_DB</strong>
            </div>

            <div>
              <span>Schema</span>
              <strong>RAW</strong>
            </div>

            <div>
              <span>Table</span>
              <strong>SALES_ORDERS</strong>
            </div>
          </div>
        </div>

        <div className="source-card">
          <div className="source-status">
            <span />
            Internal
          </div>

          <h2>Semantic Catalog</h2>

          <p>
            Defines available metrics, dimensions and
            business interpretation before data is queried.
          </p>

          <div className="metric-tags">
            <span>Revenue</span>
            <span>Profit</span>
            <span>Margin</span>
            <span>Cost</span>
          </div>
        </div>
      </div>

      <div className="panel">
        <div className="panel-header">
          <div>
            <h2>Architecture</h2>

            <p>MetricMind data flow</p>
          </div>
        </div>

        <div className="architecture-flow">
          <div>Frontend</div>

          <span>→</span>

          <div>FastAPI</div>

          <span>→</span>

          <div>MetricMind Agent</div>

          <span>→</span>

          <div>Semantic Layer</div>

          <span>→</span>

          <div>Snowflake</div>
        </div>
      </div>
    </div>
  );
}

/* =========================================================
   SETTINGS
========================================================= */

function SettingsDashboard() {
  return (
    <div className="dashboard-content">
      <SectionHeader
        eyebrow="SYSTEM"
        title="Settings"
        description="MetricMind configuration and system information."
      />

      <div className="settings-list">
        <div className="setting-row">
          <div>
            <strong>Analytics Provider</strong>

            <span>Snowflake</span>
          </div>

          <div className="status-badge success">
            Connected
          </div>
        </div>

        <div className="setting-row">
          <div>
            <strong>Semantic Metrics</strong>

            <span>
              Revenue, Profit, Margin, Cost
            </span>
          </div>

          <div className="status-badge success">
            Active
          </div>
        </div>

        <div className="setting-row">
          <div>
            <strong>Agent</strong>

            <span>MetricMind Agent</span>
          </div>

          <div className="status-badge success">
            Ready
          </div>
        </div>

        <div className="setting-row">
          <div>
            <strong>Environment</strong>

            <span>Development</span>
          </div>

          <div className="status-badge">
            Local
          </div>
        </div>
      </div>
    </div>
  );
}

/* =========================================================
   PAGE
========================================================= */

export default function HomePage() {
  const [activeTab, setActiveTab] =
    useState<DashboardTab>("overview");

  const renderContent = () => {
    switch (activeTab) {
      case "overview":
        return (
          <OverviewDashboard
            setTab={setActiveTab}
          />
        );

      case "analyst":
        return <AnalystDashboard />;

      case "regional":
        return <RegionalDashboard />;

      case "quarterly":
        return <QuarterlyDashboard />;

      case "profit":
        return <ProfitDashboard />;

      case "sources":
        return <SourcesDashboard />;

      case "settings":
        return <SettingsDashboard />;

      default:
        return (
          <OverviewDashboard
            setTab={setActiveTab}
          />
        );
    }
  };

  return (
    <div className="metricmind-app">
      <Sidebar
        activeTab={activeTab}
        onNavigate={setActiveTab}
      />

      <div className="metricmind-main">
        <TopBar />

        <main className="metricmind-body">
          {renderContent()}
        </main>
      </div>
    </div>
  );
}