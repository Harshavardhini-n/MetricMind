import type { ApiResponse } from "@/types";
export async function api<T>(path:string, options?:RequestInit):Promise<ApiResponse<T>>{const r=await fetch(path,{headers:{"Content-Type":"application/json",...options?.headers},...options});return r.json()}
