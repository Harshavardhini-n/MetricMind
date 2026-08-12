import "server-only";
import { connection } from "./client";
import { validateSql } from "./validate-sql";
import type { QueryResult } from "./types";
export async function executeReadOnly(sql:string):Promise<QueryResult>{const check=validateSql(sql);if(!check.valid)throw new Error(check.error);const started=Date.now(),conn=await connection(),limit=Math.min(Number(process.env.SNOWFLAKE_QUERY_ROW_LIMIT||1000),5000);try{return await new Promise((resolve,reject)=>conn.execute({sqlText:`SELECT * FROM (${check.sql}) AS metricmind_safe_query LIMIT ${limit}`,complete:(err,stmt,rows)=>err?reject(err):resolve({columns:(stmt.getColumns()||[]).map((c:{getName():string})=>c.getName()),rows:rows||[],rowCount:(rows||[]).length,executionTimeMs:Date.now()-started,queryId:stmt.getStatementId()} as QueryResult)}))}finally{conn.destroy(()=>undefined)}}
export async function discoverModels(){const result=await executeReadOnly("SELECT table_name FROM information_schema.tables WHERE table_schema = CURRENT_SCHEMA()");return result.rows}
