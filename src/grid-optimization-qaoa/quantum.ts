export interface QuantumResult {
    branch: string;
    energy: number;
}
export function compute(): QuantumResult {
    return { branch: "grid-optimization-qaoa", energy: Math.random() };
}
