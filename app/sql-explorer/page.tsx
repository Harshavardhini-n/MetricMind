"use client";
import { useState } from "react";
import { api } from "@/lib/api";
import type { QueryResult } from "@/lib/snowflake/types";

export default function Explorer(){
  const [sql,setSql]=useState("SELECT CURRENT_USER() AS current_user, CURRENT_ROLE() AS current_role, CURRENT_WAREHOUSE() AS current_warehouse");
  const [result,setResult]=useState<QueryResult>(); const [error,setError]=useState(""); const [loading,setLoading]=useState(false);
  const run=async()=>{setError("");setResult(undefined);setLoading(true);try{const r=await api<QueryResult>("/api/query",{method:"POST",body:JSON.stringify({sql})});if(r.success)setResult(r.data);else setError(r.error?.message||"Query failed")}catch{setError("Unable to reach the MetricMind API.")}finally{setLoading(false)}};
  return <><div className="eyebrow">Controlled query workspace</div><h1 className="page-title">SQL Explorer</h1><p className="muted">Only read-only SQL is permitted. Results are capped at 1,000 rows by default.</p><div className="form-row"><button className="button" onClick={run} disabled={loading}>{loading?"Connecting to Snowflake…":"Execute query"}</button><button className="secondary" onClick={()=>navigator.clipboard.writeText(sql)}>Copy SQL</button></div><textarea className="editor" value={sql} onChange={e=>setSql(e.target.value)} aria-label="SQL editor"/>{error&&<div className="notice" style={{marginTop:12}}>{error}</div>}{result&&<div className="card" style={{marginTop:16}}><span className="status"><i className="dot"/> {result.rowCount} rows · {result.executionTimeMs} ms</span><table className="table"><thead><tr>{result.columns.map(x=><th key={x}>{x}</th>)}</tr></thead><tbody>{result.rows.map((row,i)=><tr key={i}>{result.columns.map(c=><td key={c}>{String(row[c]??"")}</td>)}</tr>)}</tbody></table></div>}</>}
