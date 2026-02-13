export interface QuantumResult {
    branch: string;
    energy: number;
}
export function compute(): QuantumResult {
    return { branch: "green-ammonia-opt", energy: Math.random() };
}
