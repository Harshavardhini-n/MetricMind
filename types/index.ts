export type ChartType="bar"|"line"|"area"|"pie"|"donut"|"scatter"|"heatmap"|"kpi"|"table";
export type BIResponse={answer:string;sql?:string;chart?:{type:ChartType;title?:string;xKey?:string;yKeys?:string[];data:Record<string,unknown>[]};confidence:number;semanticModel?:string;warehouse?:string;executionTime?:number;rows?:number;recommendations?:string[];insights?:string[];sources?:string[];queryId?:string};
export type ApiResponse<T>={success:boolean;data?:T;error?:{code:string;message:string;details?:unknown};meta?:{executionTimeMs?:number;requestId?:string;demoMode?:boolean}};
